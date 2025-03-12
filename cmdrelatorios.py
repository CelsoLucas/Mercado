from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide6.QtWidgets import QVBoxLayout
from conexao_db import conexaoDB

class cmdRelatorios():
    def __init__(self, tela_principal):
        self.conexao = conexaoDB()
        self.tela_principal = tela_principal
        self.canvas_produtos = None  # Para o gráfico de produtos mais vendidos

    def vendas_ultimos_seis_meses(self):
        cursor = self.conexao.get_cursor()

        # Consulta para os últimos 6 meses
        comando = """
            SELECT YEAR(data_venda) AS ano, MONTH(data_venda) AS mes, SUM(valor_total) AS total
            FROM vendas
            WHERE data_venda >= DATE_SUB(CURRENT_DATE, INTERVAL 5 MONTH)
            GROUP BY YEAR(data_venda), MONTH(data_venda)
            ORDER BY ano, mes
        """
        cursor.execute(comando)
        resultados = cursor.fetchall()

        # Preparar dados para o gráfico
        meses = []
        valores = []
        for ano, mes, total in resultados:
            data = datetime(ano, mes, 1)
            meses.append(data.strftime("%b/%Y"))
            valores.append(float(total) if total is not None else 0.0)

        # Preencher meses sem vendas com zeros para garantir 6 pontos
        hoje = datetime.now()
        meses_completos = []
        valores_completos = []
        for i in range(5, -1, -1):  # Últimos 6 meses, do mais antigo ao atual
            mes_esperado = (hoje.month - i) % 12 or 12
            ano_esperado = hoje.year - (1 if hoje.month - i <= 0 else 0)
            mes_label = datetime(ano_esperado, mes_esperado, 1).strftime("%b/%Y")
            meses_completos.append(mes_label)
            if mes_label in meses:
                idx = meses.index(mes_label)
                valores_completos.append(valores[idx])
            else:
                valores_completos.append(0.0)

        # Criar o gráfico com design moderno
        fig, ax = plt.subplots(figsize=(4, 2), dpi=100)

        # Criar gráfico de barras
        ax.bar(
            meses_completos, 
            valores_completos, 
            color='#2a9d8f',  # Verde azulado elegante
            edgecolor='#264653',  # Bordas escuras
            linewidth=1.5,
        )

        # Definir o limite inferior do eixo Y como 0 e deixar o superior automático
        ax.set_ylim(0)  # Corrige para o formato correto: apenas o limite inferior

        # Personalizar o fundo e bordas
        ax.set_facecolor('#f8f9fa')  # Fundo cinza claro
        fig.patch.set_facecolor('#ffffff')  # Fundo externo branco

        # Configurar títulos e rótulos
        ax.set_ylabel("Total de Vendas (R$)", fontsize=12, color='#495057')

        # Estilizar a grade
        ax.grid(True, linestyle='--', alpha=0.6, color='#adb5bd')

        # Ajustar os ticks do eixo X
        plt.yticks(fontsize=10, color='#495057')

        # Remover bordas desnecessárias (estilo minimalista)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color('#dee2e6')
        ax.spines['bottom'].set_color('#dee2e6')

        # Ajustar layout
        plt.tight_layout()

        # Integrar o gráfico ao frame
        canvas = FigureCanvas(fig)

        # Limpar o layout existente do frame
        if self.tela_principal.frame_vendas_ultimos_seis_meses.layout() is not None:
            while self.tela_principal.frame_vendas_ultimos_seis_meses.layout().count():
                item = self.tela_principal.frame_vendas_ultimos_seis_meses.layout().takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
        else:
            QVBoxLayout(self.tela_principal.frame_vendas_ultimos_seis_meses)

        self.tela_principal.frame_vendas_ultimos_seis_meses.layout().addWidget(canvas)

    def total_faturado(self):
        cursor = self.conexao.get_cursor()
        comando = "select sum(valor_total) from vendas"
        cursor.execute(comando)
        resultado = cursor.fetchone()[0]
        try:
            self.tela_principal.label_faturamento.setText(f"R$ {resultado:.2f}")
        except TypeError:
            self.tela_principal.label_faturamento.setText("R$ 00,00")

    def produtos_mais_vendidos(self):
        cursor = self.conexao.get_cursor()

        comando = """
            SELECT e.nome_produto, SUM(iv.quantidade) AS total_vendido
            FROM estoque e
            JOIN itens_venda iv ON e.id_produto = iv.id_produto
            JOIN vendas v ON iv.id_venda = v.id_venda
            GROUP BY e.id_produto, e.nome_produto
            ORDER BY total_vendido DESC
            LIMIT 5
        """
        cursor.execute(comando)
        resultados = cursor.fetchall()

        produtos = []
        quantidades = []
        for nome_produto, total_vendido in resultados:
            produtos.append(nome_produto)
            quantidades.append(int(total_vendido) if total_vendido is not None else 0)

        if not produtos:
            if hasattr(self.tela_principal, 'label_produtos_mais_vendidos'):
                self.tela_principal.label_produtos_mais_vendidos.setText("Nenhum dado disponível")
            return

        fig, ax = plt.subplots(figsize=(6, 3), dpi=100)
        ax.barh(produtos, quantidades, color='#e76f51', edgecolor='#264653', linewidth=1.5)
        ax.set_xlim(0)
        ax.set_xlabel("Quantidade Vendida", fontsize=12, color='#495057')
        ax.set_facecolor('#f8f9fa')
        fig.patch.set_facecolor('#ffffff')
        ax.grid(True, linestyle='--', alpha=0.6, color='#adb5bd')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color('#dee2e6')
        ax.spines['bottom'].set_color('#dee2e6')
        plt.yticks(rotation=90)
        plt.tight_layout()

        if self.canvas_produtos is not None:
            layout = self.tela_principal.frame_produtos_mais_vendidos.layout()
            if layout is not None:
                layout.removeWidget(self.canvas_produtos)
                self.canvas_produtos.deleteLater()

        self.canvas_produtos = FigureCanvas(fig)
        layout = self.tela_principal.frame_produtos_mais_vendidos.layout()
        if layout is None:
            layout = QVBoxLayout(self.tela_principal.frame_produtos_mais_vendidos)
            self.tela_principal.frame_produtos_mais_vendidos.setLayout(layout)
        layout.addWidget(self.canvas_produtos)

