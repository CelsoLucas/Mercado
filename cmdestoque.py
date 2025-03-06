from conexao_db import conexaoDB
from PySide6.QtWidgets import QTreeWidgetItem, QMessageBox, QFileDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
import os
import shutil

class cmdEstoque():
    def __init__(self, tela_principal, input_pesquisar_produto_4, txt_caso_produto_nao_encontra_estoque, treeview, input_nome_produto, input_categoria_produto):
        self.tela_principal = tela_principal
        self.input_pesquisar_produto_4 = input_pesquisar_produto_4
        self.txt_caso_produto_nao_encontra_estoque = txt_caso_produto_nao_encontra_estoque
        self.nome = input_nome_produto.text()
        self.treeview = treeview
        self.input_categoria_produto = input_categoria_produto
        self.conexao = conexaoDB()
        self.mostrar_estoque()
        self.carregar_categorias()

    def mostrar_estoque(self):
        cursor = self.conexao.get_cursor()
        cursor.execute("select id_produto, nome_produto, preco, quantidade, categorias.nome_categoria from estoque join categorias on estoque.categoria = categorias.id_categorias")
        resultado = cursor.fetchall()

        tree = self.tela_principal.treeWidget
        tree.clear()

        for i in resultado:
            id, nome, preco, quantidade, categoria = i
            item = QTreeWidgetItem(tree)
            item.setText(0, str(id))  
            item.setText(1, nome)  
            item.setText(2, str(preco))  
            item.setText(3, str(quantidade))  
            item.setText(4, str(categoria))

            item.setTextAlignment(0, Qt.AlignCenter)
            item.setTextAlignment(1, Qt.AlignCenter)
            item.setTextAlignment(2, Qt.AlignCenter)
            item.setTextAlignment(3, Qt.AlignCenter)
            item.setTextAlignment(4, Qt.AlignCenter)

            tree.addTopLevelItem(item)

        cursor.close()

    def procurar_produto(self):

        self.resultado_busca_produto = self.tela_principal.input_pesquisar_produto_4.text()
        
        if not self.resultado_busca_produto:
            self.tela_principal.txt_caso_produto_nao_encontra_estoque.setText("Digite um produto para buscar.")
            return

        cursor = self.conexao.get_cursor()

        valores = (self.resultado_busca_produto, self.resultado_busca_produto)
        cursor.execute("select id_produto, nome_produto, preco, quantidade, categorias.nome_categoria from estoque join categorias on estoque.categoria = categorias.id_categorias where nome_produto = %s or id_produto = %s", valores)

        resultado = cursor.fetchone()

        tree = self.tela_principal.treeWidget
        tree.clear()

        if not resultado:
            self.tela_principal.txt_caso_produto_nao_encontra_estoque.setText("Produto não encontrado!")
        else:
            id, nome, preco, quantidade, categoria, imagem = resultado                
            item = QTreeWidgetItem(tree)
            item.setText(0, str(id))  
            item.setText(1, nome)  
            item.setText(2, str(preco))  
            item.setText(3, str(quantidade))  
            item.setText(4, str(categoria))

            item.setTextAlignment(0, Qt.AlignCenter)
            item.setTextAlignment(1, Qt.AlignCenter)
            item.setTextAlignment(2, Qt.AlignCenter)
            item.setTextAlignment(3, Qt.AlignCenter)
            item.setTextAlignment(4, Qt.AlignCenter)
            tree.addTopLevelItem(item)

        cursor.close()
    
    def tela_adc_produto(self):
        self.tela_principal.stackedWidget_3.setCurrentIndex(1)
        self.tela_principal.input_categoria_produto.setCurrentIndex(-1)  # Remove a seleção inicial

    def carregar_categorias(self):
        cursor = self.conexao.get_cursor()
            # Buscar todas as categorias
        comando = "SELECT id_categorias, nome_categoria FROM categorias ORDER BY id_categorias"
        cursor.execute(comando)
        categorias = cursor.fetchall()
            
        self.input_categoria_produto.clear()
            
        for id_cat, nome_cat in categorias:
            self.input_categoria_produto.addItem(nome_cat, id_cat)  # Texto visível e dado associado
            
        self.input_categoria_produto.setCurrentIndex(-1) 
            
        cursor.close()

    def adc_produto_estoque(self, input_nome_produto, input_preco_produto, input_quantidade_produto, input_categoria_produto):
        self.nome = input_nome_produto.text()
        if not self.nome:
            QMessageBox.warning(None, "Erro", "Digite o nome do produto!")
            return
        cursor = self.conexao.get_cursor()
        comando = "SELECT nome_produto FROM estoque where nome_produto = %s"
        cursor.execute(comando, (self.nome, ))
        resultado = cursor.fetchone()
        print(resultado)
        if self.nome in resultado:
            QMessageBox.warning(None, "Erro", f"Produto com nome '{self.nome}' já cadastrado!")
            return

        preco = input_preco_produto.text()
        if not preco:
            QMessageBox.warning(None, "Erro", "Digite um valor válido!")
            return

        quant = input_quantidade_produto.text()
        if not quant:
            QMessageBox.warning(None, "Erro", "Digite uma quantidade válida!")
            return

        categoria_index = input_categoria_produto.currentIndex() + 1
        if not categoria_index:   # Verifica se é 0, o que é incorreto aqui
            QMessageBox.warning(None, "Erro", "Selecione uma categoria!")
            return

        print(categoria_index)
        comando = "SELECT id_categorias FROM categorias WHERE id_categorias = %s"
        cursor.execute(comando, (categoria_index,))  # Passa um número, não o texto
        resultado = cursor.fetchone()
        if not resultado:
            QMessageBox.warning(None, "Erro", "Categoria não encontrada!")
            return
        categoria_id = resultado[0] 


        query = "INSERT INTO estoque (nome_produto, preco, quantidade, categoria) VALUES (%s, %s, %s, %s)"
        valores = (self.nome, preco, quant, categoria_id)
        cursor.execute(query, valores)
        self.conexao.commit()

        QMessageBox.information(None, "Sucesso", "Produto adicionado com sucesso!")

        cursor.close()
        self.mostrar_estoque()
        self.tela_principal.stackedWidget_3.setCurrentIndex(0)

    