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
            user="suporte",
            password="suporte",
            database="mercado"
        )
        self.tela_login = Ui_TelaLogin()
        self.tela_login.setupUi(self)
        self.tela_login.btn_login.clicked.connect(self.check_login)

    def init_tela_principal(self):
        self.tela_principal = Ui_TelaPrincipal()
        self.tela_principal.setupUi(self)

        self.tela_principal.stackedWidget.setCurrentIndex(0)

        self.tela_principal.btn_sair.clicked.connect(self.init_tela_login)
        self.tela_principal.btn_tela_principal.clicked.connect(self.telaprincipal)
        self.tela_principal.btn_pdv.clicked.connect(self.telapdv)
        self.tela_principal.btn_estoque.clicked.connect(self.telaestoque)
        self.tela_principal.btn_relatorios.clicked.connect(self.telarelatorios)
        self.tela_principal.btn_configuracoes.clicked.connect(self.telaconfiguracoes)


    def telaprincipal(self):
        self.tela_principal.stackedWidget.setCurrentIndex(0)

    def telapdv(self):
        self.tela_principal.stackedWidget.setCurrentIndex(1)
        self.tela_principal.stackedWidget_2.setCurrentIndex(0)    
        
    def telaestoque(self):
        self.tela_principal.stackedWidget.setCurrentIndex(2)
        self.tela_principal.stackedWidget_3.setCurrentIndex(0)

    def telarelatorios(self):
        self.tela_principal.stackedWidget.setCurrentIndex(3)

    def telaconfiguracoes(self):
        self.tela_principal.stackedWidget.setCurrentIndex(4)

        
    def init_tela_login(self):
        self.tela_login.setupUi(self)
        self.tela_login.btn_login.clicked.connect(self.check_login)

    def check_login(self):
        cursor = self.conexao.cursor()
        
        comando = "SELECT senha, img_local FROM usuarios WHERE nome_usu = %s"
        cursor.execute(comando, (self.tela_login.input_user.text(),))
        resultado = cursor.fetchone()
        
        if not resultado:
            QMessageBox.warning(self, "Erro", "Usuário inválido!")
            return
        
        senha_armazenada, foto_perfil = resultado
        
        comando_senha = "SELECT SHA2(%s, 256)"
        cursor.execute(comando_senha, (self.tela_login.input_senha.text(),))
        resultado_senha = cursor.fetchone()

        if not resultado_senha:
            QMessageBox.warning(self, "Erro", "Erro ao gerar o hash da senha digitada!")
            return

        senha_digitada_hash = resultado_senha[0]
        
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
