from conexao_db import conexaoDB
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide6.QtWidgets import QVBoxLayout
import datetime

class cmdRelatorios:
    def __init__(self, tela_principal):
        self.tela_principal = tela_principal
        self.conexao = conexaoDB()
        self.layout = QVBoxLayout(self.tela_principal.frame_produtos_mai_vendidos)
        self.tela_principal.frame_produtos_mai_vendidos.setLayout(self.layout)
        self.relatorio_produtos_mais_vendidos()
        self.relatorio_top_5_operadores()
        self.relatorio_estoque_alerta()
        self.relatorio_formas_pagamento()

    def relatorio_produtos_mais_vendidos(self):
        # Referência ao frame
        frame = self.tela_principal.frame_produtos_mai_vendidos

        # Verifica se o frame já tem um layout; se sim, limpa os widgets; se não, cria um novo
        if frame.layout() is not None:
            layout = frame.layout()
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().setParent(None)  # Remove o widget do layout imediatamente
        else:
            layout = QVBoxLayout()
            frame.setLayout(layout)

        hoje = datetime.date.today()
        cursor = self.conexao.get_cursor()

        # Query atualizada com os novos nomes de colunas
        comando = """
            SELECT 
                e.nome_produto, 
                SUM(iv.quantidade_pedido) as qtd_vendida, 
                SUM(iv.subtotal) as valor_total
            FROM itens_venda iv
            JOIN estoque e ON iv.id_produto_pedido = e.id_produto
            JOIN vendas v ON iv.id_venda = v.id_venda
            WHERE DATE(v.data_venda) = %s
            GROUP BY e.id_produto, e.nome_produto
            ORDER BY qtd_vendida DESC
            LIMIT 10
        """
        cursor.execute(comando, (hoje,))
        resultados = cursor.fetchall()

        # Depuração: imprime os resultados no terminal
        print(f"Data usada na query: {hoje}")
        print(f"Resultados da query: {resultados}")

        # Preparando os dados para o gráfico
        if not resultados:
            nomes_produtos = ["Nenhum dado"]
            quantidades = [0]
            print("Nenhum resultado encontrado na query.")
        else:
            nomes_produtos = [row[0] for row in resultados]
            quantidades = [row[1] for row in resultados]
            print(f"Produtos encontrados: {nomes_produtos}")
            print(f"Quantidades: {quantidades}")

        cursor.close()

        # Criando o gráfico de barras
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.bar(nomes_produtos, quantidades, color='skyblue')
        ax.set_xlabel('Produtos')
        ax.set_ylabel('Quantidade Vendida')
        plt.xticks(rotation=45, ha='right')
        plt.grid(True)
        plt.tight_layout()

        # Integrando o gráfico ao layout
        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)
        canvas.draw()

        # Força a atualização do frame
        frame.update()

    def relatorio_top_5_operadores(self):
        # Referência ao frame
        frame = self.tela_principal.top_5_operadores

        # Verifica se o frame já tem um layout; se sim, limpa os widgets; se não, cria um novo
        if frame.layout() is not None:
            layout = frame.layout()
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().setParent(None)
        else:
            layout = QVBoxLayout()
            frame.setLayout(layout)

        hoje = datetime.date.today()
        cursor = self.conexao.get_cursor()

        # Query para pegar os 5 operadores com maior total de vendas do dia
        comando = """
            SELECT 
                u.nome, 
                SUM(v.valor_total) as total_vendas
            FROM vendas v
            JOIN usuarios u ON v.id_usuario = u.id_usuario
            WHERE DATE(v.data_venda) = %s
            GROUP BY v.id_usuario, u.nome
            ORDER BY total_vendas DESC
            LIMIT 5
        """
        cursor.execute(comando, (hoje,))
        resultados = cursor.fetchall()
        cursor.close()

        # Preparando os dados para o gráfico
        if not resultados:
            nomes_operadores = ["Nenhum dado"]
            totais_vendas = [0]
        else:
            nomes_operadores = [row[0] for row in resultados]
            totais_vendas = [row[1] for row in resultados]

        # Criando o gráfico de barras horizontais
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.barh(nomes_operadores, totais_vendas, color='lightgreen')
        ax.set_xlabel('Total de Vendas (R$)')
        ax.set_ylabel('Operadores')
        plt.tight_layout()

        # Integrando o gráfico ao layout
        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)
        canvas.draw()

        # Força a atualização do frame
        frame.update()

    def relatorio_estoque_alerta(self):
        # Referência ao frame
        frame = self.tela_principal.frame_estoque_alerta

        # Verifica se o frame já tem um layout; se sim, limpa os widgets; se não, cria um novo
        if frame.layout() is not None:
            layout = frame.layout()
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().setParent(None)
        else:
            layout = QVBoxLayout()
            frame.setLayout(layout)

        cursor = self.conexao.get_cursor()

        # Query para pegar produtos com estoque abaixo de 10 unidades
        comando = """
            SELECT 
                nome_produto, 
                quantidade
            FROM estoque
            WHERE quantidade < 10
            ORDER BY quantidade ASC
            LIMIT 10
        """
        cursor.execute(comando)
        resultados = cursor.fetchall()
        cursor.close()

        # Preparando os dados para o gráfico
        if not resultados:
            nomes_produtos = ["Nenhum dado"]
            quantidades = [0]
        else:
            nomes_produtos = [row[0] for row in resultados]
            quantidades = [row[1] for row in resultados]

        # Criando o gráfico de barras horizontais
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.barh(nomes_produtos, quantidades, color='salmon')
        ax.set_xlabel('Quantidade em Estoque')
        ax.set_ylabel('Produtos')
        plt.tight_layout()

        # Integrando o gráfico ao layout
        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)
        canvas.draw()
        frame.update()

    def relatorio_formas_pagamento(self):
        # Referência ao frame
        frame = self.tela_principal.frame_formas_pagamento

        # Verifica se o frame já tem um layout; se sim, limpa os widgets; se não, cria um novo
        if frame.layout() is not None:
            layout = frame.layout()
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().setParent(None)
        else:
            layout = QVBoxLayout()
            frame.setLayout(layout)

        hoje = datetime.date.today()
        cursor = self.conexao.get_cursor()

        # Query para pegar o total de vendas por forma de pagamento no dia atual
        comando = """
            SELECT 
                fp.forma_pagamento, 
                SUM(v.valor_total) as total_vendas
            FROM vendas v
            JOIN formapagamento fp ON v.id_forma_pagamento = fp.id_forma_pagamento
            WHERE DATE(v.data_venda) = %s
            GROUP BY fp.id_forma_pagamento, fp.forma_pagamento
        """
        cursor.execute(comando, (hoje,))
        resultados = cursor.fetchall()
        cursor.close()

        # Preparando os dados para o gráfico
        if not resultados:
            formas_pagamento = ["Nenhum dado"]
            totais_vendas = [1]  # Valor fictício para exibir "Nenhum dado" no gráfico
        else:
            formas_pagamento = [row[0] for row in resultados]
            totais_vendas = [row[1] for row in resultados]

        # Criando o gráfico de pizza
        fig, ax = plt.subplots(figsize=(6, 6))  # Tamanho ajustado para pizza
        ax.pie(totais_vendas, labels=formas_pagamento, autopct='%1.1f%%', startangle=90, colors=['#FF9999', '#66B2FF', '#99FF99', '#FFCC99'])
        ax.axis('equal')  # Garante que o gráfico seja um círculo

        # Integrando o gráfico ao layout
        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)
        canvas.draw()
        frame.update()