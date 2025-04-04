from conexao_db import conexaoDB
from PySide6.QtWidgets import QTreeWidgetItem, QMessageBox, QFileDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
import os
import shutil
import re

class cmdEstoque():
    def __init__(self, tela_principal):
        self.tela_principal = tela_principal
        self.tela_principal.input_tipo_valor.currentTextChanged.connect(self.tipo_valor)
        self.conexao = conexaoDB()
        self.new_file_path = ""
        self.mostrar_estoque()
        self.tela_principal.input_pesquisar_produto_4.textChanged.connect(self.procurar_produto)
        self.carregar_categorias()

    def mostrar_estoque(self):
        cursor = self.conexao.get_cursor()
        cursor.execute("select id_produto, nome_produto, preco, quantidade, categorias.nome_categoria, tipo_valor from estoque join categorias on estoque.categoria = categorias.id_categorias")
        resultado = cursor.fetchall()

        tree = self.tela_principal.treeWidget
        tree.clear()

        for i in resultado:
            id, nome, preco, quantidade, categoria, tipo_valor = i
            item = QTreeWidgetItem(tree)
            item.setText(0, str(id))  
            item.setText(1, nome)  
            if tipo_valor == "1":
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

    def procurar_produto(self, texto=None):
        # Se texto for None, pega o valor do campo de entrada
        if texto is None:
            self.resultado_busca_produto = self.tela_principal.input_pesquisar_produto_4.text()
        else:
            self.resultado_busca_produto = texto

        # Limpa a árvore antes de buscar
        tree = self.tela_principal.treeWidget
        tree.clear()

        cursor = self.conexao.get_cursor()

        if not self.resultado_busca_produto:
            # Query para buscar todos os produtos quando o campo está vazio
            comando = """
                SELECT id_produto, nome_produto, preco, quantidade, categorias.nome_categoria 
                FROM estoque 
                JOIN categorias ON estoque.categoria = categorias.id_categorias
            """
            cursor.execute(comando)
            resultados = cursor.fetchall()
            self.tela_principal.txt_caso_produto_nao_encontra_estoque.setText("")  # Limpa a mensagem
        else:
            # Query ajustada para busca incremental com LIKE
            valores = (f"%{self.resultado_busca_produto}%", f"%{self.resultado_busca_produto}%")
            comando = """
                SELECT id_produto, nome_produto, preco, quantidade, categorias.nome_categoria 
                FROM estoque 
                JOIN categorias ON estoque.categoria = categorias.id_categorias 
                WHERE nome_produto LIKE %s OR id_produto LIKE %s
            """
            cursor.execute(comando, valores)
            resultados = cursor.fetchall()

        if not resultados:
            self.tela_principal.txt_caso_produto_nao_encontra_estoque.setText("Produto não encontrado!")
        else:
            self.tela_principal.txt_caso_produto_nao_encontra_estoque.setText("")  # Limpa a mensagem se encontrar resultados
            for resultado in resultados:
                id_produto, nome, preco, quantidade, categoria = resultado
                item = QTreeWidgetItem(tree)
                item.setText(0, str(id_produto))
                item.setText(1, nome)
                item.setText(2, str(preco))
                item.setText(3, str(quantidade))
                item.setText(4, categoria)

                # Alinhamento centralizado
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
        self.tela_principal.input_tipo_valor.setCurrentIndex(0)
        pixmap = QPixmap()
        self.tela_principal.img_produto_estoque.setPixmap(pixmap)
        self.tela_principal.stackedWidget_3.setCurrentIndex(1)
        self.tela_principal.input_categoria_produto.setCurrentIndex(-1)
        self.tela_principal.txt_preco_estoque.setText("Preço Un.")
        self.tela_principal.input_preco_produto.setPlaceholderText("PREÇO UN.")

    def carregar_categorias(self):
        cursor = self.conexao.get_cursor()
        comando = "SELECT id_categorias, nome_categoria FROM categorias ORDER BY id_categorias"
        cursor.execute(comando)
        categorias = cursor.fetchall()
            
        self.tela_principal.input_categoria_produto.clear()
            
        for id_cat, nome_cat in categorias:
            self.tela_principal.input_categoria_produto.addItem(nome_cat, id_cat)  
            self.tela_principal.input_categoria_produto_2.addItem(nome_cat, id_cat)  

        self.tela_principal.input_categoria_produto.setCurrentIndex(-1) 
            
        cursor.close()

    def adc_produto_estoque(self):
        self.nome = self.tela_principal.input_nome_produto.text()

        if not self.nome:
            QMessageBox.warning(None, "Erro", "Digite o nome do produto!")
            return
        if self.nome and not self.nome.replace(" ", "").isalpha():
            QMessageBox.warning(None, "Erro", "Apenas letras no Nome do Produto!")
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
        if preco and not preco.replace(" ", "").isdigit():
            QMessageBox.warning(None, "Erro", "Valor Invalido!")
            return
        if not preco or float(preco) <= 0:
            QMessageBox.warning(None, "Erro", "Digite um valor válido!")
            return

        quant = self.tela_principal.input_quantidade_produto.text()
        if quant and not quant.replace(" ", "").isdigit():
            QMessageBox.warning(None, "Erro", "Quantidade Invalida!")
            return
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

        tipo_valor = self.tela_principal.input_tipo_valor.currentIndex()
        if tipo_valor != 0 and tipo_valor != 1:
            QMessageBox.warning(None, "error", "Adicione Um tipo de Valor Valido!")
            return

        
        if self.new_file_path == "":
            QMessageBox.warning(None, "Erro", "Adicione uma Imagem!")
            return
        relative_path = os.path.relpath(self.new_file_path, os.getcwd()).replace("\\", "/")
        query = "INSERT INTO estoque (nome_produto, preco, quantidade, categoria, tipo_valor, imagem) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (self.nome, preco, quant, categoria_id, tipo_valor, relative_path)
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
                
            # Copy the image
            shutil.copy(file_path, self.new_file_path)

            # Display the image in the UI using absolute path for reliability
            absolute_path = os.path.abspath(self.new_file_path)
            pixmap = QPixmap(absolute_path)
            self.tela_principal.img_produto_estoque.setPixmap(pixmap)
            self.tela_principal.img_produto_estoque.setScaledContents(True)
            self.tela_principal.img_produto_estoque_2.setPixmap(pixmap)
            self.tela_principal.img_produto_estoque_2.setScaledContents(True)

    def tipo_valor(self):
        if self.tela_principal.input_tipo_valor.currentIndex() == 1:
            self.tela_principal.txt_preco_estoque.setText("Valor do KG")
            self.tela_principal.input_preco_produto.setPlaceholderText("KG")
            self.tela_principal.txt_quantidade_estoque.setText("Quantidade em KG no Estoque")
            self.tela_principal.input_quantidade_produto.setPlaceholderText("KG")
        else:
            self.tela_principal.txt_preco_estoque.setText("Valor da Unidade")
            self.tela_principal.input_preco_produto.setPlaceholderText("Preço Un.")
            self.tela_principal.txt_quantidade_estoque.setText("Quantidade de Unidades no Estoque")
            self.tela_principal.input_quantidade_produto.setPlaceholderText("Un.")

    def editar_produto(self):
        item_selecionado = self.tela_principal.treeWidget.currentItem()
        if item_selecionado == None:
            QMessageBox.warning(None, "error", "Selecione um Produto")
            return
        
        self.id_produto = item_selecionado.text(0)
        nome = item_selecionado.text(1)

        cursor = self.conexao.get_cursor()
        comando = "select preco, tipo_valor from estoque where id_produto = %s"
        cursor.execute(comando, (self.id_produto, ))
        resultado = cursor.fetchall()
        for i in resultado:
            preco, tipo_valor = i

        quantidade = item_selecionado.text(3)
        categoria = item_selecionado.text(4)


        self.tela_principal.input_nome_produto_2.setText(nome)
        self.tela_principal.input_categoria_produto_2.setCurrentText(categoria)
        self.tela_principal.input_quantidade_produto_2.setText(quantidade)
        self.tela_principal.input_preco_produto_2.setText(f"{float(preco)}")
        self.tela_principal.input_tipo_valor_2.setCurrentIndex(int(tipo_valor))

        comando = "select imagem from estoque where id_produto = %s"
        cursor.execute(comando, (self.id_produto, ))
        self.absolute_path = cursor.fetchone()[0]
        if self.absolute_path is None:
            pixmap = QPixmap()
        else:
            pixmap = QPixmap(self.absolute_path)
        self.tela_principal.img_produto_estoque_2.setPixmap(pixmap)
        self.tela_principal.img_produto_estoque_2.setScaledContents(True)

        self.tela_principal.stackedWidget_3.setCurrentIndex(2)

    def confirmar_atualizacao(self):

        cursor = self.conexao.get_cursor()

        self.nome = self.tela_principal.input_nome_produto_2.text()

        
        if self.nome and not self.nome.replace(" ", "").isalpha():
            QMessageBox.warning(None, "Erro", "Apenas letras no Nome do Produto!")
            return

        categoria_index = self.tela_principal.input_categoria_produto_2.currentIndex() + 1
        if not categoria_index:   
            QMessageBox.warning(None, "Erro", "Selecione uma categoria!")
            return

        preco = self.tela_principal.input_preco_produto_2.text()
        if preco and not preco.replace(" ", "").isdigit():
            QMessageBox.warning(None, "Erro", "Valor Invalido!")
            return
        if not preco or float(preco) <= 0:
            QMessageBox.warning(None, "Erro", "Digite um valor válido!")
            return

        quant = self.tela_principal.input_quantidade_produto_2.text()
        if quant and not quant.replace(" ", "").isdigit():
            QMessageBox.warning(None, "Erro", "Quantidade Invalida!")
            return
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
        
        if self.new_file_path != "" and self.new_file_path != None:
            relative_path = os.path.relpath(self.new_file_path, os.getcwd()).replace("\\", "/")

            if relative_path == None or relative_path == "":
                comando = "select imagem from estoque where id_produto = %s"
                cursor.execute(comando, (self.id_produto, ))
                self.new_file_path = cursor.fetchone()[0]
                relative_path = os.path.relpath(self.new_file_path, os.getcwd()).replace("\\", "/")
        else:
            relative_path = self.absolute_path

        comando = """UPDATE estoque SET nome_produto = %s,
                    categoria = %s, 
                    preco = %s, 
                    quantidade = %s, 
                    imagem = %s
                    WHERE id_produto = %s
                """
        
        valores = (self.nome, categoria_id, preco, quant, relative_path, self.id_produto)
        cursor.execute(comando, valores)
        self.conexao.commit()

        QMessageBox.information(None, "Sucesso", "Produto Atualizado com Sucesso!")
        self.tela_principal.stackedWidget_3.setCurrentIndex(0)