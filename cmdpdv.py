
class cmdPdv():
    def __init__(self):
        super().__init__()
        self.tela_principal.btn_pesquisar_produto.clicked.connect(lambda: self.procurar_produto)

    def procurar_produto(self):
        print("foi")

        self.resultado_busca_produto = self.tela_principal.input_pesquisar_produto.text()
        
        if not self.resultado_busca_produto:
            self.tela_principal.txt_caso_nao_produto_encontrado.setText("Digite um produto para buscar.")
            return

        cursor = self.conexao.cursor()

        valores = (self.resultado_busca_produto, self.resultado_busca_produto)
        cursor.execute("SELECT nome, preco FROM estoque WHERE nome = %s OR id = %s", valores)

        resultado = cursor.fetchone()

        if resultado is None:
            self.tela_principal.txt_caso_nao_produto_encontrado.setText("Produto não encontrado!")
        else:
            nome, preco = resultado
            self.tela_principal.stackedWidget_2.setCurrentIndex(1)
            self.tela_principal.txt_nome_preco_produto.setText(f"{nome} R${preco:.2f}")
            self.tela_principal.txt_quantidade.setText("0")
            
        cursor.close()
