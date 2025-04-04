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
        self.forma_pagamento_true = {"Pix": 0, "Débito": 0, "Crédito": 0, "Dinheiro": 0}
        self.forma_pagamento_valor = {"Pix": 0, "Débito": 0, "Crédito": 0, "Dinheiro": 0}
        self.tela_principal.input_pdv_produto.setText("")
        self.tela_principal.txt_valor_pagar.setText("R$ 0.00")
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
        self.tela_principal.stackedWidget_2.setCurrentIndex(0)
        self.mostrar_carrinho()



    def mostrar_carrinho(self):
        self.tabela = self.tela_principal.tabela_carrinho
        
        self.tabela.clear()
        
        if self.tabela.columnCount() != 4:
            return
        
        self.total_geral = 0
        self.total = 0
        for item in self.carrinho:
            nome = item[0]
            preco = float(item[1]) 
            quantidade = float(item[2])  
            total_item = preco * quantidade  
            self.total_geral += total_item 
            self.total += total_item 
            
            linha = QTreeWidgetItem([nome, str(quantidade), f"R$ {preco:.2f}", f"R$ {total_item:.2f}"])
            self.tabela.addTopLevelItem(linha)
        
        for i in range(4):
            self.tabela.resizeColumnToContents(i)
        
        self.tela_principal.txt_valor_pagar.setText(f"R$ {self.total_geral:.2f}")
        self.tela_principal.txt_valor_total.setText(f"R$ {self.total_geral:.2f}")
    
    def forma_pagamento(self):

        self.forma = self.tela_principal.input_pdv_forma_pagamento.currentText()
        frame = self.tela_principal.frame_pagamento
        
        while frame.layout() and frame.layout().count():
            item = frame.layout().takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        if self.forma == "Pix":
            qr_label = QLabel()
            pixmap = QPixmap("imgs/qrcode.png")
            pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            qr_label.setPixmap(pixmap)
            qr_label.setAlignment(Qt.AlignCenter)
            frame.layout().addWidget(qr_label)
        else:
            self.dinheiro_input = QLineEdit()
            self.dinheiro_input.setPlaceholderText("Digite o valor que deseja pagar")
            self.dinheiro_input.setStyleSheet("font-size: 14px; padding: 5px;")
            self.dinheiro_input.setMaximumWidth(200) 
            
            frame.layout().addWidget(self.dinheiro_input)

    def processar_pagamento(self):

        if self.carrinho == []:
            QMessageBox.warning(None, "error", "Carrinho está Vazio!")
            return
        if self.tela_principal.input_pdv_forma_pagamento.currentIndex() == -1:
            QMessageBox.warning(None, "error", "Selecione uma forma de pagamento!")
            return

        if self.tela_principal.input_pdv_forma_pagamento.currentText() == "Pix":
            paga = self.total_geral
        else:
            paga = self.dinheiro_input.text()

        if self.total_geral == 0:
            QMessageBox.warning(None, "Erro", "Finalize a compra, pagamento já realizado!")
            return

        if paga == "":
            QMessageBox.warning(None, "error", "Digite um valor para o pagamento!")
            return
        else:
            paga = float(paga)

        if paga <= 0:
            QMessageBox.warning(None, "Erro", "Valor mínimo: R$ 1,00")
            return

        if paga >= self.total_geral:
            troco = paga - self.total_geral
            self.total_geral = 0 
            
            self.forma_pagamento_true[self.forma] = 1
            self.forma_pagamento_valor[self.forma] += paga

            for i in reversed(range(self.tela_principal.frame_pagamento.layout().count())):
                widget = self.tela_principal.frame_pagamento.layout().itemAt(i).widget()
                if isinstance(widget, QLabel):
                    widget.deleteLater()
            if self.forma == "Dinheiro":
                if troco > 0:
                    self.dinheiro_txt = QLabel(f"Troco: R$ {troco:.2f}")
                    self.dinheiro_txt.setStyleSheet("font-size: 14px; padding: 5px;")
                    self.dinheiro_txt.setMaximumWidth(200)
                    self.tela_principal.frame_pagamento.layout().addWidget(self.dinheiro_txt)
        else:
            self.total_geral -= paga
            self.forma_pagamento_true[self.forma] = 1
            self.forma_pagamento_valor[self.forma] += paga
            self.tela_principal.txt_valor_pagar.setText(f"R$ {self.total_geral:.2f}")
        print(self.forma_pagamento_true)
        print(self.forma_pagamento_valor)
        if self.total_geral == 0:
            self.tela_principal.txt_valor_pagar.setText(f"R$ {self.total_geral:.2f}")
            QMessageBox.information(None, "Sucesso", "Pagamento concluído!")

    def finalizar_compra(self):
        if self.carrinho == []:
            QMessageBox.warning(None, "error", "Carrinho está Vazio!")
            return
        
        if self.total_geral != 0:
            QMessageBox.warning(None, "error", "Termine de Processar o Pagamento!")
            return
        
        cursor = self.conexao.get_cursor()
        comando = "select id_usuario from usuarios where nome = %s"
        cursor.execute(comando, (self.tela_principal.txt_ola_user.text(), ))
        id_user = cursor.fetchone()[0]

        comando = """insert into vendas (id_usuario, valor_total, forma_pix, forma_credito, forma_debito, forma_dinheiro, valor_pix, valor_credito, valor_debito, valor_dinheiro) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        valores = (int(id_user), float(self.total), 
                   self.forma_pagamento_true["Pix"], self.forma_pagamento_true["Crédito"], self.forma_pagamento_true["Débito"], self.forma_pagamento_true["Dinheiro"], 
                   self.forma_pagamento_valor["Pix"], self.forma_pagamento_valor["Crédito"], self.forma_pagamento_valor["Débito"], self.forma_pagamento_valor["Dinheiro"])
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

        comando = "SELECT saldo_atual FROM caixa WHERE id_user = %s AND status = '1'"
        valores = (id_user,)
        cursor.execute(comando, valores)
        resultado = cursor.fetchone()

        if resultado[0] is None:
            saldo_atual = 0
        else:
            saldo_atual = resultado[0]
        saldo_atual += self.total

        comando = "UPDATE caixa SET saldo_atual = %s WHERE id_user = %s AND status = 1"
        valores = (saldo_atual, id_user)
        cursor.execute(comando, valores)
        self.conexao.commit()

        self.carrinho = []
        self.tela_principal.input_pdv_forma_pagamento.setCurrentIndex(-1)
        self.mostrar_carrinho()
        QMessageBox.information(None, "Sucesso", "Compra Finalizada com sucesso!")
        
    def remover_carrinho(self):
        if not self.carrinho:
            QMessageBox.warning(None, "Erro", "Carrinho Vazio!")
            return
            
        item_selecionado = self.tela_principal.tabela_carrinho.currentItem()
        if item_selecionado is None:
            QMessageBox.warning(None, "Erro", "Selecione um Produto")
            return
            
        # Solicita o ID do usuário
        id_usuario, ok1 = QInputDialog.getText(
            None,
            "Confirmação de Remoção",
            "Digite um ID com Permissão:",
            QLineEdit.Normal
        )

        if not ok1 or not id_usuario:
            QMessageBox.warning(None, "Erro", "ID não fornecido!")
            return

        # Verifica permissão e senha no banco
        cursor = self.conexao.get_cursor()
        comando = "SELECT perm, senha FROM usuarios WHERE id_usuario = %s"
        cursor.execute(comando, (id_usuario,))
        resultado = cursor.fetchone()

        if resultado is None:
            QMessageBox.warning(None, "Erro", "Usuário não encontrado! Chame um supervisor")
            cursor.close()
            return

        permisao, senha_armazenada = resultado

        if permisao == "0":
            QMessageBox.warning(None, "Erro", "Usuário não tem permissão para remover itens do carrinho!")
            cursor.close()
            return

        # Solicita a senha
        senha, ok2 = QInputDialog.getText(
            None,
            "Confirmação de Remoção",
            "Digite a senha para remover o item:",
            QLineEdit.Password
        )

        if not ok2 or not senha:
            QMessageBox.warning(None, "Erro", "Senha não fornecida!")
            cursor.close()
            return

        # Calcula o hash da senha digitada
        comando_senha = "SELECT SHA2(%s, 256)"
        cursor.execute(comando_senha, (senha,))
        senha_digitada_hash = cursor.fetchone()[0]

        # Compara com a senha armazenada (hash)
        if senha_digitada_hash != senha_armazenada:
            QMessageBox.warning(None, "Erro", "Senha incorreta!")
            cursor.close()
            return

        index = self.tela_principal.tabela_carrinho.indexOfTopLevelItem(item_selecionado)
        if index != -1:  # Verifica se o item foi encontrado
            self.tela_principal.tabela_carrinho.takeTopLevelItem(index)
            self.carrinho.pop(index)
            self.mostrar_carrinho()
            QMessageBox.information(None, "Sucesso", "Item removido do carrinho!")
        else:
            QMessageBox.warning(None, "Erro", "Falha ao localizar o item no carrinho!")
        