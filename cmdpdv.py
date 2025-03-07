from conexao_db import conexaoDB
from PySide6.QtWidgets import QFrame, QVBoxLayout, QLabel, QHBoxLayout, QWidget, QPushButton, QScrollArea, QGridLayout, QMessageBox
from PySide6.QtGui import QIntValidator
from PySide6.QtCore import Qt, QSize

class cmdPdv():
    def __init__(self, btn_pesquisar_produto, input_pesquisar_produto, txt_caso_nao_produto_encontrado, stackedWidget_2, txt_quantidade, txt_nome_preco_produto, tela_pincipal, txt_nome_produto_1, txt_quantidade_1, txt_valor_1, txt_total_pagar, input_forma_pagamento, input_quantia_dinheiro):
        self.btn_pesquisar_produto = btn_pesquisar_produto
        self.input_pesquisar_produto = input_pesquisar_produto
        self.txt_caso_nao_produto_encontrado = txt_caso_nao_produto_encontrado
        self.stackedWidget_2 = stackedWidget_2
        self.txt_quantidade = txt_quantidade
        self.txt_nome_preco_produto = txt_nome_preco_produto
        self.txt_nome_produto_1 = txt_nome_produto_1
        self.txt_quantidade_1 = txt_quantidade_1
        self.txt_valor_1 = txt_valor_1
        self.tela_principal = tela_pincipal
        self.txt_nome_produto_1 = txt_nome_produto_1
        self.txt_total_pagar = txt_total_pagar
        self.input_forma_pagamento = input_forma_pagamento
        self.input_quantia_dinheiro = input_quantia_dinheiro
        self.input_quantia_dinheiro.setVisible(False)
        self.nome1 = ""
        self.preco1 = ""
        self.quantidade1 = ""
        self.conexao = conexaoDB()
        self.tot = 0
        self.carrinho = []
        self.carregar_formapagamento()
        self.input_forma_pagamento.currentTextChanged.connect(self.atualizar_visibilidade_quantia)  # Conexão do sinal

    def procurar_produto(self):

        if self.tela_principal.stackedWidget_2.currentIndex() == 0:
            self.resultado_busca_produto = self.tela_principal.input_pesquisar_produto.text()
        elif self.tela_principal.stackedWidget_2.currentIndex() == 1:
            self.resultado_busca_produto = self.tela_principal.input_pesquisar_produto_2.text()
        elif self.tela_principal.stackedWidget_2.currentIndex() == 2:
            self.resultado_busca_produto = self.tela_principal.input_pesquisar_produto_3.text()
        
        if not self.resultado_busca_produto:
            if self.tela_principal.stackedWidget_2.currentIndex() == 0:
                self.tela_principal.txt_caso_nao_produto_encontrado.setText("Digite um produto para buscar.")
            elif self.tela_principal.stackedWidget_2.currentIndex() == 1:
                self.tela_principal.txt_caso_nao_produto_encontrado2.setText("Digite um produto para buscar.")
            elif self.tela_principal.stackedWidget_2.currentIndex() == 2:
                self.tela_principal.txt_caso_nao_produto_encontrado3.setText("Digite um produto para buscar.")

            return

        cursor = self.conexao.get_cursor()

        valores = (self.resultado_busca_produto, self.resultado_busca_produto)
        cursor.execute("SELECT nome_produto, preco, quantidade FROM estoque WHERE nome_produto = %s OR id_produto = %s", valores)

        resultado = cursor.fetchone()

        if resultado is None:
            self.tela_principal.txt_caso_nao_produto_encontrado.setText("Produto não encontrado!")
        else:
            self.nome, self.preco, self.quantidade = resultado
            self.tela_principal.stackedWidget_2.setCurrentIndex(1)
            self.tela_principal.txt_nome_preco_produto.setText(f"{self.nome} R${self.preco:.2f}")
            self.tela_principal.txt_quantidade.setText("1")
            
        cursor.close()
    
    def menos(self):
        quantidade = int(self.txt_quantidade.text())

        if quantidade <= 1:
            QMessageBox.warning(None, "Erro", f"Quantidade Minima é 1")
            self.tela_principal.txt_quantidade.setText("1")
        else:
            quantidade -= 1
            self.txt_quantidade.setText(f"{quantidade}")

    def mais(self):
        quantidade = int(self.txt_quantidade.text())

        if quantidade >= self.quantidade:
            QMessageBox.warning(None, "Erro", f"Quantidade Indisponivel no Estoque, Você pode pedir no maximo {self.quantidade}")
        else:
            quantidade += 1
            self.txt_quantidade.setText(f"{quantidade}")

    def adc_carrinho(self):
        self.suporte_carrinho = []
        self.carrinho.append(self.suporte_carrinho)
        self.suporte_carrinho.append(self.nome)
        self.suporte_carrinho.append(self.preco)
        quantidade = self.txt_quantidade.text()
        self.suporte_carrinho.append(quantidade)
        print(self.carrinho)
        self.stackedWidget_2.setCurrentIndex(2)
        self.mostrar_carrinho()

    def mostrar_carrinho(self):
        self.nome1 = ""
        self.quantidade1 = ""
        self.valor1 = ""
        self.tot = 0.0 

        for item in self.carrinho:
            nome = str(item[0])              # Nome do produto
            preco = float(item[1])           # Preço como float
            quantidade = int(item[2])        # Quantidade como inteiro
            valor_item = preco * quantidade  # Calcula valor total

            self.nome1 += nome + "\n"
            self.quantidade1 += str(quantidade) + "\n"
            self.valor1 += f"R${valor_item:.2f}\n"
            self.tot += valor_item


        if self.nome1:
            self.nome1 = self.nome1.rstrip("\n")
            self.quantidade1 = self.quantidade1.rstrip("\n")
            self.valor1 = self.valor1.rstrip("\n")

        self.txt_nome_produto_1.setText(self.nome1)
        self.txt_quantidade_1.setText(self.quantidade1)
        self.txt_valor_1.setText(self.valor1)
        self.txt_total_pagar.setText(f"Total R${self.tot:.2f}")
        if self.input_forma_pagamento.currentText() == "Dinheiro":
            self.input_quantia_dinheiro.setVisible(True)

    def carregar_formapagamento(self):
        cursor = self.conexao.get_cursor()
            # Buscar todas as categorias
        comando = "SELECT id_forma_pagamento, forma_pagamento FROM formapagamento ORDER BY id_forma_pagamento"
        cursor.execute(comando)
        formapagamento = cursor.fetchall()
            
        self.input_forma_pagamento.clear()
            
        for id_cat, nome_cat in formapagamento:
            self.input_forma_pagamento.addItem(nome_cat, id_cat)  # Texto visível e dado associado
            
        self.input_forma_pagamento.setCurrentIndex(-1) 
            
        cursor.close()

    def atualizar_visibilidade_quantia(self):
        if self.input_forma_pagamento.currentText() == "Dinheiro":
            self.input_quantia_dinheiro.setVisible(True)
        else:
            self.input_quantia_dinheiro.setVisible(False)

    def validar_compra(self):
        self.atualizar_visibilidade_quantia()  # Garante que o input esteja visível se "Dinheiro" for selecionado
        if self.input_forma_pagamento.currentText() == "Dinheiro":
            quant_dinheiro = float(self.input_quantia_dinheiro.text()) if self.input_quantia_dinheiro.text() else 0.0
            if quant_dinheiro < self.tot:
                QMessageBox.warning(None, "Erro", "Quantidade de Dinheiro Insuficiente!")
                return
            elif quant_dinheiro == self.tot:
                QMessageBox.information(None, "Sucesso", "Obrigado por comprar no Mercado do Celso!")

            else:
                QMessageBox.information(None, "Sucesso", f"Obrigado por comprar no Mercado do Celso! Seu Troco é R${(quant_dinheiro - self.tot):.2f}")
        else:
            QMessageBox.information(None, "Sucesso", "Obrigado por comprar no Mercado do Celso!")
        self.input_pesquisar_produto.setText("")
        self.txt_quantidade.setText("")
        self.input_quantia_dinheiro.setText("")
        self.input_forma_pagamento.setCurrentIndex(-1)
        self.txt_nome_produto_1.setText("")
        self.txt_quantidade_1.setText("")
        self.txt_valor_1.setText("")
        self.txt_total_pagar.setText("Total R$0.00")
        self.carrinho = []
        self.tot = 0.0
        self.stackedWidget_2.setCurrentIndex(0)