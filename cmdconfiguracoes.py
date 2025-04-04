from PySide6.QtWidgets import QTreeWidgetItem, QMessageBox, QFileDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from conexao_db import conexaoDB
import os
import random
import string
import shutil
import dns.resolver

class cmdConfiguracoes():
    def __init__(self, tree, tela_principal):
        self.conexao = conexaoDB()
        self.tree = tree
        self.tela_principal = tela_principal
        self.new_file_path = ""
        self.tela_principal.tabWidget.currentChanged.connect(self.on_tab_changed)
        self.mostrar_usuarios()
        self.mostrar_categoria()
        self.tela_principal.tabWidget.setCurrentIndex(0)
        self.tela_principal.stackedWidget_5.setCurrentIndex(0)
        self.tela_principal.stackedWidget_4.setCurrentIndex(0)
        self.tela_principal.stackedWidget_6.setCurrentIndex(0)


    def on_tab_changed(self):
        if self.tela_principal.tabWidget.currentIndex() == 0:  
            self.tela_principal.stackedWidget_4.setCurrentIndex(0)
        elif self.tela_principal.tabWidget.currentIndex() == 1: 
            self.tela_principal.stackedWidget_5.setCurrentIndex(0)

    def mostrar_usuarios(self):
        cursor = self.conexao.get_cursor()
        cursor.execute("select cod, nome, email, cpf, telefone, perm from usuarios")
        resultado = cursor.fetchall()

        tree = self.tela_principal.treeWidget_2
        tree.clear()

        for i in resultado:
            cod, nome, email, cpf, telefone, perm = i
            item = QTreeWidgetItem(tree)
            item.setText(0, str(cod))  
            item.setText(1, nome)  
            item.setText(2, str(email))  
            item.setText(3, str(cpf))  
            item.setText(4, str(telefone))
            item.setText(5, str(perm))


            item.setTextAlignment(0, Qt.AlignCenter)
            item.setTextAlignment(1, Qt.AlignCenter)
            item.setTextAlignment(2, Qt.AlignCenter)
            item.setTextAlignment(3, Qt.AlignCenter)
            item.setTextAlignment(4, Qt.AlignCenter)
            item.setTextAlignment(5, Qt.AlignCenter)


            tree.addTopLevelItem(item)

        cursor.close()
    
    def validar_email(self, email):
        try:
            dominio = email.split('@')[1]
            registros_mx = dns.resolver.resolve(dominio, 'MX')
            return bool(registros_mx)
        except:
            return False
        
    def valida_cpf(self, cpf):
        cpf = ''.join(filter(str.isdigit, cpf))

        if len(cpf) != 11:
            return False

        if cpf == cpf[0] * 11:
            return False

        soma1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
        digito1 = (soma1 * 10) % 11
        if digito1 == 10 or digito1 == 11:
            digito1 = 0
        if digito1 != int(cpf[9]):
            return False

        soma2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
        digito2 = (soma2 * 10) % 11
        if digito2 == 10 or digito2 == 11:
            digito2 = 0
        if digito2 != int(cpf[10]):
            return False

        return True

    def gerar_codigo_recuperacao(self):
        """Gera um código de 6 dígitos"""
        return ''.join(random.choices(string.digits, k=6))
    
    def adc_usuario(self):
        
        cursor = self.conexao.get_cursor()
        nome = self.tela_principal.input_nome_adc_usuario.text()
        comando = "select nome from usuarios where nome = %s"
        cursor.execute(comando, (nome,))
        resultado = cursor.fetchone()
        if resultado == None:
            self.nome = self.tela_principal.input_nome_adc_usuario.text()
        else:
            QMessageBox.warning(None, "Erro", f"Nome de Usuario ja Cdastrado!")
            cursor.close()
            return
        
        email = self.tela_principal.input_email_adc_usuario.text()
        email_valido = self.validar_email(email)
        if email_valido == False:
            QMessageBox.warning(None, "error", "Digite um email valido!")
            return
        
        comando = "select email from usuarios where email = %s"
        cursor.execute(comando, (email,))
        resultado = cursor.fetchone()
        if resultado:
            QMessageBox.warning(None, "error", "Email já cadastrado!")
            return
        
        senha = self.tela_principal.input_senha_adc_usuario.text()

        cpf = self.tela_principal.input_cpf_adc_usuario.text()
        if cpf and not cpf.replace(" ", "").isdigit():
            QMessageBox.warning(None, "Erro", "CPF Invalido!")
            return
        if not self.valida_cpf(cpf):
            QMessageBox.warning(None, "Erro", "Digite um CPF válido!")
            return

        comando = "SELECT cpf FROM usuarios WHERE cpf = %s"
        cursor.execute(comando, (cpf,))
        if cursor.fetchone():
            QMessageBox.warning(None, "Erro", "CPF já cadastrado!")
            return

        telefone = self.tela_principal.input_telefone_adc_usuario.text()
        if telefone and not telefone.replace(" ", "").isdigit():
            QMessageBox.warning(None, "Erro", "telefone Invalido!")
            return
        
        if self.tela_principal.perm_n.isChecked():
            perm = "0"
        elif self.tela_principal.perm_s.isChecked():
            perm = "1"

        if self.new_file_path == "":
            QMessageBox.warning(None, "Erro", "Adicione uma Imagem!")
            return
        relative_path = os.path.relpath(self.new_file_path, os.getcwd()).replace("\\", "/")

        codigo = self.gerar_codigo_recuperacao()

        comando = "insert into usuarios (nome, email, cpf, telefone, senha, cod, perm, foto) values (%s, %s, %s, %s, sha2(%s, 256), %s, %s, %s)"
        dados = (nome, email, cpf, telefone, senha, codigo, perm, relative_path)

        cursor.execute(comando, dados)
        self.conexao.commit()
        cursor.close()
        QMessageBox.information(None, "Sucesso", "Cadastro realizado com sucesso!")
        self.mostrar_usuarios()
        self.tela_principal.stackedWidget_4.setCurrentIndex(0)


    def open_image(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(None, "Open Image", "", "Images(*.png *.xpm *.jpg *.jpeg *.bmp);;All Files (*)")

        if file_path:
            # Define the destination directory
            save_dir = "imgs/foto_usuarios"  # Corrected to a single, intended directory
            
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
                self.tela_principal.label_img_adc_usuario.setPixmap(pixmap)
                self.tela_principal.label_img_adc_usuario.setScaledContents(True)

            except Exception as e:
                QMessageBox.warning(None, "error", f"{e}")
                raise
    
    def tela_adc_usuario(self):
        self.tela_principal.stackedWidget_4.setCurrentIndex(1)
        self.tela_principal.input_nome_adc_usuario.setText("")
        self.tela_principal.input_email_adc_usuario.setText("")
        self.tela_principal.input_senha_adc_usuario.setText("")
        self.tela_principal.input_cpf_adc_usuario.setText("")
        self.tela_principal.input_telefone_adc_usuario.setText("")

    
    def tela_adc_categoria(self):
        self.tela_principal.stackedWidget_5.setCurrentIndex(1)
        self.tela_principal.input_nome_adc_categoria.setText("")

    def mostrar_categoria(self):
        cursor = self.conexao.get_cursor()
        cursor.execute("select id_categorias, nome_categoria from categorias ORDER BY id_categorias ASC")
        resultado = cursor.fetchall()

        tree = self.tela_principal.tabela_categoria
        tree.clear()

        for i in resultado:
            id, nome,= i
            item = QTreeWidgetItem(tree)
            item.setText(0, str(id))  
            item.setText(1, nome)  

            item.setTextAlignment(0, Qt.AlignCenter)
            item.setTextAlignment(1, Qt.AlignCenter)

            tree.addTopLevelItem(item)

        cursor.close()
    
    def adc_categoria(self):

        nome = self.tela_principal.input_nome_adc_categoria.text()
        if nome == "":
            QMessageBox.warning(None, "error", "Digite um nome valido!")
            return
        
        cursor = self.conexao.get_cursor()

        comando = "insert into categorias (nome_categoria) values (%s)"
        dados = (nome,)

        cursor.execute(comando, dados)
        self.conexao.commit()
        cursor.close()
        QMessageBox.information(None, "Sucesso", "Categoria Cadastrada com Sucesso!")
        self.tela_principal.stackedWidget_5.setCurrentIndex(0)

        self.mostrar_categoria()
