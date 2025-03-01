from conexao_db import conexaoDB
from PySide6.QtWidgets import QFrame, QVBoxLayout, QLabel, QHBoxLayout, QWidget, QPushButton, QScrollArea, QGridLayout, QMessageBox
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QSize

class cmdPdv():
    def __init__(self, btn_pesquisar_produto, input_pesquisar_produto, txt_caso_nao_produto_encontrado, stackedWidget_2, txt_quantidade, txt_nome_preco_produto, tela_pincipal, txt_nome_produto_1, txt_quantidade_1, txt_valor_1):
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
        self.conexao = conexaoDB()
        self.carrinho = 0

    def procurar_produto(self):

        self.resultado_busca_produto = self.tela_principal.input_pesquisar_produto.text()
        
        if not self.resultado_busca_produto:
            self.tela_principal.txt_caso_nao_produto_encontrado.setText("Digite um produto para buscar.")
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
            self.tela_principal.txt_quantidade.setText("0")
            
        cursor.close()
    
    def menos(self):
        quantidade = int(self.txt_quantidade.text())

        if quantidade == 0:
            QMessageBox.warning(None, "Erro", "Não pode diminuir mais")
        else:
            quantidade -= 1
            self.txt_quantidade.setText(f"{quantidade}")
        self.carrinho.append(self.nome, self.preco, self.quantidade)


    def mais(self):
        quantidade = int(self.txt_quantidade.text())

        if quantidade >= self.quantidade:
            QMessageBox.warning(None, "Erro", "Não pode aumentar mais")
        else:
            quantidade += 1
            self.txt_quantidade.setText(f"{quantidade}")

