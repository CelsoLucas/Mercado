from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide6.QtWidgets import QVBoxLayout
from conexao_db import conexaoDB

class cmdRelatorios():
    def __init__(self, tela_principal):
        self.conexao = conexaoDB()
        self.tela_principal = tela_principal
    def vendas_ultimos_seis_meses(self):
        cursor = self.conexao.get_cursor()
        try:
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
            fig, ax = plt.subplots(figsize=(8, 5), dpi=100)
            
            # Estilizar a linha e os marcadores
            ax.plot(
                meses_completos, 
                valores_completos, 
                marker='o', 
                linestyle='-', 
                color='#2a9d8f',  # Verde azulado elegante
                linewidth=2.5, 
                markersize=8,
                markeredgecolor='#264653',  # Bordas escuras nos marcadores
                markeredgewidth=1.5
            )

            # Personalizar o fundo e bordas
            ax.set_facecolor('#f8f9fa')  # Fundo cinza claro
            fig.patch.set_facecolor('#ffffff')  # Fundo externo branco

            # Configurar títulos e rótulos
            ax.set_xlabel("Mês", fontsize=12, color='#495057')
            ax.set_ylabel("Total de Vendas (R$)", fontsize=12, color='#495057')

            # Estilizar a grade
            ax.grid(True, linestyle='--', alpha=0.6, color='#adb5bd')

            # Ajustar os ticks do eixo X
            plt.xticks(rotation=45, ha="right", fontsize=10, color='#495057')
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

        except Exception as e:
            print(f"Erro ao criar gráfico de vendas dos últimos 6 meses: {str(e)}")
            from PySide6.QtWidgets import QLabel
            label = QLabel("Erro ao carregar gráfico de vendas")
            if self.tela_principal.frame_vendas_ultimos_seis_meses.layout() is not None:
                while self.tela_principal.frame_vendas_ultimos_seis_meses.layout().count():
                    item = self.tela_principal.frame_vendas_ultimos_seis_meses.layout().takeAt(0)
                    widget = item.widget()
                    if widget is not None:
                        widget.deleteLater()
            else:
                QVBoxLayout(self.tela_principal.frame_vendas_ultimos_seis_meses)
            self.tela_principal.frame_vendas_ultimos_seis_meses.layout().addWidget(label)
        finally:
            cursor.close()