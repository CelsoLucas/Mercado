from conexao_db import conexaoDB
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide6.QtWidgets import QVBoxLayout

class cmdRelatorios():
    def __init__(self, tela_principal):
        self.conexao = conexaoDB()
        self.tela_principal = tela_principal
        self.vendas_ultimos_seis_meses()
        self.faturamento()
        self.produtos_mais_vendidos()
        self.vendas_por_forma_pagamento()

        
    def vendas_ultimos_seis_meses(self):
        cursor = None
        try:
            # Obter cursor da conexão
            cursor = self.conexao.get_cursor()

            # Query para pegar as vendas dos últimos 6 meses agrupadas por mês
            query = """
                SELECT 
                    DATE_FORMAT(data_venda, '%Y-%m') as mes,
                    SUM(valor_total) as total_vendas
                FROM vendas
                WHERE data_venda >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
                GROUP BY DATE_FORMAT(data_venda, '%Y-%m')
                ORDER BY mes ASC
            """
            cursor.execute(query)
            resultados = cursor.fetchall()

            # Processar os dados
            meses = []
            vendas = []
            for mes, total in resultados:
                meses.append(mes)
                vendas.append(float(total))

            # Se não houver dados, criar dados zerados para 6 meses
            if not meses:
                hoje = datetime.now()
                meses = [(hoje - timedelta(days=i*30)).strftime('%Y-%m') 
                        for i in range(5, -1, -1)]
                vendas = [0] * 6

            # Criar o gráfico de barras
            fig = plt.figure(figsize=(8, 4))
            plt.bar(meses, vendas, color='skyblue')  # Alterado para gráfico de barras
            
            # Configurações do gráfico
            plt.ylabel('Total de Vendas (R$)')
            plt.ylim(0, max(vendas) * 1.1 if vendas else 100)  # Y começa em 0 até 110% do máximo
            plt.grid(True, linestyle='--', alpha=0.7, axis='y')  # Grade apenas no eixo Y
            
            # Ajustar layout do gráfico
            plt.tight_layout()

            # Obter o frame da tela principal
            frame = self.tela_principal.frame_vendas_ultimos_seis_meses
            
            # Criar ou obter o layout do frame
            layout = frame.layout()
            if layout is None:
                layout = QVBoxLayout(frame)
            else:
                # Limpar o layout existente antes de adicionar o novo gráfico
                while layout.count():
                    item = layout.takeAt(0)
                    widget = item.widget()
                    if widget is not None:
                        widget.deleteLater()

            # Criar canvas para PySide6 (Qt)
            canvas = FigureCanvas(fig)
            
            # Adicionar o canvas ao layout
            layout.addWidget(canvas)
            canvas.draw()

        except Exception as err:
            print(f"Erro: {err}")
        finally:
            if cursor is not None:
                cursor.close()
    
    def faturamento(self):
        cursor = self.conexao.get_cursor()
        comando = "select sum(valor_total) from vendas"
        cursor.execute(comando)
        resultado = cursor.fetchone()[0]

        self.tela_principal.label_faturamento.setText(f"R$ {resultado:.2f}")

    def produtos_mais_vendidos(self):
        cursor = None
        try:
            # Obter cursor da conexão
            cursor = self.conexao.get_cursor()

            # Query para pegar os 5 produtos mais vendidos
            query = """
                SELECT 
                    e.nome_produto,
                    SUM(iv.quantidade) as total_vendido
                FROM itens_venda iv
                JOIN estoque e ON iv.id_produto = e.id_produto
                GROUP BY iv.id_produto, e.nome_produto
                ORDER BY total_vendido DESC
                LIMIT 5
            """
            cursor.execute(query)
            resultados = cursor.fetchall()

            # Processar os dados
            produtos = []
            quantidades = []
            for nome, total in resultados:
                produtos.append(nome)
                quantidades.append(int(total))

            # Se não houver dados, usar valores fictícios
            if not produtos:
                produtos = ["Produto 1", "Produto 2", "Produto 3", "Produto 4", "Produto 5"]
                quantidades = [0, 0, 0, 0, 0]

            # Criar o gráfico de barras
            fig = plt.figure(figsize=(8, 4))
            plt.bar(produtos, quantidades, color='skyblue')
            
            # Configurações do gráfico
            plt.ylabel('Quantidade Vendida')
            plt.ylim(0, max(quantidades) * 1.1 if quantidades else 10)  # Y começa em 0 até 110% do máximo
            plt.xticks(rotation=45, ha='right')  # Rotacionar nomes para melhor legibilidade
            plt.grid(True, linestyle='--', alpha=0.7, axis='y')  # Grade apenas no eixo Y
            
            # Ajustar layout do gráfico
            plt.tight_layout()

            # Obter o frame da tela principal
            frame = self.tela_principal.frame_produtos_mais_vendidos  # Reutilizando o mesmo frame
            
            # Criar ou obter o layout do frame
            layout = frame.layout()
            if layout is None:
                layout = QVBoxLayout(frame)
            else:
                # Limpar o layout existente antes de adicionar o novo gráfico
                while layout.count():
                    item = layout.takeAt(0)
                    widget = item.widget()
                    if widget is not None:
                        widget.deleteLater()

            # Criar canvas para PySide6 (Qt)
            canvas = FigureCanvas(fig)
            
            # Adicionar o canvas ao layout
            layout.addWidget(canvas)
            canvas.draw()

        except Exception as err:
            print(f"Erro: {err}")
        finally:
            if cursor is not None:
                cursor.close()

    def vendas_por_forma_pagamento(self):
        cursor = None
        try:
            # Obter cursor da conexão
            cursor = self.conexao.get_cursor()

            # Query para contar vendas por forma de pagamento
            query = """
                SELECT 
                    fp.forma_pagamento,
                    COUNT(v.id_venda) as total_vendas
                FROM vendas v
                LEFT JOIN formapagamento fp ON v.id_forma_pagamento = fp.id_forma_pagamento
                GROUP BY fp.id_forma_pagamento, fp.forma_pagamento
            """
            cursor.execute(query)
            resultados = cursor.fetchall()

            # Processar os dados
            formas_pagamento = []
            quantidades = []
            for forma, total in resultados:
                formas_pagamento.append(forma if forma else "Não especificado")
                quantidades.append(int(total))

            # Se não houver dados, usar valores fictícios
            if not formas_pagamento:
                formas_pagamento = ["Nenhuma venda registrada"]
                quantidades = [0]

            # Criar o gráfico de barras
            fig = plt.figure(figsize=(8, 4))
            plt.bar(formas_pagamento, quantidades, color='lightgreen')
            
            # Configurações do gráfico
            plt.title('Vendas por Forma de Pagamento')
            plt.xlabel('Forma de Pagamento')
            plt.ylabel('Quantidade de Vendas')
            plt.ylim(0, max(quantidades) * 1.1 if quantidades else 10)  # Y começa em 0 até 110% do máximo
            plt.grid(True, linestyle='--', alpha=0.7, axis='y')  # Grade apenas no eixo Y
            plt.xticks(rotation=45, ha='right')  # Rotacionar rótulos para melhor legibilidade
            
            # Ajustar layout do gráfico
            plt.tight_layout()

            # Obter o frame da tela principal
            frame = self.tela_principal.frame_formas_pagamento
            
            # Criar ou obter o layout do frame
            layout = frame.layout()
            if layout is None:
                layout = QVBoxLayout(frame)
            else:
                # Limpar o layout existente antes de adicionar o novo gráfico
                while layout.count():
                    item = layout.takeAt(0)
                    widget = item.widget()
                    if widget is not None:
                        widget.deleteLater()

            # Criar canvas para PySide6 (Qt)
            canvas = FigureCanvas(fig)
            
            # Adicionar o canvas ao layout
            layout.addWidget(canvas)
            canvas.draw()

        except Exception as err:
            print(f"Erro: {err}")
        finally:
            if cursor is not None:
                cursor.close()