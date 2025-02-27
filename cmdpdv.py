from conexao_db import conexaoDB
from PySide6.QtWidgets import QFrame, QVBoxLayout, QLabel, QHBoxLayout, QWidget, QPushButton, QScrollArea, QGridLayout, QMessageBox
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QSize

class cmdPdv():
    def __init__(self, btn_pesquisar_produto, input_pesquisar_produto, txt_caso_nao_produto_encontrado, stackedWidget_2, txt_quantidade, txt_nome_preco_produto, tela_pincipal, txt_nome_produto_1, txt_quantidade_1, txt_valor_1):
        self.btn_pesquisar_produto = btn_pesquisar_produto
        self.input_pesquisar_produto = input_pesquisar_produto
        self.txt_caso_nao_produto_encontrado = txt_caso_nao_produto_encontrado
        self.stackedWidget_2 = stackedWidget_2
        self.txt_quantidade = txt_quantidade
        self.txt_nome_preco_produto = txt_nome_preco_produto
        self.txt_nome_produto_1 = txt_nome_produto_1
        self.txt_quantidade_1 = txt_quantidade_1
        self.txt_valor_1 = txt_valor_1
        self.tela_principal = tela_pincipal
        self.conexao = conexaoDB()
        self.carrinho = 0
        self.adc_card()

    def procurar_produto(self):
        print("foi")

        self.resultado_busca_produto = self.tela_principal.input_pesquisar_produto.text()
        
        if not self.resultado_busca_produto:
            self.tela_principal.txt_caso_nao_produto_encontrado.setText("Digite um produto para buscar.")
            return

        cursor = self.conexao.get_cursor()

        valores = (self.resultado_busca_produto, self.resultado_busca_produto)
        cursor.execute("SELECT nome, preco, quantidade FROM estoque WHERE nome = %s OR id = %s", valores)

        resultado = cursor.fetchone()

        if resultado is None:
            self.tela_principal.txt_caso_nao_produto_encontrado.setText("Produto não encontrado!")
        else:
            self.nome, self.preco, self.quantidade = resultado
            self.tela_principal.stackedWidget_2.setCurrentIndex(1)
            self.tela_principal.txt_nome_preco_produto.setText(f"{self.nome} R${self.preco:.2f}")
            self.tela_principal.txt_quantidade.setText("0")
            
        cursor.close()
    
    def menos(self):
        quantidade = int(self.txt_quantidade.text())

        if quantidade == 0:
            QMessageBox.warning(None, "Erro", "Não pode diminuir mais")
        else:
            quantidade -= 1
            self.txt_quantidade.setText(f"{quantidade}")
        self.carrinho.append(self.nome, self.preco, self.quantidade)


    def mais(self):
        quantidade = int(self.txt_quantidade.text())

        if quantidade >= self.quantidade:
            QMessageBox.warning(None, "Erro", "Não pode aumentar mais")
        else:
            quantidade += 1
            self.txt_quantidade.setText(f"{quantidade}")

    def adc_card(self):
        # Acessa a ScrollArea e seu conteúdo
        scroll_area = self.tela_principal.scrollArea
        scroll_content = self.tela_principal.scrollAreaWidgetContents

        # Configurações para garantir rolagem vertical
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll_area.setWidgetResizable(False)  # Desativa redimensionamento automático
        scroll_area.setFixedHeight(600)  # Limita a altura para forçar rolagem

        # Remove o layout existente, se houver
        if scroll_content.layout() is not None:
            # Limpa os widgets do layout atual
            old_layout = scroll_content.layout()
            while old_layout.count():
                child = old_layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
            # Remove o layout antigo do scroll_content
            QWidget().setLayout(scroll_content.layout())  # Transfere o layout para um widget temporário para deletá-lo
            scroll_content.setLayout(None)  # Remove o layout

        # Cria um novo QGridLayout
        scroll_layout = QGridLayout(scroll_content)
        scroll_content.setLayout(scroll_layout)

        # Conecta ao banco de dados e busca todos os produtos
        cursor = self.conexao.get_cursor()
        cursor.execute("SELECT nome, preco, quantidade, imagem FROM estoque")
        produtos = cursor.fetchall()

        if not produtos:
            self.tela_principal.txt_caso_nao_produto_encontrado.setText("Nenhum produto encontrado no estoque!")
            cursor.close()
            return

        # Organiza os cards em uma grade com 3 colunas
        colunas = 3  # Número de colunas por linha
        row = 0
        col = 0

        for idx, produto in enumerate(produtos):
            nome, preco, quantidade, imagem = produto

            # Cria o frame do card
            card_frame = QFrame()
            card_frame.setStyleSheet("""
                background-color: #ffffff;
                border-radius: 10px;
                border: 1px solid #dbdbdb;
                padding: 10px;
            """)
            card_frame.setFixedSize(400, 400)

            # Layout principal do card (vertical)
            card_layout = QVBoxLayout(card_frame)
            card_layout.setContentsMargins(0, 0, 0, 0)

            # Container para a imagem
            image_container = QFrame()
            image_container.setStyleSheet("border: none;")
            image_layout = QHBoxLayout(image_container)
            image_layout.setContentsMargins(0, 0, 0, 0)
            
            # Carrega a imagem do produto
            imagem_label = QLabel()
            imagem_label.setFixedSize(200, 200)
            imagem_label.setStyleSheet("border: none;")
            if imagem:
                pixmap = QPixmap(imagem)
                if not pixmap.isNull():
                    imagem_label.setPixmap(pixmap.scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                    imagem_label.setAlignment(Qt.AlignCenter)
                else:
                    imagem_label.setText("Sem imagem")
                    imagem_label.setAlignment(Qt.AlignCenter)
                    imagem_label.setStyleSheet("font-size: 20px; color: #666666; border: none;")
            else:
                imagem_label.setText("Sem imagem")
                imagem_label.setAlignment(Qt.AlignCenter)
                imagem_label.setStyleSheet("font-size: 20px; color: #666666; border: none;")
            
            image_layout.addWidget(imagem_label)
            image_layout.setAlignment(Qt.AlignCenter)
            card_layout.addWidget(image_container, alignment=Qt.AlignCenter)

            # Informações do produto
            nome_label = QLabel(f"{nome}")
            nome_label.setStyleSheet("""
                font-size: 18px; 
                font-weight: bold; 
                border: none; 
                background: transparent;
            """)
            nome_label.setWordWrap(True)
            nome_label.setAlignment(Qt.AlignCenter)
            
            preco_label = QLabel(f"R${preco:.2f}")
            preco_label.setStyleSheet("""
                font-size: 16px; 
                border: none; 
                background: transparent;
            """)
            preco_label.setAlignment(Qt.AlignCenter)
            
            quantidade_label = QLabel(f"Estoque: {quantidade}")
            quantidade_label.setStyleSheet("""
                font-size: 16px; 
                border: none; 
                background: transparent;
            """)
            quantidade_label.setAlignment(Qt.AlignCenter)

            # Adiciona as informações ao layout
            card_layout.addWidget(nome_label)
            card_layout.addWidget(preco_label)
            card_layout.addWidget(quantidade_label)

            # Botão Comprar
            btn_comprar = QPushButton("Comprar")
            btn_comprar.setStyleSheet("""
                background-color: #005AFF;
                color: #F0F8FF;
                border-radius: 10px;
                padding: 10px;
                font-size: 16px;
            """)
            btn_comprar.setFixedSize(200, 50)
            btn_comprar.clicked.connect(lambda checked, n=nome, p=preco, q=quantidade: self.comprar_produto(n, p, q))
            
            card_layout.addWidget(btn_comprar, alignment=Qt.AlignCenter)

            # Calcula a posição na grade (3 colunas por linha)
            row = idx // colunas
            col = idx % colunas
            scroll_layout.addWidget(card_frame, row, col)

        # Calcula o tamanho total do conteúdo
        num_rows = (len(produtos) + colunas - 1) // colunas  # Número de linhas necessárias
        content_height = num_rows * 510  # 500 (altura do card) + 10 (espaço estimado)
        content_width = colunas * 510  # 3 colunas de 500 pixels + margens
        scroll_content.setMinimumSize(QSize(content_width, content_height))

        # Garante que o widget interno seja atualizado na ScrollArea
        scroll_area.setWidget(scroll_content)

        cursor.close()

    def comprar_produto(self, nome, preco, quantidade):
        """Função chamada ao clicar no botão Comprar"""
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.tela_principal.stackedWidget_2.setCurrentIndex(1)
        self.tela_principal.txt_nome_preco_produto.setText(f"{nome} R${preco:.2f}")
        self.tela_principal.txt_quantidade.setText("1")