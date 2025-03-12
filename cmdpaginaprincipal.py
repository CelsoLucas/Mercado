from conexao_db import conexaoDB

class cmdPaginaPrincipal():
    def __init__(self, tela_principal):
        self.conexao = conexaoDB()
        self.tela_principal = tela_principal
        self.grafico_vendas_dia()

    def grafico_vendas_dia(self):
        cursor = self.conexao.get_cursor()
        comando = "select sum(valor_total) from vendas where data_venda = current_date"
        cursor.execute(comando)
        resultado = cursor.fetchone()[0]
        try:
            self.tela_principal.txt_vendas_dia_db.setText(f"R$ {float(resultado):.2f}")
        except TypeError:
                self.tela_principal.txt_vendas_dia_db.setText(f"R$ 00,00")

    def grafico_vendas_semana(self):
        cursor = self.conexao.get_cursor()
        comando = """SELECT SUM(valor_total) FROM vendas WHERE data_venda 
                     BETWEEN DATE_SUB(CURRENT_DATE, INTERVAL 6 DAY) AND CURRENT_DATE;
                  """
        cursor.execute(comando)
        resultado = cursor.fetchone()[0]
        try:
            self.tela_principal.txt_vendas_semana_db.setText(f"R$ {float(resultado):.2f}")
        except TypeError:
            self.tela_principal.txt_vendas_semana_db.setText(f"R$ 00,00")

    def grafico_vendas_mes(self):
        cursor = self.conexao.get_cursor()
        comando = """SELECT SUM(valor_total) FROM vendas 
                    WHERE MONTH(data_venda) = MONTH(CURRENT_DATE)
                    AND YEAR(data_venda) = YEAR(CURRENT_DATE);
                  """
        cursor.execute(comando)
        resultado = cursor.fetchone()[0]
        try:
            self.tela_principal.txt_vendas_mes_db.setText(f"R$ {float(resultado):.2f}")  
        except TypeError:
            self.tela_principal.txt_vendas_mes_db.setText(f"R$ 00,00")
    def produtos_baixo_estoque(self):
        cursor = self.conexao.get_cursor()
        comando = """SELECT nome_produto, quantidade FROM estoque
                WHERE quantidade < 10 ORDER BY quantidade ASC
                  """
        cursor.execute(comando)
        resultados = cursor.fetchall()  

        if resultados:
            texto = ""
            for nome_produto, quantidade in resultados:
                texto += f"- {nome_produto} ({quantidade} unidades)\n"
        else:
            texto = "Nenhum produto com baixo estoque."
        
        self.tela_principal.txt_produtos_baixo_estoque_db.setText(texto)   
        
    