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

    def _limpar_layout(self, frame):
        """Função auxiliar para limpar o layout de um frame."""
        if frame.layout() is not None:
            layout = frame.layout()
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().setParent(None)
        else:
            layout = QVBoxLayout()
            frame.setLayout(layout)
        return layout

    def relatorio_produtos_mais_vendidos(self):
        frame = self.tela_principal.frame_produtos_mai_vendidos
        layout = self._limpar_layout(frame)

        hoje = datetime.date.today()
        cursor = self.conexao.get_cursor()
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
        cursor.close()

        if not resultados:
            nomes_produtos = ["Nenhum dado"]
            quantidades = [0]
        else:
            nomes_produtos = [row[0] for row in resultados]
            quantidades = [row[1] for row in resultados]

        fig, ax = plt.subplots(figsize=(10, 6), facecolor='#dbdbdb')
        ax.set_facecolor('#FFFFFF')
        ax.bar(nomes_produtos, quantidades, color='#4C51BF', edgecolor='#2D3748', linewidth=0.5)
        ax.set_title("Produtos Mais Vendidos", fontsize=20, fontfamily='Segoe UI', color='#2D3748')
        ax.set_ylabel('Quantidade Vendida', fontsize=14, fontfamily='Segoe UI', color='#2D3748')
        ax.tick_params(axis='x', labelsize=12, rotation=45, labelfontfamily='Segoe UI', color='#4A5568', labelcolor='#4A5568')
        ax.tick_params(axis='y', labelsize=12, labelfontfamily='Segoe UI', color='#4A5568', labelcolor='#4A5568')
        ax.grid(True, linestyle='--', alpha=0.7, color='#E2E8F0')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color('#E2E8F0')
        ax.spines['bottom'].set_color('#E2E8F0')
        plt.tight_layout()

        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)
        canvas.draw()
        frame.update()

    def relatorio_top_5_operadores(self):
        frame = self.tela_principal.top_5_operadores
        layout = self._limpar_layout(frame)

        hoje = datetime.date.today()
        cursor = self.conexao.get_cursor()
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

        if not resultados:
            nomes_operadores = ["Nenhum dado"]
            totais_vendas = [0]
        else:
            nomes_operadores = [row[0] for row in resultados]
            totais_vendas = [row[1] for row in resultados]

        fig, ax = plt.subplots(figsize=(8, 4), facecolor='#dbdbdb')
        ax.set_facecolor('#FFFFFF')
        ax.barh(nomes_operadores, totais_vendas, color='#48BB78', edgecolor='#2D3748', linewidth=0.5)  # Verde para operadores
        ax.set_title("Top 5 Operadores", fontsize=20, fontfamily='Segoe UI', color='#2D3748')
        ax.set_xlabel('Total de Vendas (R$)', fontsize=14, fontfamily='Segoe UI', color='#2D3748')
        ax.tick_params(axis='x', labelsize=12, labelfontfamily='Segoe UI', color='#4A5568', labelcolor='#4A5568')
        ax.tick_params(axis='y', labelsize=12, labelfontfamily='Segoe UI', color='#4A5568', labelcolor='#4A5568')
        ax.grid(True, linestyle='--', alpha=0.7, color='#E2E8F0')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color('#E2E8F0')
        ax.spines['bottom'].set_color('#E2E8F0')
        plt.tight_layout()

        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)
        canvas.draw()
        frame.update()

    def relatorio_estoque_alerta(self):
        frame = self.tela_principal.frame_estoque_alerta
        layout = self._limpar_layout(frame)

        cursor = self.conexao.get_cursor()
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

        if not resultados:
            nomes_produtos = ["Nenhum dado"]
            quantidades = [0]
        else:
            nomes_produtos = [row[0] for row in resultados]
            quantidades = [row[1] for row in resultados]

        fig, ax = plt.subplots(figsize=(8, 4), facecolor='#dbdbdb')
        ax.set_facecolor('#FFFFFF')
        ax.barh(nomes_produtos, quantidades, color='#E53E3E', edgecolor='#2D3748', linewidth=0.5)  # Vermelho para alerta
        ax.set_title("Estoque em Alerta", fontsize=20, fontfamily='Segoe UI', color='#2D3748')
        ax.set_xlabel('Quantidade em Estoque', fontsize=14, fontfamily='Segoe UI', color='#2D3748')
        ax.tick_params(axis='x', labelsize=12, labelfontfamily='Segoe UI', color='#4A5568', labelcolor='#4A5568')
        ax.tick_params(axis='y', labelsize=12, labelfontfamily='Segoe UI', color='#4A5568', labelcolor='#4A5568')
        ax.grid(True, linestyle='--', alpha=0.7, color='#E2E8F0')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color('#E2E8F0')
        ax.spines['bottom'].set_color('#E2E8F0')
        plt.tight_layout()

        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)
        canvas.draw()
        frame.update()

    def relatorio_formas_pagamento(self):
        frame = self.tela_principal.frame_formas_pagamento
        layout = self._limpar_layout(frame)

        hoje = datetime.date.today()
        cursor = self.conexao.get_cursor()

        # Query ajustada para somar os valores de cada forma de pagamento diretamente da tabela vendas
        comando = """
            SELECT 
                SUM(valor_pix) as total_pix,
                SUM(valor_credito) as total_credito,
                SUM(valor_debito) as total_debito,
                SUM(valor_dinheiro) as total_dinheiro
            FROM vendas
            WHERE DATE(data_venda) = %s
        """
        cursor.execute(comando, (hoje,))
        resultado = cursor.fetchone()
        cursor.close()

        # Preparando os dados para o gráfico
        formas_pagamento = ["Pix", "Crédito", "Débito", "Dinheiro"]
        totais_vendas = [
            resultado[0] if resultado[0] is not None else 0,
            resultado[1] if resultado[1] is not None else 0,
            resultado[2] if resultado[2] is not None else 0,
            resultado[3] if resultado[3] is not None else 0
        ]

        # Verifica se há dados; se não, exibe "Nenhum dado"
        if sum(totais_vendas) == 0:
            formas_pagamento = ["Nenhum dado"]
            totais_vendas = [1]
        else:
            # Filtra formas de pagamento com valor zero para evitar clutter no gráfico
            formas_pagamento = [forma for forma, total in zip(formas_pagamento, totais_vendas) if total > 0]
            totais_vendas = [total for total in totais_vendas if total > 0]

        # Criando o gráfico de pizza
        fig, ax = plt.subplots(figsize=(6, 6), facecolor='#dbdbdb')
        ax.set_facecolor('#FFFFFF')
        ax.pie(totais_vendas, labels=formas_pagamento, autopct='%1.1f%%', startangle=90, 
            colors=['#FF9999', '#66B2FF', '#99FF99', '#FFCC99'], 
            textprops={'fontsize': 12, 'fontfamily': 'Segoe UI', 'color': '#2D3748'})
        ax.set_title("Formas de Pagamento", fontsize=20, fontfamily='Segoe UI', color='#2D3748')
        ax.axis('equal')

        # Integrando o gráfico ao layout
        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)
        canvas.draw()
        frame.update()