from conexao_db import conexaoDB

class cmdPaginaPrincipal():
    def __init__(self, tela_principal):
        self.conexao = conexaoDB()
        self.tela_principal = tela_principal
        