from conexao_db import conexaoDB

class checker():
    def __init__(self, usuario, senha, txt_validacao):

        self.conexao = conexaoDB() 

        comando = f"select senha from usuarios where nome_usu = '{usuario}'"
        resultado = self.conexao.select_bd(comando)

        if not resultado:
            txt_validacao.configure(text="Usuario Invalido!", text_color="red")
        else:
            if senha != resultado[0][0]:
                txt_validacao.configure(text="Senha Invalida!", text_color="red")
            else:
                txt_validacao.configure(text=f"Bem Vindo {usuario}", text_color="green")


        self.conexao.fechar_conexao()