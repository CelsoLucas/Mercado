from ui_tela_login import Ui_TelaLogin
from ui_tela_principal import Ui_TelaPrincipal
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
import sys
import mysql.connector


class main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="celsadas",
            password="33880188",
            database="mercado"
        )
        self.tela_login = Ui_TelaLogin()
        self.tela_login.setupUi(self)
        self.tela_login.btn_login.clicked.connect(self.check_login)

    def init_tela_principal(self):
        self.tela_principal = Ui_TelaPrincipal()
        self.tela_principal.setupUi(self)
        
    def init_tela_login(self):
        self.tela_login.setupUi(self)

    def check_login(self):
        cursor = self.conexao.cursor()
        
        comando = "SELECT senha, img_local FROM usuarios WHERE nome_usu = %s"
        cursor.execute(comando, (self.tela_login.input_user.text(),))
        resultado = cursor.fetchone()
        
        if not resultado:
            QMessageBox.warning(self, "Erro", "Usuário inválido!")
            return
        
        senha_armazenada, foto_perfil = resultado

        print("Senha armazenada (hash):", senha_armazenada)
        
        comando_senha = "SELECT SHA2(%s, 256)"
        cursor.execute(comando_senha, (self.tela_login.input_senha.text(),))
        resultado_senha = cursor.fetchone()

        if not resultado_senha:
            QMessageBox.warning(self, "Erro", "Erro ao gerar o hash da senha digitada!")
            return

        senha_digitada_hash = resultado_senha[0]

        print("Senha digitada (hash):", senha_digitada_hash)
        
        if senha_digitada_hash != senha_armazenada:
            QMessageBox.warning(self, "Erro", "Senha inválida!")
        else:
            QMessageBox.information(self, "Sucesso", f"Bem-vindo, {self.tela_login.input_user.text()}!")
            self.init_tela_principal()
            
        cursor.close()


        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = main()
    window.show()
    sys.exit(app.exec())
