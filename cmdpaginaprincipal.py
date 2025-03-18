from PySide6.QtWidgets import QMessageBox
from conexao_db import conexaoDB
import datetime

class cmdPaginaPrincipal():
    def __init__(self, tela_principal):
        self.conexao = conexaoDB()
        self.tela_principal = tela_principal
        self.tela_principal.stackedWidget_7.setCurrentIndex(0)
        
    def tela_abrir_caixa(self):
        self.tela_principal.stackedWidget_7.setCurrentIndex(1)
    
    def tela_fechar_caixa(self):
        self.tela_principal.stackedWidget_7.setCurrentIndex(2)

    def tela_sangria(self):
        self.tela_principal.stackedWidget_7.setCurrentIndex(3)
        self.tela_principal.btn_cancelar_sangria.clicked.connect(self.cancelar_acao)

    def tela_suprimento(self):
        self.tela_principal.stackedWidget_7.setCurrentIndex(4)
        self.tela_principal.btn_cancelar_suprimento.clicked.connect(self.cancelar_acao)

    def cancelar_acao(self):
        self.tela_principal.stackedWidget_7.setCurrentIndex(0)

    def abrir_caixa(self):
        quant_init = self.tela_principal.input_quantidade_caixa_abrir.text()
        hoje = datetime.date.today()

        cursor = self.conexao.get_cursor()
        comando = "select sum(valor_total) from vendas where data_venda = %s"
        cursor.execute(comando, (hoje, ))
        total_vendas_dia = cursor.fetchone()[0]

        if float(quant_init) < float(total_vendas_dia):
            QMessageBox.warning(None, "error", "Quantidade Menor que Total no Caixa!")
            return
                

