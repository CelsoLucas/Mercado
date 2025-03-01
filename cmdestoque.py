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
        cursor.execute("select id_produto, nome_produto, preco, quantidade, categorias.nome_categoria, imagem from estoque join categorias on estoque.categoria = categorias.id_categorias")
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
        cursor.execute("select id_produto, nome_produto, preco, quantidade, categorias.nome_categoria, imagem from estoque join categorias on estoque.categoria = categorias.id_categorias where nome_produto = %s or id_produto = %s", valores)

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
    
    def tela_adc_produto(self):
        self.tela_principal.stackedWidget_3.setCurrentIndex(1)
        self.tela_principal.input_categoria_produto.setCurrentIndex(-1)  # Remove a seleção inicial

    def carregar_categorias(self):
        cursor = self.conexao.get_cursor()
        try:
            # Buscar todas as categorias
            comando = "SELECT id_categorias, nome_categoria FROM categorias ORDER BY id_categorias"
            cursor.execute(comando)
            categorias = cursor.fetchall()
            
            # Limpar combobox antes de adicionar
            self.input_categoria_produto.clear()
            
            # Adicionar categorias ao combobox
            for id_cat, nome_cat in categorias:
                self.input_categoria_produto.addItem(nome_cat, id_cat)  # Texto visível e dado associado
            
            # Opcional: definir um item padrão
            self.input_categoria_produto.setCurrentIndex(-1)  # Nenhum selecionado por padrão
            
        except Exception as e:
            QMessageBox.warning(None, "Erro", f"Erro ao carregar categorias: {e}")
        finally:
            cursor.close()

    def adc_produto_estoque(self, input_nome_produto, input_preco_produto, input_quantidade_produto, input_categoria_produto):
        cursor = self.conexao.get_cursor()
        try:
            comando = "SELECT nome_produto FROM estoque"
            cursor.execute(comando)
            resultado = cursor.fetchall()

            self.nome = input_nome_produto.text()
            if not self.nome:
                QMessageBox.warning(None, "Erro", "Digite o nome do produto!")
                return
            if any(row[0] == self.nome for row in resultado):
                QMessageBox.warning(None, "Erro", "Produto já cadastrado!")
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

            # Ensure self.new_file_path is relative to the project root
            relative_path = os.path.relpath(self.new_file_path, os.getcwd()).replace("\\", "/")
            query = "INSERT INTO estoque (nome_produto, preco, quantidade, categoria, imagem) VALUES (%s, %s, %s, %s, %s)"
            valores = (self.nome, preco, quant, categoria_id, relative_path)
            cursor.execute(query, valores)
            self.conexao.commit()

            QMessageBox.information(None, "Sucesso", "Produto adicionado com sucesso!")

        except Exception as e:
            QMessageBox.warning(None, "error", f"{e}")            
            raise
        finally:
            cursor.close()
            self.mostrar_estoque()
            self.tela_principal.stackedWidget_3.setCurrentIndex(0)

    def open_image(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(None, "Open Image", "", "Images(*.png *.xpm *.jpg *.jpeg *.bmp);;All Files (*)")

        if file_path:
            # Define the destination directory
            save_dir = "imgs/foto_produtos"  # Corrected to a single, intended directory
            
            try:
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
                if pixmap.isNull():
                    raise ValueError(f"Failed to load image at {absolute_path}")
                self.tela_principal.img_produto_adc_estoque.setPixmap(pixmap)
                self.tela_principal.img_produto_adc_estoque.setScaledContents(True)

            except Exception as e:
                QMessageBox.warning(None, "error", f"{e}")
                raise