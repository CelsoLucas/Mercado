from ui_tela_login import Ui_TelaLogin
from ui_tela_principal import Ui_TelaPrincipal
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QVBoxLayout
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import Qt
import sys
from cmdTelaLogin import CmdTelaLogin
from cmdpaginaprincipal import cmdPaginaPrincipal
from cmdpdv import cmdPdv
from cmdestoque import cmdEstoque
from cmdrelatorios import cmdRelatorios
from cmdconfiguracoes import cmdConfiguracoes
from conexao_db import conexaoDB

class main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tela_login = Ui_TelaLogin()
        self.tela_login.setupUi(self)
        self.setWindowTitle("LOGIN")
        self.setWindowIcon(QIcon("imgs/icon (1).png"))
        self.tela_login.btn_login.clicked.connect(self.check_login)
        self.tela_login.btn_esqueci_senha.clicked.connect(self.tela_recuperar_senha)

    def init_tela_principal(self):

        self.setWindowState(Qt.WindowMaximized)

        self.tela_principal = Ui_TelaPrincipal()
        self.tela_principal.setupUi(self)
        self.setWindowTitle("MERCADO DO CELSADAS")
        self.setWindowIcon(QIcon("imgs/icon (1).png"))

        self.setFixedSize(0, 0)  # Remove tamanho fixo
        self.setMinimumSize(0, 0)  # Permite qualquer tamanho mínimo
        self.setMaximumSize(16777215, 16777215)

        self.tela_principal.txt_ola_user.setText(f"{self.user}")

        self.tela_principal.stackedWidget.setCurrentIndex(0)
        self.tela_principal.btn_sair.clicked.connect(self.init_tela_login)
        self.tela_principal.btn_tela_principal.clicked.connect(self.telaprincipal)
        self.telaprincipal()

        self.tela_principal.btn_pdv.clicked.connect(self.telapdv)
        self.tela_principal.btn_estoque.clicked.connect(self.telaestoque)
        self.tela_principal.btn_relatorios.clicked.connect(self.telarelatorios)
        self.tela_principal.btn_configuracoes.clicked.connect(self.telaconfiguracoes)

        self.setWindowState(Qt.WindowMaximized)
        self.showMaximized()
        self.adjustSize()  # Ajusta o tamanho ao conteúdo, mas respeitando o estado maximizado
        self.update()
        self.repaint()

    def verificar_status(self):
        conexao = conexaoDB()
        cursor = conexao.get_cursor()
        comando = "select id_usuario from usuarios where nome = %s"
        cursor.execute(comando, (self.user,))
        id_usuario = cursor.fetchone()[0]

        comando = "Select * from caixa where id_user = %s and status = '1'"
        cursor.execute(comando, (id_usuario,))
        resultado = cursor.fetchall()
        if resultado == []:
            resultado = False
        else:
            resultado = True
        cursor.close()
        conexao.conexao.close()
        return resultado
    
    def telaprincipal(self):
        self.tela_principal.stackedWidget.setCurrentIndex(0)
        self.telaprin = cmdPaginaPrincipal(self.tela_principal)
        self.tela_principal.btn_abrir_caixa.clicked.connect(self.telaprin.tela_abrir_caixa)
        self.tela_principal.btn_fechar_caixa.clicked.connect(self.telaprin.tela_fechar_caixa)
        self.tela_principal.btn_sangria.clicked.connect(self.telaprin.tela_sangria)
        self.tela_principal.btn_suprimento.clicked.connect(self.telaprin.tela_suprimento)
        self.tela_principal.btn_cancelar_sangria.clicked.connect(self.telaprin.cancelar_acao)
        self.tela_principal.btn_cancelar_suprimento.clicked.connect(self.telaprin.cancelar_acao)
        self.tela_principal.btn_confirmar_abrir.clicked.connect(self.telaprin.abrir_caixa)
        self.tela_principal.btn_confirmar_sangria.clicked.connect(self.telaprin.registrar_sangria)
        self.tela_principal.btn_confirmar_suprimento.clicked.connect(self.telaprin.registrar_suprimento)
        self.tela_principal.btn_confirmar_fechar.clicked.connect(self.telaprin.fechar_caixa)

    def telapdv(self):
        resultado = self.verificar_status()
        if resultado is False:
            QMessageBox.information(None, "error", "Você deve abrir o caixa antes!")
        else:
            self.tela_principal.stackedWidget.setCurrentIndex(1)
            self.pdv = cmdPdv(self.tela_principal)
            self.tela_principal.stackedWidget_2.setCurrentIndex(0)
            self.tela_principal.stackedWidget_6.setCurrentIndex(0)
            self.tela_principal.btn_pdv_mais.clicked.connect(self.pdv.mais)
            self.tela_principal.btn_pdv_menos.clicked.connect(self.pdv.menos)
            self.tela_principal.btn_adc_carrinho.clicked.connect(self.pdv.adc_carrinho)
            self.tela_principal.btn_adc_carrinho_2.clicked.connect(self.pdv.adc_carrinho)
            self.tela_principal.btn_finaliza_compra.clicked.connect(self.pdv.finalizar_compra)
            self.tela_principal.btn_remover_produto_carrinho.clicked.connect(self.pdv.remover_carrinho)

    def telaestoque(self):
        resultado = self.verificar_status()
        if resultado is False:
            QMessageBox.information(None, "error", "Você deve abrir o caixa antes!")
        else:
            self.tela_principal.stackedWidget.setCurrentIndex(2)
            self.tela_principal.stackedWidget_3.setCurrentIndex(0)
            self.estoque = cmdEstoque(self.tela_principal)
            self.tela_principal.btn_pesquisar_produto_4.clicked.connect(self.estoque.procurar_produto)
            self.tela_principal.btn_adc_produto_estoque.clicked.connect(self.estoque.tela_adc_produto)
            self.tela_principal.btn_adc_foto_produto.clicked.connect(self.estoque.open_image)
            self.tela_principal.btn_adc_produto.clicked.connect(self.estoque.adc_produto_estoque)
            self.tela_principal.btn_editar_produto.clicked.connect(self.estoque.editar_produto)
            self.tela_principal.btn_adc_produto_2.clicked.connect(self.estoque.confirmar_atualizacao)
            self.tela_principal.btn_adc_foto_produto_2.clicked.connect(self.estoque.open_image)

    def telarelatorios(self):
        resultado = self.verificar_status()
        if resultado is False:
            QMessageBox.information(None, "error", "Você deve abrir o caixa antes!")
        else:
            self.tela_principal.stackedWidget.setCurrentIndex(3)
            self.relatorios = cmdRelatorios(self.tela_principal)


    def telaconfiguracoes(self):
        resultado = self.verificar_status()
        if resultado is False:
            QMessageBox.information(None, "error", "Você deve abrir o caixa antes!")
        else:
            self.tela_principal.stackedWidget.setCurrentIndex(4)
            self.config = cmdConfiguracoes(self.tela_principal.treeWidget_2, self.tela_principal)
            self.tela_principal.btn_adc_user.clicked.connect(self.config.tela_adc_usuario)
            self.tela_principal.btn_procurar_ft_adc_usuario.clicked.connect(self.config.open_image)
            self.tela_principal.btn_adc_usuario.clicked.connect(self.config.adc_usuario)
            self.tela_principal.btn_adc_categoria.clicked.connect(self.config.tela_adc_categoria)
            self.tela_principal.btn_adc_categoria_2.clicked.connect(self.config.adc_categoria)

    def init_tela_login(self):
        self.tela_login.setupUi(self)
        self.showMaximized()
        self.tela_login.btn_login.clicked.connect(self.check_login)
        self.tela_login.btn_esqueci_senha.clicked.connect(self.tela_recuperar_senha)

    def tela_recuperar_senha(self):
        self.recuperar_senha = CmdTelaLogin(self.tela_login)
        self.tela_login.stackedWidget.setCurrentIndex(1)
        self.tela_login.btn_enviar_codigo.clicked.connect(self.recuperar_senha.enviar_email_recuperacao)
        self.tela_login.btn_redefinir_senha.clicked.connect(self.recuperar_senha.verificar_e_mudar_senha)
        self.tela_login.btn_voltar.clicked.connect(self.recuperar_senha.voltar)

    def check_login(self):

        self.user = self.tela_login.input_user.text()
        conexao = conexaoDB()
        cursor = conexao.get_cursor()
        
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
        conexao.conexao.close()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = main()
    window.showMaximized()
    sys.exit(app.exec())
