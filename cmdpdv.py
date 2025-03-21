from conexao_db import conexaoDB
from PySide6.QtWidgets import QApplication, QScrollArea, QWidget, QVBoxLayout, QGridLayout, QLabel, QPushButton, QHBoxLayout, QMessageBox, QTreeWidgetItem, QLineEdit, QInputDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class cmdPdv():
    def __init__(self, tela_principal):
        self.conexao = conexaoDB()
        self.tela_principal = tela_principal
        self.tela_principal.stackedWidget_2.setCurrentIndex(0)
        self.tela_principal.stackedWidget_6.setCurrentIndex(0)
        self.carrinho = []
        self.tela_principal.input_pdv_forma_pagamento.setCurrentIndex(-1)
        self.tela_principal.input_pdv_produto.textChanged.connect(self.filtrar_produtos_pesquisa)
        self.tela_principal.input_pdv_categoria.currentTextChanged.connect(self.filtrar_produtos_categorias)
        self.adc_card_normal()
        self.adc_card_pesquisa()
        self.adc_card_cat()
        self.mostrar_carrinho()
        self.carregar_categorias()
        self.tela_principal.input_pdv_produto.setText("")
        self.tela_principal.input_pdv_forma_pagamento.currentTextChanged.connect(self.forma_pagamento)

    def carregar_categorias(self):
        cursor = self.conexao.get_cursor()
        comando = "select nome_categoria from categorias"
        cursor.execute(comando)
        resultado = cursor.fetchall()
        self.tela_principal.input_pdv_categoria.clear()
        for i in range(len(resultado)):
            categoria = resultado[i][0]
            self.tela_principal.input_pdv_categoria.addItem(f"{categoria}")
        
        self.tela_principal.input_pdv_categoria.setCurrentIndex(-1) 
        cursor.close()

    def adc_card_pesquisa(self):
        self.filtrar_produtos_pesquisa("")
        

    def adc_card_cat(self):
        self.filtrar_produtos_categorias() 

    def adc_card_normal(self):
        self.filtrar_produtos_normal(f"") 


    def filtrar_produtos_normal(self, texto):
        # Pegar a "vitrine" onde os cards aparecem
        scroll_area = self.tela_principal.mostruario_cards2_2
        content_widget = scroll_area.widget()  # Isso é como uma folha em branco onde os cards ficam

        # Limpar tudo que estava na vitrine antes
        if content_widget and content_widget.layout():  # Se já tem algo desenhado...
            grid_layout = content_widget.layout()  # A "grade" onde os cards estão arrumados
            while grid_layout.count():  # Enquanto tiver cards...
                item = grid_layout.takeAt(0)  # Pega um card
                if item.widget():  # Se for realmente um card...
                    item.widget().deleteLater()  # Apaga ele da tela
        else:
            # Se a vitrine estava vazia, cria uma nova folha em branco
            content_widget = QWidget()
            scroll_area.setWidget(content_widget)
            scroll_area.setWidgetResizable(True)
            grid_layout = QGridLayout(content_widget)  # Faz uma grade nova

        cursor = self.conexao.get_cursor()
        comando = "select id_produto, nome_produto, preco, imagem from estoque where nome_produto like %s"
        cursor.execute(comando, (f"%{texto}%",))
        produtos = cursor.fetchall()
        cursor.close()

        row = 0
        col = 0
        for produto in produtos:
            card = self.criar_card({
                'id_produto' : produto[0],
                'nome_produto' : produto[1],
                'preco' : produto[2],
                'imagem' : produto[3]
            })
            grid_layout.addWidget(card, row, col)
            col += 1
            if col > 2:
                col = 0
                row += 1

        # Se não achar nada, mostrar um aviso
        if not produtos:  # Se a lista estiver vazia...
            sem_resultados = QLabel("Nenhum produto encontrado.")  # Cria um texto
            sem_resultados.setAlignment(Qt.AlignCenter)  # Coloca no meio
            sem_resultados.setStyleSheet("font-size: 14px; color: gray;")  # Deixa bonitinho
            grid_layout.addWidget(sem_resultados, 0, 0, 1, 3)  # Mostra na grade

    def filtrar_produtos_pesquisa(self, texto):
        # Pegar a "vitrine" onde os cards aparecem
        scroll_area = self.tela_principal.mostruario_cards2_2
        content_widget = scroll_area.widget()  # Isso é como uma folha em branco onde os cards ficam

        # Limpar tudo que estava na vitrine antes
        if content_widget and content_widget.layout():  # Se já tem algo desenhado...
            grid_layout = content_widget.layout()  # A "grade" onde os cards estão arrumados
            while grid_layout.count():  # Enquanto tiver cards...
                item = grid_layout.takeAt(0)  # Pega um card
                if item.widget():  # Se for realmente um card...
                    item.widget().deleteLater()  # Apaga ele da tela
        else:
            # Se a vitrine estava vazia, cria uma nova folha em branco
            content_widget = QWidget()
            scroll_area.setWidget(content_widget)
            scroll_area.setWidgetResizable(True)
            grid_layout = QGridLayout(content_widget)  # Faz uma grade nova

        cursor = self.conexao.get_cursor()
        comando = "select id_produto, nome_produto, preco, imagem from estoque where nome_produto like %s"
        cursor.execute(comando, (f"%{texto}%",))
        produtos = cursor.fetchall()
        cursor.close()

        row = 0
        col = 0
        for produto in produtos:
            card = self.criar_card({
                'id_produto' : produto[0],
                'nome_produto' : produto[1],
                'preco' : produto[2],
                'imagem' : produto[3]
            })
            grid_layout.addWidget(card, row, col)
            col += 1
            if col > 2:
                col = 0
                row += 1

        # Se não achar nada, mostrar um aviso
        if not produtos:  # Se a lista estiver vazia...
            sem_resultados = QLabel("Nenhum produto encontrado.")  # Cria um texto
            sem_resultados.setAlignment(Qt.AlignCenter)  # Coloca no meio
            sem_resultados.setStyleSheet("font-size: 14px; color: gray;")  # Deixa bonitinho
            grid_layout.addWidget(sem_resultados, 0, 0, 1, 3)  # Mostra na grade

    def filtrar_produtos_categorias(self):
        
        if self.tela_principal.input_pdv_categoria.currentIndex() == -1:
            return
        else:
            # Pegar a "vitrine" onde os cards aparecem
            scroll_area = self.tela_principal.mostruario_cards2_2
            content_widget = scroll_area.widget()  # Isso é como uma folha em branco onde os cards ficam

            # Limpar tudo que estava na vitrine antes
            if content_widget and content_widget.layout():  # Se já tem algo desenhado...
                grid_layout = content_widget.layout()  # A "grade" onde os cards estão arrumados
                while grid_layout.count():  # Enquanto tiver cards...
                    item = grid_layout.takeAt(0)  # Pega um card
                    if item.widget():  # Se for realmente um card...
                        item.widget().deleteLater()  # Apaga ele da tela
            else:
                # Se a vitrine estava vazia, cria uma nova folha em branco
                content_widget = QWidget()
                scroll_area.setWidget(content_widget)
                scroll_area.setWidgetResizable(True)
                grid_layout = QGridLayout(content_widget)  # Faz uma grade nova

            cursor = self.conexao.get_cursor()
            comando = "select id_categorias from categorias where nome_categoria = %s "
            filtro_cat = self.tela_principal.input_pdv_categoria.currentText()
            if filtro_cat == "" or filtro_cat == None:
                return
            cursor.execute(comando, (filtro_cat, ))
            id_categoria = cursor.fetchone()[0]
            comando = "select id_produto, nome_produto, preco, imagem from estoque where categoria = %s"
            cursor.execute(comando, (id_categoria, ))
            produtos = cursor.fetchall()
            cursor.close()

            row = 0
            col = 0
            for produto in produtos:
                card = self.criar_card({
                    'id_produto' : produto[0],
                    'nome_produto' : produto[1],
                    'preco' : produto[2],
                    'imagem' : produto[3]
                })
                grid_layout.addWidget(card, row, col)
                col += 1
                if col > 2:
                    col = 0
                    row += 1

            # Se não achar nada, mostrar um aviso
            if not produtos:  # Se a lista estiver vazia...
                sem_resultados = QLabel("Nenhum produto encontrado.")  # Cria um texto
                sem_resultados.setAlignment(Qt.AlignCenter)  # Coloca no meio
                sem_resultados.setStyleSheet("font-size: 14px; color: gray;")  # Deixa bonitinho
                grid_layout.addWidget(sem_resultados, 0, 0, 1, 3)  # Mostra na grade

    def criar_card(self, produto):
        card = QWidget()
        card.setFixedSize(175, 300) 
        layout = QVBoxLayout(card)
        layout.setAlignment(Qt.AlignCenter)

        imagem_label = QLabel()
        if produto['imagem'] is None:
            pixmap = QPixmap("imgs/foto_produtos/produto_sem_imagem.png")
        else:
            pixmap = QPixmap(produto['imagem'])  
        if pixmap.isNull():
            pixmap = QPixmap("imgs/foto_produtos/produto_sem_imagem.png")  

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
        comando = "select id_produto, nome_produto, preco, quantidade, categoria, tipo_valor from estoque where nome_produto = %s"
        cursor.execute(comando, (nome_produto,))
        resultado = cursor.fetchone()
        self.id, self.nome, self.preco, self.quantidade, self.categoria, self.tipo_valor = resultado

        comando = "select nome_categoria from categorias where id_categorias = %s"
        cursor.execute(comando, (self.categoria, ))
        self.categoria = cursor.fetchone()[0]

        if self.tipo_valor == "1":
            self.tela_principal.stackedWidget_2.setCurrentIndex(2)
            self.tela_principal.txt_pdv_nome_2.setText(f"{self.nome}")
            self.tela_principal.txt_pdv_valor_2.setText(f"R$ {self.preco} Kg")
            self.tela_principal.input_pdv_quant_2.setPlaceholderText("0.00")
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

        if self.tipo_valor == "1":
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

            comando = """insert into itens_venda (id_venda, id_produto_pedido, quantidade_pedido, preco_unitario, subtotal)
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

        comando = "SELECT data_abertura FROM caixa WHERE id_user = %s ORDER BY data_abertura DESC LIMIT 1"
        cursor.execute(comando, (id_user,))
        data_abertura = cursor.fetchone()[0]  # Get single value instead of tuple

        comando = "SELECT saldo_atual FROM caixa WHERE id_user = %s AND data_abertura = %s"
        valores = (id_user, data_abertura)
        cursor.execute(comando, valores)
        resultado = cursor.fetchone()

        if resultado[0] is None:
            saldo_atual = 0
        else:
            saldo_atual = resultado[0]
        saldo_atual += self.total_geral
        print(id_forma_pagamento)
        if id_forma_pagamento == 4:
            comando = "UPDATE caixa SET saldo_atual = %s WHERE id_user = %s AND status = 1"
            valores = (saldo_atual, id_user)
            cursor.execute(comando, valores)
            self.conexao.commit()

        QMessageBox.information(None, "Sucesso", "Obrigado por Comprar no Mercado do Celsadas")
        self.tabela.clear()
        self.tela_principal.txt_valor_total.setText("R$ 00,00")
        self.tela_principal.input_pdv_forma_pagamento.setCurrentIndex(-1)
        self.carrinho = []

    def remover_carrinho(self):
        if not self.carrinho:
            QMessageBox.warning(None, "Erro", "Carrinho Vazio!")
            return
            
        item_selecionado = self.tela_principal.tabela_carrinho.currentItem()
        if item_selecionado is None:
            QMessageBox.warning(None, "Erro", "Selecione um Produto")
            return
            
        # Popup para pedir a senha com eco de senha (asteriscos)
        senha, ok = QInputDialog.getText(
            None,
            "Confirmação de Remoção",
            "Digite a senha para remover o item:",
            echo=QLineEdit.Password  # Correção: Usa QLineEdit.Password
        )
        
        if not ok or not senha:
            QMessageBox.warning(None, "Erro", "Senha não fornecida!")
            return
        
        senha_correta = "1234"  # Substitua pela sua lógica de validação
        if senha != senha_correta:
            QMessageBox.warning(None, "Erro", "Senha incorreta!")
            return

        index = self.tela_principal.tabela_carrinho.indexOfTopLevelItem(item_selecionado)
        if index != -1:  # Verifica se o item foi encontrado
            self.tela_principal.tabela_carrinho.takeTopLevelItem(index)
            self.carrinho.pop(index)
            self.mostrar_carrinho()
            QMessageBox.information(None, "Sucesso", "Item removido do carrinho!")
        else:
            QMessageBox.warning(None, "Erro", "Falha ao localizar o item no carrinho!")
        print(self.carrinho)
        