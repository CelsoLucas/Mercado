from PySide6.QtWidgets import QMessageBox, QInputDialog, QLineEdit, QTreeWidgetItem
from PySide6.QtCore import Qt
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
        self.dados()


    def dados(self):
        #primeira parte
        hoje = datetime.date.today()
        self.tela_principal.txt_data.setText(f"Data: {hoje}")
        self.tela_principal.txt_operador_db.setText(f"Operador: {self.tela_principal.txt_ola_user.text()}")

        #segunda parte
        #lado esquerdo =-=-=-=-=-=-=-=-=
        cursor = self.conexao.get_cursor()
        comando = "select sum(valor_total) from vendas where id_usuario = %s and data_venda = %s"
        valores = (self.id_user, hoje)
        cursor.execute(comando, valores)
        resultado = cursor.fetchone()
        if resultado is None or resultado[0] is None:            
            vendas_total = 0
        else:
            vendas_total = resultado[0]
        print(vendas_total)
        self.tela_principal.txt_total_vendas_db.setText(f"Total de Vendas: R$ {float(vendas_total):.2f}")

        comando = "select sum(valor_total) from vendas where id_usuario = %s and data_venda = %s and id_forma_pagamento = 1"
        valores = (self.id_user, hoje)
        cursor.execute(comando, valores)
        resultado = cursor.fetchone()
        if resultado is None or resultado[0] is None:
            vendas_pix = 0
        else:
            vendas_pix = resultado[0]
        self.tela_principal.txt_total_vendas_pix_db.setText(f"R$ {float(vendas_pix):.2f}")

        
        comando = "select sum(valor_total) from vendas where id_usuario = %s and data_venda = %s and id_forma_pagamento = 2"
        valores = (self.id_user, hoje)
        cursor.execute(comando, valores)
        resultado = cursor.fetchone()
        if resultado is None or resultado[0] is None:
            vendas_debito = 0
        else:
            vendas_debito = resultado[0]
        self.tela_principal.txt_total_vendas_debito_db.setText(f"R$ {float(vendas_debito):.2f}")

        
        comando = "select sum(valor_total) from vendas where id_usuario = %s and data_venda = %s and id_forma_pagamento = 3"
        valores = (self.id_user, hoje)
        cursor.execute(comando, valores)
        resultado = cursor.fetchone()
        if resultado is None or resultado[0] is None:
            vendas_credito = 0
        else:
            vendas_credito = resultado[0]
        self.tela_principal.txt_total_vendas_credito_db.setText(f"R$ {float(vendas_credito):.2f}")

        
        comando = "select sum(valor_total) from vendas where id_usuario = %s and data_venda = %s and id_forma_pagamento = 4"
        valores = (self.id_user, hoje)
        cursor.execute(comando, valores)
        resultado = cursor.fetchone()
        if resultado is None or resultado[0] is None:
            vendas_dinheiro = 0
        else:
            vendas_dinheiro = resultado[0]
        self.tela_principal.txt_total_venda_dinheiro_db.setText(f"R$ {float(vendas_dinheiro):.2f}")

        #lado direito =-=-=-=-=-=-=-=-=
        comando = "select sum(saldo_atual) from caixa"
        cursor.execute(comando)
        resultado = cursor.fetchone()
        if resultado is None or resultado[0] is None:
            total_gaveta = 0
        else:
            total_gaveta = resultado[0]
        self.tela_principal.txt_total_gaveta_db.setText(f"Total em Gaveta: R$ {float(total_gaveta):.2f}")

        comando = "select saldo_ini from caixa where id_user = %s and status = '1'"
        cursor.execute(comando, (self.id_user,))
        resultado = cursor.fetchone()
        if resultado is None or resultado[0] is None:
            saldo_ini = 0
        else:
            saldo_ini = resultado[0]
        self.tela_principal.txt_saldo_inicial_db.setText(f"R$ {float(saldo_ini):.2f}")

        comando = "select sum(valor_total) from vendas where id_forma_pagamento = '4' and data_venda = %s"
        cursor.execute(comando, (hoje,))
        resultado = cursor.fetchone()
        if resultado is None or resultado[0] is None:
            saldo_atual = 0
        else:
            saldo_atual = resultado[0]
        self.tela_principal.txt_vendas_dinheiro_db.setText(f"R$ {float(saldo_atual):.2f}")

        comando = "select valor_suprimento from caixa where id_user = %s and status = '1'"
        cursor.execute(comando, (self.id_user,))
        resultado = cursor.fetchone()
        if resultado is None or resultado[0] is None:
            valor_suprimento = 0
        else:
            valor_suprimento = resultado[0]
        self.tela_principal.txt_suprimento_db.setText(f"R$ {float(valor_suprimento):.2f}")

        comando = "select valor_sangria from caixa where id_user = %s and status = '1'"
        cursor.execute(comando, (self.id_user,))
        resultado = cursor.fetchone()
        if resultado is None or resultado[0] is None:
            valor_sangria = 0
        else:
            valor_sangria = resultado[0]
        self.tela_principal.txt_total_sangria_db.setText(f"R$ {float(valor_sangria):.2f}")

        #Tabela =-=-=-=-=-=-=-=-=-=-=-=-=
        data_hora = datetime.date.today()

        comando = "select * from mov_caixa where data_hora = %s and id_user = %s"
        cursor.execute(comando, (data_hora, self.id_user))
        resultado = cursor.fetchall()
        if resultado is None:
            pass

        tree = self.tela_principal.tabela_hist_mov
        tree.clear()

        for i in resultado:
            id_mov, id_user, data, desc, formapagamento, obs, valor = i
            item = QTreeWidgetItem(tree)
            item.setText(0, str(data))  
            item.setText(1, desc)  
            item.setText(2, str(formapagamento))  
            item.setText(3, str(obs))  
            item.setText(4, str(valor))


            item.setTextAlignment(0, Qt.AlignCenter)
            item.setTextAlignment(1, Qt.AlignCenter)
            item.setTextAlignment(2, Qt.AlignCenter)
            item.setTextAlignment(3, Qt.AlignCenter)
            item.setTextAlignment(4, Qt.AlignCenter)

            tree.addTopLevelItem(item)


        

    def tela_abrir_caixa(self):
        cursor = self.conexao.get_cursor()
        comando = "select id_user from caixa where id_user = %s and status = '1'"
        cursor.execute(comando, (self.id_user,))
        resultado = cursor.fetchone()
        if resultado:
            QMessageBox.warning(None, "error", "Caixa Já Aberto!")
            return
        self.tela_principal.stackedWidget_7.setCurrentIndex(1)
        self.tela_principal.input_quantidade_caixa_abrir.setText("")
    
    def tela_fechar_caixa(self):
        cursor = self.conexao.get_cursor()
        comando = "select id_user from caixa where id_user = %s and status = '0'"
        cursor.execute(comando, (self.id_user,))
        resultado = cursor.fetchone()
        if resultado:
            QMessageBox.warning(None, "error", "Nenhum Caixa Aberto!")
            return
        self.tela_principal.stackedWidget_7.setCurrentIndex(2)
        self.tela_principal.input_quantidade_caixa_fechar.setText("")

    def tela_sangria(self):
        self.tela_principal.stackedWidget_7.setCurrentIndex(3)
        self.tela_principal.input_valor_sangria.setText("")
        self.tela_principal.input_vendedor_responsavel_sangria.setText("")
        self.tela_principal.input_obs_sangria.setText("")

    def tela_suprimento(self):
        self.tela_principal.stackedWidget_7.setCurrentIndex(4)
        self.tela_principal.input_valor_suprimento.setText("")
        self.tela_principal.input_vendedor_responsavel_suprimento.setText("")
        self.tela_principal.input_obs_suprimento.setText("")


    def cancelar_acao(self):
        self.tela_principal.stackedWidget_7.setCurrentIndex(0)

    def abrir_caixa(self):
    
        quant_init = self.tela_principal.input_quantidade_caixa_abrir.text()
        
        self.hoje = datetime.datetime.today()

        cursor = self.conexao.get_cursor()
        comando = "select sum(valor_total) from vendas where data_venda = %s and id_forma_pagamento = 4"
        cursor.execute(comando, (self.hoje, ))
        self.total_vendas_dia = cursor.fetchone()[0]
        if self.total_vendas_dia is None:
            self.total_vendas_dia = 0

        if float(quant_init) < float(self.total_vendas_dia):
            QMessageBox.warning(None, "error", "Quantidade Menor que Total no Caixa!")
            return
        
        comando = "insert into caixa (id_user, saldo_ini, data_abertura, status) values (%s, %s, %s, %s)"
        valores = (self.id_user, quant_init, self.hoje, "1")
        cursor.execute(comando, valores)
        self.conexao.commit()
        QMessageBox.information(None, "Sucesso", "Caixa Aberto!")
        self.dados()
        self.tela_principal.stackedWidget_7.setCurrentIndex(0)

    def registrar_sangria(self):
        valor_sangria = self.tela_principal.input_valor_sangria.text()
        vendedor_resp = self.tela_principal.input_vendedor_responsavel_sangria.text()
        obs_sangria = self.tela_principal.input_obs_sangria.toPlainText()

        if float(valor_sangria) <= 0:
            QMessageBox.warning(None, "Erro", "Sangria precisa ser maior que R$0,00")
            return
        
        if obs_sangria and not obs_sangria.replace(" ", "").isalpha():
            QMessageBox.warning(None, "Erro", "Apenas letras na observação!")
            return
        
        cursor = self.conexao.get_cursor()
            # Verifica permissão do usuário
        comando = "SELECT perm, senha FROM usuarios WHERE id_usuario = %s"
        cursor.execute(comando, (vendedor_resp,))
        resultado = cursor.fetchone()
        if resultado is None:
            QMessageBox.warning(None, "Erro", "Usuário não encontrado! Chame um supervisor")
            return
        permisao, senha_armazenada = resultado

        if permisao == "0":
            QMessageBox.warning(None, "Erro", "Usuário não tem permissão para fazer uma Sangria! Chame um supervisor")
            return
            
            # Solicita a senha
        senha, ok = QInputDialog.getText(
            None,
            "Confirmação de Sangria",
            "Digite a senha para realizar a sangria",
            echo=QLineEdit.Password  
        )
            
        if not ok or not senha:
            QMessageBox.warning(None, "Erro", "Senha não fornecida!")
            return
            
            # Calcula o hash da senha digitada
        comando_senha = "SELECT SHA2(%s, 256)"
        cursor.execute(comando_senha, (senha,))
        senha_digitada_hash = cursor.fetchone()[0]
            
            # Compara diretamente com a senha armazenada (já é um hash)
        if senha_digitada_hash != senha_armazenada:
            QMessageBox.warning(None, "Erro", "Senha inválida!")
            return
            
        comando = "select valor_sangria from caixa where id_user = %s and status = 1"
        cursor.execute(comando, (self.id_user,))
        valor_atual_sangria = cursor.fetchone()[0]

        if valor_atual_sangria is None or valor_atual_sangria == "0":
            valor_atual_sangria = 0

        novo_valor = float(valor_atual_sangria) + float(valor_sangria)

        cursor = self.conexao.get_cursor()
        comando = "select saldo_atual from caixa where id_user = %s and status = 1"
        cursor.execute(comando, (self.id_user,))
        self.total_vendas_dia = cursor.fetchone()[0]
        cursor.close()
        if self.total_vendas_dia is None:
            self.total_vendas_dia = 0

        if self.total_vendas_dia <= 100:
            QMessageBox.warning(None, "error", "Você não pode fazer uma sangria! Quantidade mínima no caixa deve ser R$100")
            return
        
        cursor = self.conexao.get_cursor()
        comando = "update caixa set valor_sangria = %s where id_user = %s and status = 1"
        valores = (novo_valor, self.id_user)
        cursor.execute(comando, valores)
        self.conexao.commit()

        self.total_vendas_dia -= float(valor_sangria)

        cursor = self.conexao.get_cursor()
        comando = "update caixa set saldo_atual = %s where id_user = %s and status = 1"
        valores = (self.total_vendas_dia, self.id_user)
        cursor.execute(comando, valores)
        self.conexao.commit()


        cursor = self.conexao.get_cursor()
        comando = """insert into mov_caixa (descricao, formapagamento, obs, valor)
                    values ('Sangria de Caixa', 'Dinheiro', %s, %s)"""
        valores = (obs_sangria, float(valor_sangria))
        cursor.execute(comando, valores)
        self.conexao.commit()

        QMessageBox.information(None, "Sucesso", "Sangria realizada com sucesso!")
        self.dados()
        self.tela_principal.stackedWidget_7.setCurrentIndex(0)
        cursor.close()

    def registrar_suprimento(self):
        valor_suprimeto = self.tela_principal.input_valor_suprimento.text()
        vendedor_resp = self.tela_principal.input_vendedor_responsavel_suprimento.text()
        obs_suprimento = self.tela_principal.input_obs_suprimento.toPlainText()

        if float(valor_suprimeto) <= 0:
            QMessageBox.warning(None, "Erro", "Suprimento precisa ser maior que R$0,00")
            return
        
        if obs_suprimento and not obs_suprimento.replace(" ", "").isalpha():
            QMessageBox.warning(None, "Erro", "Apenas letras na observação!")
            return
        
        cursor = self.conexao.get_cursor()
            # Verifica permissão do usuário
            
        comando = "SELECT perm, senha FROM usuarios WHERE id_usuario = %s"
        cursor.execute(comando, (vendedor_resp,))
        resultado = cursor.fetchone()
        if resultado is None:
            QMessageBox.warning(None, "Erro", "Usuário não encontrado! Chame um supervisor")
            return
        permisao, senha_armazenada = resultado

        if permisao == "0":
            QMessageBox.warning(None, "Erro", "Usuário não tem permissão para fazer um Suprimento! Chame um supervisor")
            return
            
            # Solicita a senha
        senha, ok = QInputDialog.getText(
            None,
            "Confirmação de Remoção",
            "Digite a senha para realizar o suprimento",
            echo=QLineEdit.Password  
        )
            
        if not ok or not senha:
            QMessageBox.warning(None, "Erro", "Senha não fornecida!")
            return
            
            # Calcula o hash da senha digitada
        comando_senha = "SELECT SHA2(%s, 256)"
        cursor.execute(comando_senha, (senha,))
        senha_digitada_hash = cursor.fetchone()[0]
            
            # Compara diretamente com a senha armazenada (já é um hash)
        if senha_digitada_hash != senha_armazenada:
            QMessageBox.warning(None, "Erro", "Senha inválida!")
            return
            
        comando = "select valor_suprimento from caixa where id_user = %s and status = 1"
        cursor.execute(comando, (self.id_user,))
        valor_atual_suprimento = cursor.fetchone()[0]

        if valor_atual_suprimento is None or valor_atual_suprimento == "0":
            valor_atual_suprimento = 0

        novo_valor = float(valor_atual_suprimento) + float(valor_suprimeto)

        comando = "update caixa set valor_suprimento = %s where id_user = %s and status = 1"
        valores = (novo_valor, self.id_user)
        cursor.execute(comando, valores)
        self.conexao.commit()

        cursor = self.conexao.get_cursor()
        comando = "select saldo_atual from caixa where id_user = %s and status = 1"
        cursor.execute(comando, (self.id_user,))
        self.total_vendas_dia = cursor.fetchone()[0]
        cursor.close()
        if self.total_vendas_dia is None:
            self.total_vendas_dia = 0
        self.total_vendas_dia += float(valor_suprimeto)

        cursor = self.conexao.get_cursor()
        comando = "update caixa set saldo_atual = %s where id_user = %s and status = 1"
        valores = (self.total_vendas_dia, self.id_user)
        cursor.execute(comando, valores)
        self.conexao.commit()


        comando = """insert into mov_caixa (descricao, formapagamento, obs, valor)
                    values ('Suprimento de Caixa', 'Dinheiro', %s, %s)"""
        valores = (obs_suprimento, float(valor_suprimeto))
        cursor.execute(comando, valores)
        self.conexao.commit()

        QMessageBox.information(None, "Sucesso", "Suprimento Realizado com sucesso!")
        self.dados()
        self.tela_principal.stackedWidget_7.setCurrentIndex(0)
        cursor.close()

    def fechar_caixa(self):
        quant_final = self.tela_principal.input_quantidade_caixa_fechar.text()
        hoje = datetime.datetime.today()

        cursor = self.conexao.get_cursor()
        comando = "SELECT data_abertura FROM caixa WHERE id_user = %s ORDER BY data_abertura DESC LIMIT 1"
        cursor.execute(comando, (self.id_user,))
        data_abertura = cursor.fetchone()[0]

        comando = "select saldo_atual from caixa where id_user = %s and status = '1'"
        cursor.execute(comando, (self.id_user,))
        self.total_vendas_dia = cursor.fetchone()[0]
        if self.total_vendas_dia is None:
            self.total_vendas_dia = 0
            
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
        self.dados()
        self.tela_principal.stackedWidget_7.setCurrentIndex(0)
