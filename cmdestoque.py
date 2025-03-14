from conexao_db import conexaoDB
from PySide6.QtWidgets import QTreeWidgetItem, QMessageBox, QFileDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
import os
import shutil

class cmdEstoque():
    def __init__(self, tela_principal):
        self.tela_principal = tela_principal
        self.tela_principal.input_categoria_produto.currentTextChanged.connect(self.categoria)
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
            if categoria == "HortiFruti":
                item.setText(2, f"R$ {str(preco)} KG")
            else:
                item.setText(2, f"R$ {str(preco)} UN.")  
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
        self.tela_principal.input_nome_produto.setText("")
        self.tela_principal.input_categoria_produto.setCurrentIndex(-1)
        self.tela_principal.input_quantidade_produto.setText("")
        self.tela_principal.input_preco_produto.setText("")
        pixmap = QPixmap()
        self.tela_principal.img_produto_estoque.setPixmap(pixmap)
        self.tela_principal.stackedWidget_3.setCurrentIndex(1)
        self.tela_principal.input_categoria_produto.setCurrentIndex(-1) 

    def carregar_categorias(self):
        cursor = self.conexao.get_cursor()
        comando = "SELECT id_categorias, nome_categoria FROM categorias ORDER BY id_categorias"
        cursor.execute(comando)
        categorias = cursor.fetchall()
            
        self.tela_principal.input_categoria_produto.clear()
            
        for id_cat, nome_cat in categorias:
            self.tela_principal.input_categoria_produto.addItem(nome_cat, id_cat)  
            
        self.tela_principal.input_categoria_produto.setCurrentIndex(-1) 
            
        cursor.close()

    def adc_produto_estoque(self):
        self.nome = self.tela_principal.input_nome_produto.text()

        if not self.nome:
            QMessageBox.warning(None, "Erro", "Digite o nome do produto!")
            return
        
        cursor = self.conexao.get_cursor()
        comando = "SELECT nome_produto FROM estoque where nome_produto = %s"
        cursor.execute(comando, (self.nome, ))
        resultado = cursor.fetchone()

        if resultado == None:
            self.nome = self.tela_principal.input_nome_produto.text()
        else:
            QMessageBox.warning(None, "Erro", f"Produto com nome '{self.nome}' já cadastrado!")
            cursor.close()
            return

        categoria_index = self.tela_principal.input_categoria_produto.currentIndex() + 1
        if not categoria_index:   
            QMessageBox.warning(None, "Erro", "Selecione uma categoria!")
            return

        preco = self.tela_principal.input_preco_produto.text()
        if not preco or float(preco) <= 0:
            QMessageBox.warning(None, "Erro", "Digite um valor válido!")
            return

        quant = self.tela_principal.input_quantidade_produto.text()
        if not quant or int(quant) <= 0:
            QMessageBox.warning(None, "Erro", "Digite uma quantidade válida!")
            return



        comando = "SELECT id_categorias FROM categorias WHERE id_categorias = %s"
        cursor.execute(comando, (categoria_index,)) 
        resultado = cursor.fetchone()
        if not resultado:
            QMessageBox.warning(None, "Erro", "Categoria não encontrada!")
            return
        categoria_id = resultado[0] 

        relative_path = os.path.relpath(self.new_file_path, os.getcwd()).replace("\\", "/")
        query = "INSERT INTO estoque (nome_produto, preco, quantidade, categoria, imagem) VALUES (%s, %s, %s, %s, %s)"
        valores = (self.nome, preco, quant, categoria_id, relative_path)
        cursor.execute(query, valores)
        self.conexao.commit()

        QMessageBox.information(None, "Sucesso", "Produto adicionado com sucesso!")

        cursor.close()
        self.mostrar_estoque()
        self.tela_principal.stackedWidget_3.setCurrentIndex(0)

    def open_image(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(None, "Open Image", "", "Images(*.png *.xpm *.jpg *.jpeg *.bmp);;All Files (*)")

        if file_path:
            # Define the destination directory
            save_dir = "imgs/foto_produtos"  # Corrected to a single, intended directory
            
            # Create the directory if it doesn’t exist
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)
            
            # Get the original filename
            original_filename = os.path.basename(file_path)
           
            # Define the new file path using only save_dir
            self.new_file_path = os.path.join(save_dir, original_filename)
            print(f"Copying from {file_path} to {self.new_file_path}")  # Debug print
                
            # Copy the image
            shutil.copy(file_path, self.new_file_path)

            # Display the image in the UI using absolute path for reliability
            absolute_path = os.path.abspath(self.new_file_path)
            pixmap = QPixmap(absolute_path)
            self.tela_principal.img_produto_estoque.setPixmap(pixmap)
            self.tela_principal.img_produto_estoque.setScaledContents(True)

    def categoria(self):
        if self.tela_principal.input_categoria_produto.currentText() == "HortiFruti" or self.tela_principal.input_categoria_produto.currentText() == "Fruta":
            self.tela_principal.txt_preco_estoque.setText("Valor do KG")
            self.tela_principal.input_preco_produto.setPlaceholderText("KG")