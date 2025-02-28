from conexao_db import conexaoDB
from PySide6.QtWidgets import QTreeWidgetItem
from PySide6.QtCore import Qt

class cmdEstoque():
    def __init__(self, tela_principal, input_pesquisar_produto_4, txt_caso_produto_nao_encontra_estoque, treeview):
        self.tela_principal = tela_principal
        self.input_pesquisar_produto_4 = input_pesquisar_produto_4
        self.txt_caso_produto_nao_encontra_estoque = txt_caso_produto_nao_encontra_estoque
        self.treeview = treeview
        self.conexao = conexaoDB()
        self.mostrar_estoque()

    def mostrar_estoque(self):
        cursor = self.conexao.get_cursor()
        cursor.execute("select id_estoque, nome, preco, quantidade, categorias.categoria, imagem from estoque join categorias on estoque.categoria = categorias.id_categoria")
        resultado = cursor.fetchall()

        tree = self.tela_principal.treeWidget
        tree.clear()

        for i in resultado:
            id, nome, preco, quantidade, categoria, imagem = i
            item = QTreeWidgetItem(tree)
            item.setText(0, str(id))  
            item.setText(1, nome)  
            item.setText(2, str(preco))  
            item.setText(3, str(quantidade))  
            item.setText(4, str(categoria))
            item.setText(5, str(imagem))

            item.setTextAlignment(0, Qt.AlignCenter)
            item.setTextAlignment(1, Qt.AlignCenter)
            item.setTextAlignment(2, Qt.AlignCenter)
            item.setTextAlignment(3, Qt.AlignCenter)
            item.setTextAlignment(4, Qt.AlignCenter)
            item.setTextAlignment(5, Qt.AlignCenter) 

            tree.addTopLevelItem(item)

        cursor.close()

    def procurar_produto(self):

        self.resultado_busca_produto = self.tela_principal.input_pesquisar_produto_4.text()
        
        if not self.resultado_busca_produto:
            self.tela_principal.txt_caso_produto_nao_encontra_estoque.setText("Digite um produto para buscar.")
            return

        cursor = self.conexao.get_cursor()

        valores = (self.resultado_busca_produto, self.resultado_busca_produto)
        cursor.execute("select id_estoque, nome, preco, quantidade, categorias.categoria, imagem from estoque join categorias on estoque.categoria = categorias.id_categoria where nome = %s or id_estoque = %s", valores)

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
            item.setText(5, str(imagem))

            item.setTextAlignment(0, Qt.AlignCenter)
            item.setTextAlignment(1, Qt.AlignCenter)
            item.setTextAlignment(2, Qt.AlignCenter)
            item.setTextAlignment(3, Qt.AlignCenter)
            item.setTextAlignment(4, Qt.AlignCenter)
            item.setTextAlignment(5, Qt.AlignCenter)
            tree.addTopLevelItem(item)

        cursor.close()