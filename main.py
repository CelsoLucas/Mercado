from ui_tela_login import Ui_TelaLogin
from ui_tela_principal import Ui_TelaPrincipal
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QVBoxLayout
from PySide6.QtGui import QPixmap
import sys
import mysql.connector
from cmdpaginaprincipal import cmdPaginaPrincipal
from cmdpdv import cmdPdv
from cmdestoque import cmdEstoque
from cmdrelatorios import cmdRelatorios
from cmdconfiguracoes import cmdConfiguracoes
from conexao_db import conexaoDB

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
        
        self.tela_principal.txt_ola_user.setText(f"{self.user}")

        self.tela_principal.stackedWidget.setCurrentIndex(0)

        self.tela_principal.btn_sair.clicked.connect(self.init_tela_login)
        self.tela_principal.btn_tela_principal.clicked.connect(self.telaprincipal)
        self.tela_principal.btn_pdv.clicked.connect(self.telapdv)
        self.tela_principal.btn_estoque.clicked.connect(self.telaestoque)
        self.tela_principal.btn_relatorios.clicked.connect(self.telarelatorios)
        self.tela_principal.btn_configuracoes.clicked.connect(self.telaconfiguracoes)

        self.telaprin = cmdPaginaPrincipal(self.tela_principal)
        self.telaprin.grafico_vendas_dia()
        self.telaprin.grafico_vendas_semana()
        self.telaprin.grafico_vendas_mes()
        self.telaprin.produtos_baixo_estoque()


    def telaprincipal(self):
        self.tela_principal.stackedWidget.setCurrentIndex(0)
        self.telaprin = cmdPaginaPrincipal(self.tela_principal)
        self.telaprin.grafico_vendas_dia()
        self.telaprin.grafico_vendas_semana()
        self.telaprin.grafico_vendas_mes()
        self.telaprin.produtos_baixo_estoque()

    def telapdv(self):
        self.tela_principal.stackedWidget.setCurrentIndex(1)
        self.pdv = cmdPdv(self.tela_principal)
        self.tela_principal.stackedWidget_2.setCurrentIndex(0)
        self.tela_principal.stackedWidget_6.setCurrentIndex(0)
        self.tela_principal.btn_pdv_mais.clicked.connect(self.pdv.mais)
        self.tela_principal.btn_pdv_menos.clicked.connect(self.pdv.menos)
        self.tela_principal.btn_adc_carrinho.clicked.connect(self.pdv.adc_carrinho)
        self.tela_principal.btn_adc_carrinho_2.clicked.connect(self.pdv.adc_carrinho)
        self.tela_principal.btn_finaliza_compra.clicked.connect(self.pdv.finalizar_compra)

    def telaestoque(self):
        self.tela_principal.stackedWidget.setCurrentIndex(2)
        self.tela_principal.stackedWidget_3.setCurrentIndex(0)
        self.estoque = cmdEstoque(self.tela_principal)
        self.tela_principal.btn_pesquisar_produto_4.clicked.connect(self.estoque.procurar_produto)
        self.tela_principal.btn_adc_produto_estoque.clicked.connect(self.estoque.tela_adc_produto)
        self.tela_principal.btn_adc_foto_produto.clicked.connect(self.estoque.open_image)
        self.tela_principal.btn_adc_produto.clicked.connect(self.estoque.adc_produto_estoque)

    def telarelatorios(self):
        self.tela_principal.stackedWidget.setCurrentIndex(3)
        self.relatorios = cmdRelatorios(self.tela_principal)


    def telaconfiguracoes(self):
        self.tela_principal.stackedWidget.setCurrentIndex(4)
        self.config = cmdConfiguracoes(self.tela_principal.treeWidget_2, self.tela_principal)
        self.tela_principal.btn_adc_user.clicked.connect(self.config.tela_adc_usuario)
        self.tela_principal.btn_procurar_ft_adc_usuario.clicked.connect(self.config.open_image)
        self.tela_principal.btn_adc_usuario.clicked.connect(self.config.adc_usuario)
        self.tela_principal.btn_adc_categoria.clicked.connect(self.config.tela_adc_categoria)
        self.tela_principal.btn_adc_categoria_2.clicked.connect(self.config.adc_categoria)

    def init_tela_login(self):
        self.tela_login.setupUi(self)
        self.tela_login.btn_login.clicked.connect(self.check_login)

    def check_login(self):

        self.user = self.tela_login.input_user.text()
        cursor = self.conexao.get_cursor()
        
        comando = "SELECT senha, foto FROM usuarios WHERE nome = %s"
        cursor.execute(comando, (self.user,))
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
