from conexao_db import conexaoDB
from PySide6.QtWidgets import QApplication, QScrollArea, QWidget, QVBoxLayout, QGridLayout, QLabel, QPushButton, QHBoxLayout, QMessageBox, QTreeWidgetItem, QLineEdit
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import qrcode

class cmdPdv():
    def __init__(self, tela_principal):
        self.conexao = conexaoDB()
        self.tela_principal = tela_principal
        self.tela_principal.stackedWidget_2.setCurrentIndex(0)
        self.tela_principal.stackedWidget_6.setCurrentIndex(0)
        self.carrinho = []
        self.adc_card()
        self.mostrar_carrinho()
        self.tela_principal.input_pdv_forma_pagamento.currentTextChanged.connect(self.forma_pagamento)

    def adc_card(self):
        # Obter o QScrollArea (mostruario_cards2_2)
        scroll_area = self.tela_principal.mostruario_cards2_2
        if not isinstance(scroll_area, QScrollArea):
            print("Erro: mostruario_cards2_2 não é um QScrollArea!")
            return

        # Criar o widget interno para o ScrollArea (apenas se necessário)
        content_widget = scroll_area.widget()
        if content_widget is None:
            content_widget = QWidget()
            scroll_area.setWidget(content_widget)
            scroll_area.setWidgetResizable(True)

        # Criar ou substituir o QGridLayout
        existing_layout = content_widget.layout()
        if existing_layout:
            # Remover o layout existente
            for i in reversed(range(existing_layout.count())):
                item = existing_layout.takeAt(i)
                if item.widget():
                    item.widget().deleteLater()
            content_widget.setLayout(None)  # Limpar o layout existente
        grid_layout = QGridLayout(content_widget)
        content_widget.setLayout(grid_layout)

        # Buscar produtos do banco de dados
        cursor = self.conexao.get_cursor()  # Garantir que o cursor retorna dicionários
        cursor.execute("SELECT id_produto, nome_produto, preco, imagem FROM estoque")
        produtos = cursor.fetchall()
        cursor.close()

        # Adicionar cards ao grid layout (3 colunas)
        row = 0
        col = 0
        for produto in produtos:
            # Verificar se o produto é um dicionário ou tupla
            if isinstance(produto, dict):
                card = self.criar_card(produto)
            else:
                # Se for tupla, mapear índices para colunas
                card = self.criar_card({
                    'id_produto': produto[0],
                    'nome_produto': produto[1],
                    'preco': produto[2],
                    'imagem': produto[3]
                })
            grid_layout.addWidget(card, row, col)
            col += 1
            if col > 2:  # Limite de 3 colunas por linha
                col = 0
                row += 1

    def criar_card(self, produto):
        # Widget personalizado para cada card
        card = QWidget()
        card.setFixedSize(175, 300)  # Tamanho fixo do card
        layout = QVBoxLayout(card)
        layout.setAlignment(Qt.AlignCenter)

        # Exibir a imagem do produto
        imagem_label = QLabel()
        pixmap = QPixmap(produto['imagem'])  # Certifique-se de que o caminho da imagem esteja correto
        if pixmap.isNull():
            pixmap = QPixmap("default_image.png")  # Imagem padrão caso a imagem não seja carregada
        # Redimensionar a imagem para 160x160, mantendo a proporção
        pixmap = pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        imagem_label.setPixmap(pixmap)
        imagem_label.setAlignment(Qt.AlignCenter)  # Garantir que a imagem esteja centralizada no QLabel
        layout.addWidget(imagem_label)

        # Nome do produto
        nome_label = QLabel(produto['nome_produto'])
        nome_label.setAlignment(Qt.AlignCenter)
        nome_label.setWordWrap(True)  # Permitir quebra de texto
        nome_label.setStyleSheet("font-size: 12px;")  # Ajustar o tamanho da fonte
        layout.addWidget(nome_label)

        # Preço do produto
        preco_label = QLabel(f"R$ {produto['preco']:.2f}")
        preco_label.setAlignment(Qt.AlignCenter)
        preco_label.setStyleSheet("font-size: 12px; font-weight: bold;")  # Ajustar o tamanho e estilo da fonte
        layout.addWidget(preco_label)

        # Botão Comprar
        comprar_button = QPushButton("Comprar")
        comprar_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 5px;
                border-radius: 3px;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        comprar_button.clicked.connect(lambda: self.escolher_quant(produto['nome_produto']))
        layout.addWidget(comprar_button)

        card.setStyleSheet("""
            QWidget {
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 10px;
                margin: 5px;
                background-color: white;
            }
        """)
        return card

    def escolher_quant(self, nome_produto):
        self.tela_principal.stackedWidget_2.setCurrentIndex(1)
        cursor = self.conexao.get_cursor()
        comando = "select id_produto, nome_produto, preco, quantidade from estoque where nome_produto = %s"
        cursor.execute(comando, (nome_produto,))
        resultado = cursor.fetchone()
        self.id, self.nome, self.preco, self.quantidade = resultado

        self.tela_principal.txt_pdv_nome.setText(f"{self.nome}")
        self.tela_principal.txt_pdv_valor.setText(f"{self.preco}")
        self.tela_principal.input_pdv_quant.setText("1")

    def menos(self):
        if int(self.tela_principal.input_pdv_quant.text()) <= 1:
            QMessageBox.warning(None, "error", "Quantidade Minima é 0")
            self.tela_principal.input_pdv_quant.setText("1")
            return
        else:
            cont = int(self.tela_principal.input_pdv_quant.text()) - 1
            self.tela_principal.input_pdv_quant.setText(f"{cont}")

    def mais(self):
        if int(self.tela_principal.input_pdv_quant.text()) >= self.quantidade:
            QMessageBox.warning(None, "error", f"Quantidade Maxima é {self.quantidade}")
            self.tela_principal.input_pdv_quant.setText("1")
            return
        else:
            cont = int(self.tela_principal.input_pdv_quant.text()) + 1
            self.tela_principal.input_pdv_quant.setText(f"{cont}")
    
    def adc_carrinho(self):
        quantidade = int(self.tela_principal.input_pdv_quant.text())
        if quantidade <= 0:
            QMessageBox.warning(None, "error", "Quantidade Minima é 0")
            return
        elif quantidade > self.quantidade:
            QMessageBox.warning(None, "error", f"Quantidade Maxima é {self.quantidade}")
            return
        self.suporte_carrinho = []
        self.carrinho.append(self.suporte_carrinho)
        self.suporte_carrinho.append(self.nome)
        self.suporte_carrinho.append(self.preco)
        self.suporte_carrinho.append(quantidade)
        print(self.carrinho)
        self.tela_principal.stackedWidget_2.setCurrentIndex(0)
        self.mostrar_carrinho()


    def mostrar_carrinho(self):
        # Referência ao QTreeWidget
        tabela = self.tela_principal.tabela_carrinho
        
        # Limpar o conteúdo atual da tabela, mantendo os cabeçalhos
        tabela.clear()
        
        # Verificar se o número de colunas está correto (deve ser 4 agora)
        if tabela.columnCount() != 4:
            print("Erro: O QTreeWidget deve ter 4 colunas (Nome, Preço, Quantidade, Total)")
            return
        
        total_geral = 0
        
        for item in self.carrinho:
            nome = item[0]
            preco = float(item[1]) 
            quantidade = int(item[2])  
            total_item = preco * quantidade  
            total_geral += total_item  
            
            linha = QTreeWidgetItem([nome, f"R$ {preco:.2f}", str(quantidade), f"R$ {total_item:.2f}"])
            tabela.addTopLevelItem(linha)
        
        for i in range(4):
            tabela.resizeColumnToContents(i)
        
        self.tela_principal.txt_valor_total.setText(f"{total_geral}")
    
    def forma_pagamento(self):
        forma = self.tela_principal.input_pdv_forma_pagamento.currentText()
        frame = self.tela_principal.frame_pagamento
        
        while frame.layout() and frame.layout().count():
            item = frame.layout().takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        if forma == "Pix":
            pass
            # img = QLabel()
            # pixmap = QPixmap("")
            # frame.layout().addWidget(dinheiro_input)
        elif forma == "Dinheiro":
            dinheiro_input = QLineEdit()
            dinheiro_input.setPlaceholderText("Digite o valor em dinheiro")
            dinheiro_input.setStyleSheet("font-size: 14px; padding: 5px;")
            dinheiro_input.setMaximumWidth(200) 
            
            frame.layout().addWidget(dinheiro_input)
        else:
            pass

