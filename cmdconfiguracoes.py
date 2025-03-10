from PySide6.QtWidgets import QTreeWidgetItem, QMessageBox, QFileDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from conexao_db import conexaoDB
import os
import shutil
import dns.resolver

class cmdConfiguracoes():
    def __init__(self, tree, tela_principal):
        self.conexao = conexaoDB()
        self.tree = tree
        self.tela_principal = tela_principal
        self.mostrar_usuarios()
        self.mostrar_categoria()
        self.mostrar_formapagamento()
        self.tela_principal.tabWidget.setCurrentIndex(0)
        self.tela_principal.stackedWidget_5.setCurrentIndex(0)
        self.tela_principal.stackedWidget_4.setCurrentIndex(0)
        self.tela_principal.stackedWidget_6.setCurrentIndex(0)


    def mostrar_usuarios(self):
        cursor = self.conexao.get_cursor()
        cursor.execute("select id_usuario, nome, email, cpf, telefone, ativo from usuarios")
        resultado = cursor.fetchall()

        tree = self.tela_principal.treeWidget_2
        tree.clear()

        for i in resultado:
            id, nome, email, cpf, telefone, ativo = i
            item = QTreeWidgetItem(tree)
            item.setText(0, str(id))  
            item.setText(1, nome)  
            item.setText(2, str(email))  
            item.setText(3, str(cpf))  
            item.setText(4, str(telefone))
            item.setText(5, str(ativo))


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
    
    def adc_usuario(self, input_nome_adc_usuario, input_email_adc_usuario, input_senha_adc_usuario, input_cpf_adc_usuario, input_telefone_adc_usuario):
        
        cursor = self.conexao.get_cursor()
        nome = input_nome_adc_usuario.text()
        comando = "select nome from usuarios where nome = %s"
        cursor.execute(comando, (nome,))
        resultado = cursor.fetchone()
        if resultado:
            QMessageBox.warning(None, "error", "Nome de Usuario já cadastrado!")
            return
        
        email = input_email_adc_usuario.text()
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
        
        senha = input_senha_adc_usuario.text()

        cpf = input_cpf_adc_usuario.text()
        if not self.valida_cpf(cpf):
            QMessageBox.warning(None, "Erro", "Digite um CPF válido!")
            return

        comando = "SELECT cpf FROM usuarios WHERE cpf = %s"
        cursor.execute(comando, (cpf,))
        if cursor.fetchone():
            QMessageBox.warning(None, "Erro", "CPF já cadastrado!")
            return

        telefone = input_telefone_adc_usuario.text()
        
        relative_path = os.path.relpath(self.new_file_path, os.getcwd()).replace("\\", "/")

        comando = "insert into usuarios (nome, email, cpf, telefone, senha, foto) values (%s, %s, %s, %s, sha2(%s, 256), %s)"
        dados = (nome, email, cpf, telefone, senha, relative_path)

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

    def tela_adc_formapagamento(self):
        self.tela_principal.stackedWidget_6.setCurrentIndex(1)
        self.tela_principal.input_nome_adc_forma_pagamento.setText("")

    def mostrar_categoria(self):
        cursor = self.conexao.get_cursor()
        cursor.execute("select id_categorias, nome_categoria from categorias")
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
    
    def adc_categoria(self, input_nome_adc_categoria):

        nome = input_nome_adc_categoria.text()
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

    def mostrar_formapagamento(self):
        cursor = self.conexao.get_cursor()
        cursor.execute("SELECT id_forma_pagamento, forma_pagamento FROM formapagamento ORDER BY id_forma_pagamento ASC")
        resultado = cursor.fetchall()

        tree = self.tela_principal.tabela_forma_pagamento
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

    def adc_forma_pagamento(self, input_nome_adc_forma_pagamento):
        nome = input_nome_adc_forma_pagamento.text().strip()

        if not nome:
            QMessageBox.warning(None, "Erro", "Digite uma forma de pagamento válida!")
            return

        cursor = self.conexao.get_cursor()

        comando = "SELECT forma_pagamento FROM formapagamento WHERE forma_pagamento = %s"
        cursor.execute(comando, (nome,))
        if cursor.fetchone():
            QMessageBox.warning(None, "Erro", "Forma de pagamento já cadastrada!")
            cursor.close()
            return

        comando = "INSERT INTO formapagamento (forma_pagamento) VALUES (%s)"
        dados = (nome,)
        cursor.execute(comando, dados)
        self.conexao.commit()
        cursor.close()

        QMessageBox.information(None, "Sucesso", "Forma de pagamento cadastrada com sucesso!")
        self.tela_principal.stackedWidget_6.setCurrentIndex(0)
        self.mostrar_formapagamento()