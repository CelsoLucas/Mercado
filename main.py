from ui_tela_login import Ui_TelaLogin
from ui_tela_principal import Ui_TelaPrincipal
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QVBoxLayout
from PySide6.QtGui import QPixmap
import sys
import mysql.connector
from cmdpdv import cmdPdv
from cmdestoque import cmdEstoque
from cmdconfiguracoes import cmdConfiguracoes
from cmdconfiguracoes import cmdConfiguracoes
from conexao_db import conexaoDB
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.conexao = conexaoDB()
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
        self.pdv = cmdPdv(
        self.tela_principal.btn_pesquisar_produto,
        self.tela_principal.input_pesquisar_produto,
        self.tela_principal.txt_caso_nao_produto_encontrado,
        self.tela_principal.stackedWidget_2,
        self.tela_principal.txt_quantidade,
        self.tela_principal.txt_nome_preco_produto,
        self.tela_principal,
        self.tela_principal.txt_nome_produto_1,
        self.tela_principal.txt_quantidade_1,
        self.tela_principal.txt_valor_1)
        self.tela_principal.btn_pesquisar_produto.clicked.connect(self.pdv.procurar_produto)
        self.tela_principal.btn_menos.clicked.connect(self.pdv.menos)
        self.tela_principal.btn_mais.clicked.connect(self.pdv.mais)


    def telaestoque(self):
        self.tela_principal.stackedWidget.setCurrentIndex(2)
        self.tela_principal.stackedWidget_3.setCurrentIndex(0)
        self.estoque = cmdEstoque(self.tela_principal,
                                  self.tela_principal.input_pesquisar_produto_4,
                                  self.tela_principal.txt_caso_produto_nao_encontra_estoque,
                                  self.tela_principal.treeWidget,
                                  self.tela_principal.input_nome_produto,
                                  self.tela_principal.input_categoria_produto)
        self.tela_principal.btn_pesquisar_produto_4.clicked.connect(self.estoque.procurar_produto)
        self.tela_principal.btn_adc_produto_estoque.clicked.connect(self.estoque.tela_adc_produto)
        self.tela_principal.btn_adc_produto.clicked.connect(lambda: self.estoque.adc_produto_estoque(self.tela_principal.input_nome_produto, self.tela_principal.input_preco_produto, self.tela_principal.input_quantidade_produto, self.tela_principal.input_categoria_produto))

    def telarelatorios(self):
        self.tela_principal.stackedWidget.setCurrentIndex(3)

    def telaconfiguracoes(self):
        self.tela_principal.stackedWidget.setCurrentIndex(4)
        self.config = cmdConfiguracoes(self.tela_principal.treeWidget_2, self.tela_principal)
        self.tela_principal.btn_adc_user.clicked.connect(self.config.tela_adc_usuario)
        self.tela_principal.btn_procurar_ft_adc_usuario.clicked.connect(self.config.open_image)
        self.tela_principal.btn_adc_usuario.clicked.connect(lambda: self.config.adc_usuario(self.tela_principal.input_nome_adc_usuario,
                                                                                    self.tela_principal.input_email_adc_usuario,
                                                                                    self.tela_principal.input_senha_adc_usuario,
                                                                                    self.tela_principal.input_cpf_adc_usuario,
                                                                                    self.tela_principal.input_telefone_adc_usuario))
        self.tela_principal.btn_adc_categoria.clicked.connect(self.config.tela_adc_categoria)
        self.tela_principal.btn_adc_categoria_2.clicked.connect(lambda: self.config.adc_categoria(self.tela_principal.input_nome_adc_categoria))
    def init_tela_login(self):
        self.tela_login.setupUi(self)
        self.tela_login.btn_login.clicked.connect(self.check_login)

    def check_login(self):
        cursor = self.conexao.get_cursor()
        
        comando = "SELECT senha, foto FROM usuarios WHERE nome = %s"
        cursor.execute(comando, (self.tela_login.input_user.text(),))
        resultado = cursor.fetchone()
        
        if not resultado:
            QMessageBox.warning(None, "Erro", "Usuário inválido!")
            return
        
        senha_armazenada, foto_perfil = resultado
        
        comando_senha = "SELECT SHA2(%s, 256)"
        cursor.execute(comando_senha, (self.tela_login.input_senha.text(),))
        resultado_senha = cursor.fetchone()

        if not resultado_senha:
            QMessageBox.warning(None, "Erro", "Erro ao gerar o hash da senha digitada!")
            return

        senha_digitada_hash = resultado_senha[0]
        
        if senha_digitada_hash != senha_armazenada:
            QMessageBox.warning(None, "Erro", "Senha inválida!")
        else:
            if foto_perfil:
                pixmap = QPixmap(foto_perfil)
                self.tela_login.icon_login.setPixmap(pixmap)
                self.tela_login.icon_login.setScaledContents(True)
            QMessageBox.information(None, "Sucesso", f"Bem-vindo, {self.tela_login.input_user.text()}!")
            self.init_tela_principal()
            
        cursor.close()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = main()
    window.show()
    sys.exit(app.exec())
