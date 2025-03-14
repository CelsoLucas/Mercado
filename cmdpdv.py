from conexao_db import conexaoDB
from PySide6.QtWidgets import QApplication, QScrollArea, QWidget, QVBoxLayout, QGridLayout, QLabel, QPushButton, QHBoxLayout, QMessageBox, QTreeWidgetItem, QLineEdit
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from time import sleep

class cmdPdv():
    def __init__(self, tela_principal):
        self.conexao = conexaoDB()
        self.tela_principal = tela_principal
        self.tela_principal.stackedWidget_2.setCurrentIndex(0)
        self.tela_principal.stackedWidget_6.setCurrentIndex(0)
        self.carrinho = []
        self.tela_principal.input_pdv_forma_pagamento.setCurrentIndex(-1)
        self.adc_card()
        self.mostrar_carrinho()
        self.tela_principal.input_pdv_forma_pagamento.currentTextChanged.connect(self.forma_pagamento)

    def adc_card(self):
        scroll_area = self.tela_principal.mostruario_cards2_2
        if not isinstance(scroll_area, QScrollArea):
            print("Erro: mostruario_cards2_2 não é um QScrollArea!")
            return

        content_widget = scroll_area.widget()
        if content_widget is None:
            content_widget = QWidget()
            scroll_area.setWidget(content_widget)
            scroll_area.setWidgetResizable(True)
            grid_layout = QGridLayout(content_widget)
        else:
            grid_layout = content_widget.layout()
            if grid_layout:
                while grid_layout.count():
                    item = grid_layout.takeAt(0)
                    if item.widget():
                        item.widget().deleteLater()
            else:
                grid_layout = QGridLayout(content_widget)

        cursor = self.conexao.get_cursor() 
        cursor.execute("SELECT id_produto, nome_produto, preco, imagem FROM estoque")
        produtos = cursor.fetchall()
        cursor.close()

        row = 0
        col = 0
        for produto in produtos:
            if isinstance(produto, dict):
                card = self.criar_card(produto)
            else:
                card = self.criar_card({
                    'id_produto': produto[0],
                    'nome_produto': produto[1],
                    'preco': produto[2],
                    'imagem': produto[3]
                })
            grid_layout.addWidget(card, row, col)
            col += 1
            if col > 2:  
                col = 0
                row += 1

    def criar_card(self, produto):
        card = QWidget()
        card.setFixedSize(175, 300) 
        layout = QVBoxLayout(card)
        layout.setAlignment(Qt.AlignCenter)

        imagem_label = QLabel()
        pixmap = QPixmap(produto['imagem'])  
        if pixmap.isNull():
            pixmap = QPixmap("default_image.png")  

        pixmap = pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        imagem_label.setPixmap(pixmap)
        imagem_label.setAlignment(Qt.AlignCenter) 
        layout.addWidget(imagem_label)

        nome_label = QLabel(produto['nome_produto'])
        nome_label.setAlignment(Qt.AlignCenter)
        nome_label.setWordWrap(True)  
        nome_label.setStyleSheet("font-size: 12px;")  
        layout.addWidget(nome_label)

        preco_label = QLabel(f"R$ {produto['preco']:.2f}")
        preco_label.setAlignment(Qt.AlignCenter)
        preco_label.setStyleSheet("font-size: 12px; font-weight: bold;")
        layout.addWidget(preco_label)

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
        cursor = self.conexao.get_cursor()
        comando = "select id_produto, nome_produto, preco, quantidade, categoria from estoque where nome_produto = %s"
        cursor.execute(comando, (nome_produto,))
        resultado = cursor.fetchone()
        self.id, self.nome, self.preco, self.quantidade, self.categoria = resultado
        print(self.categoria)
        if self.categoria == "HortiFruti" or self.categoria == 2:
            self.tela_principal.stackedWidget_2.setCurrentIndex(2)
            self.tela_principal.txt_pdv_nome_2.setText(f"{self.nome}")
            self.tela_principal.txt_pdv_valor_2.setText(f"R$ {self.preco} Kg")
            self.tela_principal.input_pdv_quant_2.setText("00.00")
        else:
            self.tela_principal.stackedWidget_2.setCurrentIndex(1)
            self.tela_principal.txt_pdv_nome.setText(f"{self.nome}")
            self.tela_principal.txt_pdv_valor.setText(f"R$ {self.preco} Un.")
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
        if self.categoria == "HortiFruti" or self.categoria == 2:
            quantidade = float(self.tela_principal.input_pdv_quant_2.text())
        else:
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
        self.tabela = self.tela_principal.tabela_carrinho
        
        self.tabela.clear()
        
        if self.tabela.columnCount() != 4:
            print("Erro: O QTreeWidget deve ter 4 colunas (Nome, Preço, Quantidade, Total)")
            return
        
        self.total_geral = 0
        
        for item in self.carrinho:
            nome = item[0]
            preco = float(item[1]) 
            quantidade = float(item[2])  
            total_item = preco * quantidade  
            self.total_geral += total_item  
            
            linha = QTreeWidgetItem([nome, str(quantidade), f"R$ {preco:.2f}", f"R$ {total_item:.2f}"])
            self.tabela.addTopLevelItem(linha)
        
        for i in range(4):
            self.tabela.resizeColumnToContents(i)
        
        self.tela_principal.txt_valor_total.setText(f"R$ {self.total_geral:.2f}")
    
    def forma_pagamento(self):

        forma = self.tela_principal.input_pdv_forma_pagamento.currentText()
        frame = self.tela_principal.frame_pagamento
        
        while frame.layout() and frame.layout().count():
            item = frame.layout().takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        if forma == "Pix":
            qr_label = QLabel()
            pixmap = QPixmap("imgs/qrcode.png")
            pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            qr_label.setPixmap(pixmap)
            qr_label.setAlignment(Qt.AlignCenter)
            frame.layout().addWidget(qr_label)
        elif forma == "Dinheiro":
            self.dinheiro_input = QLineEdit()
            self.dinheiro_input.setPlaceholderText("Digite o valor em dinheiro")
            self.dinheiro_input.setStyleSheet("font-size: 14px; padding: 5px;")
            self.dinheiro_input.setMaximumWidth(200) 
            
            frame.layout().addWidget(self.dinheiro_input)

    def finalizar_compra(self):

        if self.carrinho == []:
            QMessageBox.warning(None, "error", "Carrinho está Vazio!")
            return

        if self.tela_principal.input_pdv_forma_pagamento.currentText() == "Dinheiro":
            if float(self.dinheiro_input.text()) < self.total_geral:
                QMessageBox.warning(None, "error", "Quantidade de dinheiro menor que o total")
                return
                
            elif float(self.dinheiro_input.text()) > self.total_geral:
                troco = float(self.dinheiro_input.text()) - self.total_geral
                self.dinheiro_txt = QLabel()
                self.dinheiro_txt.setText(f"Troco: R$ {troco:.2f}")
                self.dinheiro_txt.setStyleSheet("font-size: 14px; padding: 5px;")
                self.dinheiro_txt.setMaximumWidth(200) 
                frame = self.tela_principal.frame_pagamento
                frame.layout().addWidget(self.dinheiro_txt)

            else:
                troco = float(self.dinheiro_input.text()) - self.total_geral
                self.dinheiro_txt = QLabel()
                self.dinheiro_txt.setText(f"Troco: R$ {troco:.2f}")
                self.dinheiro_txt.setStyleSheet("font-size: 14px; padding: 5px;")
                self.dinheiro_txt.setMaximumWidth(200) 
                frame = self.tela_principal.frame_pagamento
                frame.layout().addWidget(self.dinheiro_txt)


        
        cursor = self.conexao.get_cursor()
        comando = "select id_usuario from usuarios where nome = %s"
        cursor.execute(comando, (self.tela_principal.txt_ola_user.text(), ))
        id_user = cursor.fetchone()[0]
        cursor = self.conexao.get_cursor()
        comando = "select id_forma_pagamento from formapagamento where forma_pagamento = %s"
        cursor.execute(comando, (self.tela_principal.input_pdv_forma_pagamento.currentText(), ))
        id_forma_pagamento = cursor.fetchone()[0]

        comando = """insert into vendas (id_usuario, valor_total, id_forma_pagamento)
                     values (%s, %s, %s)"""
        valores = (int(id_user), float(self.total_geral), int(id_forma_pagamento))
        cursor.execute(comando, valores)
        self.conexao.commit()

        comando = "SELECT id_venda FROM vendas ORDER BY id_venda DESC LIMIT 1"
        cursor.execute(comando)
        id_venda = cursor.fetchone()[0]

        for i in self.carrinho:
            nome = i[0]
            preco = i[1]
            quantidade = i[2]

            cursor = self.conexao.get_cursor()
            comando = "select id_produto from estoque where nome_produto = %s"
            cursor.execute(comando, (nome,))
            id_produto = cursor.fetchone()[0]

            comando = """insert into itens_venda (id_venda, id_produto, quantidade, preco_unitario, subtotal)
                         values (%s, %s, %s, %s, %s)"""
            valores = (int(id_venda), int(id_produto), float(quantidade), float(preco), float(float(quantidade) * float(preco)))
            cursor.execute(comando, valores)
            self.conexao.commit()

            comando = "select quantidade from estoque where nome_produto = %s"
            cursor.execute(comando, (nome, ))
            quantidade_estoque = cursor.fetchone()[0]

            comando = "update estoque set quantidade = %s where nome_produto = %s"
            valores = (quantidade_estoque - quantidade, nome)
            cursor.execute(comando, valores)
            self.conexao.commit()

        QMessageBox.information(None, "Sucesso", "Obrigado por Comprar no Mercado do Celsadas")
        self.tabela.clear()
        self.tela_principal.txt_valor_total.setText("R$ 00,00")
        self.tela_principal.input_pdv_forma_pagamento.setCurrentIndex(-1)
        self.carrinho = []

