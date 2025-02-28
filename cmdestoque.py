from conexao_db import conexaoDB
from PySide6.QtWidgets import QTreeWidgetItem, QMessageBox, QFileDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
import os
import shutil

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
    
    def tela_adc_produto(self):
        self.tela_principal.stackedWidget_3.setCurrentIndex(1)

    def adc_produto_estoque(self, input_nome_produto, input_preco_produto, input_quantidade_produto, input_categoria_produto):
        cursor = self.conexao.get_cursor()

        comando = "select nome from estoque"
        cursor.execute(comando)
        resultado = cursor.fetchall()

        self.nome = input_nome_produto.text()

        if self.nome in resultado:
            QMessageBox.warning(None, "error", "Produto já Cadastrado")
            return
        
        preco = input_preco_produto.text()
        if preco == "":
            QMessageBox.warning(None, "error", "Digite um Valor Valido!")
            return
        
        quant = input_quantidade_produto.text()
        if quant == "":
            QMessageBox.warning(None, "error", "Digite uma Quantidade Valida!")
            return
        

        categoria = input_categoria_produto.currentText()

        comando = "select id_categoria from categorias where categoria = %s"
        cursor.execute(comando, (categoria,))
        resultado = cursor.fetchone()

        if not resultado:
            QMessageBox.warning(None, "error", "Selecione uma Categoria")
            return
        categoria = resultado

        cursor = self.conexao.get_cursor()
        query = "INSERT INTO estoque (nome, preco, quantidade, categoria, imagem) VALUES (%s, %s, %s, %s, %s)"
        valores = (self.nome, preco, quant, categoria, self.new_file_path)            
        cursor.execute(query, valores)
        self.conexao.commit()

    def open_image(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(None, "Open Image", "", "Images(*.png *.xpm *.jpg *.jpeg *.bmp);;All Files (*)")

        if file_path:
            # Criar diretório de destino se não existir
            save_dir = "imgs"
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)

            # Definir novo nome para a imagem (exemplo: usando o nome do usuário)
            prod_name = self.nome.replace(" ", "_")
            new_file_name = f"{prod_name}.jpg"  # Salvar sempre como .jpg para padronização

            # Caminho completo do arquivo de destino
            self.new_file_path = os.path.join(f"mercado/", save_dir, new_file_name)

            # Copiar a imagem para a pasta de destino
            shutil.copy(file_path, self.new_file_path)

            # Exibir a imagem na interface
            pixmap = QPixmap(self.new_file_path)
            self.tela_principal.img_produto_adc_estoque.setPixmap(pixmap)
            self.tela_principal.img_produto_adc_estoque.setScaledContents(True)
            self.tela_principal.img_produto_adc_estoque.setPixmap(pixmap)