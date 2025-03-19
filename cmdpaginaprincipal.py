from PySide6.QtWidgets import QMessageBox, QInputDialog, QLineEdit
from conexao_db import conexaoDB
import datetime

class cmdPaginaPrincipal():
    def __init__(self, tela_principal):
        self.conexao = conexaoDB()
        self.tela_principal = tela_principal
        self.tela_principal.stackedWidget_7.setCurrentIndex(0)

        cursor = self.conexao.get_cursor()
        comando = "select id_usuario from usuarios where nome = %s"
        cursor.execute(comando, (self.tela_principal.txt_ola_user.text(),))
        self.id_user = cursor.fetchone()[0]
        cursor.close()

        
    def tela_abrir_caixa(self):
        self.tela_principal.stackedWidget_7.setCurrentIndex(1)
    
    def tela_fechar_caixa(self):
        self.tela_principal.stackedWidget_7.setCurrentIndex(2)

    def tela_sangria(self):
        self.tela_principal.stackedWidget_7.setCurrentIndex(3)

    def tela_suprimento(self):
        self.tela_principal.stackedWidget_7.setCurrentIndex(4)

    def cancelar_acao(self):
        self.tela_principal.stackedWidget_7.setCurrentIndex(0)

    def abrir_caixa(self):
        quant_init = self.tela_principal.input_quantidade_caixa_abrir.text()
        
        self.hoje = datetime.date.today()

        cursor = self.conexao.get_cursor()
        comando = "select sum(valor_total) from vendas where data_venda = %s and id_forma_pagamento = 4"
        cursor.execute(comando, (self.hoje, ))
        self.total_vendas_dia = cursor.fetchone()[0]
        if self.total_vendas_dia is None:
            self.total_vendas_dia = 0

        if float(quant_init) < float(self.total_vendas_dia):
            QMessageBox.warning(None, "error", "Quantidade Menor que Total no Caixa!")
            return
        
        comando = "insert into caixa (id_user, saldo_ini, status) values (%s, %s, %s)"
        valores = (self.id_user, quant_init, "1")
        cursor.execute(comando, valores)
        self.conexao.commit()
        QMessageBox.information(None, "Sucesso", "Caixa Aberto!")
        self.tela_principal.stackedWidget_7.setCurrentIndex(0)

    def registrar_sangria(self):
        valor_sangria = float(self.tela_principal.input_valor_sangria.text())
        vendedor_resp = self.tela_principal.input_vendedor_responsavel_sangria.text()
        obs_sangria = self.tela_principal.input_obs_sangria.text()

        if valor_sangria is None:
            QMessageBox.warning(None, "error", "Digite um valor para sangria!")
            return
        
        if valor_sangria and not valor_sangria.replace(" ", "").isdigit():
            QMessageBox.warning(None, "Erro", "Valor Invalido! Digite apenas números")
            return
        
        if float(valor_sangria) > self.total_vendas_dia:
            QMessageBox.warning(None, "error", "Quantidade maior que o caixa do dia!")
            return

        if (self.total_vendas_dia - float(valor_sangria)) < 100 :
            QMessageBox.warning(None, "error", "Precisa sobrar no mínimo R$100 de caixa!")
            return
        
        if obs_sangria and not obs_sangria.replace(" ", "").isalpha():
            QMessageBox.warning(None, "Erro", "Apenas letras na observação!")
            return
    
        cursor = self.conexao.get_cursor()
        comando = "select perm from usuarios where id_usuario = %s"
        cursor.execute(comando, (vendedor_resp, ))
        permisao = cursor.fetchone()[0]

        if permisao == "0":
            QMessageBox.warning(None, "error", "Usuario não tem permissão para fazer uma sangria! Chame um supervisor")
            return
        
        senha, ok = QInputDialog.getText(
            None,
            "Confirmação de Remoção",
            "Digite a senha para remover o item:",
            echo=QLineEdit.Password  # Correção: Usa QLineEdit.Password
        )
        
        if not ok or not senha:
            QMessageBox.warning(None, "Erro", "Senha não fornecida!")
            return

        comando = "SELECT senha FROM usuarios WHERE id_usuario = %s"
        cursor.execute(comando, (vendedor_resp,))
        senha_armazenada = cursor.fetchone()

        comando_senha = "SELECT SHA2(%s, 256)"
        cursor.execute(comando_senha, (senha,))
        resultado_senha = cursor.fetchone()
        
        senha_digitada_hash = resultado_senha[0]

        if senha_digitada_hash != senha_armazenada:
            QMessageBox.warning(None, "Erro", "Senha inválida!")
            return
        comando = "select valor_sangria where id_user = %s and status = 1"
        cursor.execute(comando, (self.id_user,))
        valor_atual_sangria = cursor.fetchone()[0]

        if valor_atual_sangria is None or valor_atual_sangria == "0":
            valor_atual_sangria = 0

        novo_valor = float(valor_atual_sangria) + valor_sangria

        comando = "update caixa set valor_sangria = %s where id_user = %s and status = 1"
        valores = (novo_valor, self.id_user)
        cursor.execute(comando, valores)
        self.conexao.commit()
        
        comando = "select saldo_atual from caixa where id_user = %s and and status = 1"
        valores = (self.id_user, self.hoje)
        cursor.execute(comando, (self.id_user,))
        self.total_vendas_dia = cursor.fetchone()[0]
        cursor.close()

        self.total_vendas_dia -= valor_sangria
        self.tela_principal.stackedWidget_7.setCurrentIndex(0)

    def registrar_suprimento(self):
        valor_suprimeto = self.tela_principal.input_valor_suprimento.text()
        vendedor_resp = self.tela_principal.input_vendedor_responsavel_suprimento.text()
        obs_suprimento = self.tela_principal.input_obs_suprimento.text()

        if float(valor_suprimeto) <= 0:
            QMessageBox.warning(None, "error", "Suprimento Precisa ser maior que R$0,00")
            return
        
        if obs_suprimento and not obs_suprimento.replace(" ", "").isalpha():
            QMessageBox.warning(None, "Erro", "Apenas letras na observação!")
            return
        
        cursor = self.conexao.get_cursor()
        comando = "select perm from usuarios where id_usuario = %s"
        cursor.execute(comando, (vendedor_resp, ))
        permisao = cursor.fetchone()[0]

        if permisao == "0":
            QMessageBox.warning(None, "error", "Usuario não tem permissão para fazer um Suprimento! Chame um supervisor")
            return
        
        senha, ok = QInputDialog.getText(
            None,
            "Confirmação de Remoção",
            "Digite a senha para remover o item:",
            echo=QLineEdit.Password  
        )
        
        if not ok or not senha:
            QMessageBox.warning(None, "Erro", "Senha não fornecida!")
            return
        
        comando = "SELECT senha FROM usuarios WHERE id_usuario = %s"
        cursor.execute(comando, (vendedor_resp,))
        senha_armazenada = cursor.fetchone()

        comando_senha = "SELECT SHA2(%s, 256)"
        cursor.execute(comando_senha, (senha,))
        resultado_senha = cursor.fetchone()
        
        senha_digitada_hash = resultado_senha[0]

        if senha_digitada_hash != senha_armazenada:
            QMessageBox.warning(None, "Erro", "Senha inválida!")
            return
        comando = "select valor_suprimento from caixa where id_user = %s and status = 1"
        cursor.execute(comando, (self.id_user,))
        valor_atual_suprimento = cursor.fetchone()[0]

        if valor_atual_suprimento is None or valor_atual_suprimento == "0":
            valor_atual_suprimento = 0

        novo_valor = float(valor_atual_suprimento) + valor_suprimeto

        comando = "update caixa set valor_suprimento = %s where id_user = %s and status = 1"
        valores = (novo_valor, self.id_user)
        cursor.execute(comando, valores)
        self.conexao.commit()

        cursor = self.conexao.get_cursor()
        comando = "select saldo_atual from caixa where id_user = %s and status = 1"
        cursor.execute(comando, (self.id_user,))
        self.total_vendas_dia = cursor.fetchone()[0]
        cursor.close()

        self.total_vendas_dia += valor_suprimeto
        self.tela_principal.stackedWidget_7.setCurrentIndex(0)

    def fechar_caixa(self):
        quant_final = self.tela_principal.input_quantidade_caixa_fechar.text()
        hoje = datetime.date.today()

        cursor = self.conexao.get_cursor()
        comando = "SELECT data_abertura FROM caixa WHERE id_user = %s ORDER BY data_abertura DESC LIMIT 1"
        cursor.execute(comando, (self.id_user,))
        data_abertura = cursor.fetchone()[0]

        comando = "select saldo_atual from caixa where id_user = %s and where status = '1'"
        valores = (self.id_user)
        cursor.execute(comando, valores)
        self.total_vendas_dia = cursor.fetchone()[0]

        if float(quant_final) < float(self.total_vendas_dia):
            QMessageBox.warning(None, "error", "Quantidade Menor que Total no Caixa!")
            return
        
        elif float(quant_final) > float(self.total_vendas_dia):
            QMessageBox.warning(None, "error", "Quantidade Menor que Total no Caixa!")
            return
        
        comando = "update caixa set saldo_final = %s, status = '0', data_fechar = %s where id_user = %s and status = 1"
        valores = (quant_final, hoje, self.id_user)
        cursor.execute(comando, valores)
        self.conexao.commit()
        QMessageBox.information(None, "Sucesso", "Caixa Fechado!")  
        self.tela_principal.stackedWidget_7.setCurrentIndex(0)
