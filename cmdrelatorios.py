import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from conexao_db import conexaoDB

class cmdRelatorios():
    def __init__(self):
        self.conexao = conexaoDB()
    
    def mostrar_relatorios(self):
        # Mudar para a tela de relatórios
        self.ui.stackedWidget.setCurrentIndex(3)
        
        # Conectar ao banco de dados e buscar os dados
        cursor = self.conexao.get_cursor()

        # Executar a consulta SQL
        query = """
        SELECT 
            YEAR(data_venda) AS ano,
            MONTH(data_venda) AS mes,
            SUM(valor_total) AS total_vendas
        FROM 
            vendas
        WHERE 
            data_venda >= DATE_SUB('2025-02-28', INTERVAL 6 MONTH)
        GROUP BY 
            YEAR(data_venda), MONTH(data_venda)
        ORDER BY 
            ano DESC, mes DESC;
        """
        cursor.execute(query)
        resultados = cursor.fetchall()

        # Fechar a conexão
        cursor.close()
        self.conexao.close()

        # Processar os dados
        meses = []
        vendas = []
        meses_nome = {
            1: 'Jan', 2: 'Fev', 3: 'Mar', 4: 'Abr', 5: 'Mai', 6: 'Jun',
            7: 'Jul', 8: 'Ago', 9: 'Set', 10: 'Out', 11: 'Nov', 12: 'Dez'
        }

        for ano, mes, total in resultados:
            meses.append(f"{meses_nome[mes]}/{str(ano)[-2:]}")
            vendas.append(float(total))

        # Criar o gráfico
        fig, ax = plt.subplots(figsize=(6, 4))  # Ajustar o tamanho para caber na label
        ax.plot(meses, vendas, marker='o', linestyle='-', color='b', label='Vendas')
        ax.set_title('Vendas dos Últimos 6 Meses', fontsize=12)
        ax.set_xlabel('Mês/Ano', fontsize=10)
        ax.set_ylabel('Total de Vendas (R$)', fontsize=10)
        ax.grid(True)
        ax.legend()

        # Adicionar rótulos aos pontos
        for i, venda in enumerate(vendas):
            ax.text(meses[i], venda, f'R$ {venda:.2f}', ha='center', va='bottom', fontsize=8)

        # Integrar o gráfico na label_vendas_ultimos_6_meses
        canvas = FigureCanvas(fig)
        self.ui.label_vendas_ultimos_6_meses.setMinimumSize(600, 400)  # Ajustar tamanho mínimo
        layout = self.ui.label_vendas_ultimos_6_meses.layout()
        if layout is not None:
            # Limpar layout existente, se houver
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
        else:
            # Criar um novo layout se não existir
            from PySide6.QtWidgets import QVBoxLayout
            layout = QVBoxLayout(self.ui.label_vendas_ultimos_6_meses)
        
        layout.addWidget(canvas)
        canvas.draw()