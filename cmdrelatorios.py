import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide6.QtWidgets import QVBoxLayout
from datetime import datetime
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
                # Converter ano e mês para formato legível (ex.: "Out/2024")
                data = datetime(ano, mes, 1)
                meses.append(data.strftime("%b/%Y"))  # Ex.: "Out/2024"
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

            # Criar o gráfico
            fig, ax = plt.subplots(figsize=(6, 4))  # Ajuste o tamanho conforme o frame
            ax.plot(meses_completos, valores_completos, marker='o', linestyle='-', color='b')
            ax.set_title("Vendas dos Últimos 6 Meses")
            ax.set_xlabel("Mês")
            ax.set_ylabel("Total de Vendas (R$)")
            ax.grid(True)
            plt.xticks(rotation=45, ha="right")
            plt.tight_layout()

            # Integrar o gráfico ao frame existente
            canvas = FigureCanvas(fig)

            # Limpar o layout existente do frame (se houver) e adicionar o gráfico
            if self.tela_principal.frame_vendas_ultimos_seis_meses.layout() is not None:
                # Remover widgets existentes no layout
                while self.tela_principal.frame_vendas_ultimos_seis_meses.layout().count():
                    item = self.tela_principal.frame_vendas_ultimos_seis_meses.layout().takeAt(0)
                    widget = item.widget()
                    if widget is not None:
                        widget.deleteLater()
            else:
                # Se não houver layout, criar um novo
                QVBoxLayout(self.tela_principal.frame_vendas_ultimos_seis_meses)

            self.tela_principal.frame_vendas_ultimos_seis_meses.layout().addWidget(canvas)

        except Exception as e:
            print(f"Erro ao criar gráfico de vendas dos últimos 6 meses: {str(e)}")
            # Em caso de erro, exibir mensagem no frame
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