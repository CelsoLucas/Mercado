# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_tela_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QTabWidget, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)
from imgs import icons_rc

class Ui_TelaPrincipal(object):
    def setupUi(self, TelaPrincipal):
        if not TelaPrincipal.objectName():
            TelaPrincipal.setObjectName(u"TelaPrincipal")
        TelaPrincipal.resize(1260, 845)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TelaPrincipal.sizePolicy().hasHeightForWidth())
        TelaPrincipal.setSizePolicy(sizePolicy)
        TelaPrincipal.setStyleSheet(u"*{\n"
"	font: \"poppins\";\n"
"}\n"
"#menu{\n"
"	background-color: #005AFF;\n"
"}\n"
"\n"
"#menu QLabel{\n"
"    color: #F0F8FF; /* Cor dos textos */\n"
"    font-size: 28px; /* Tamanho dos textos */\n"
"}\n"
"\n"
"#mainbody{\n"
"	background-color:  #005AFF;\n"
"}\n"
"\n"
"#telaprincipal, #telaconfiguracoes, #telaestoque, #telapdv, #telarelatorios{\n"
"	border-radius: 20px;\n"
"	background-color: rgb(240, 248, 255);\n"
"}\n"
"\n"
" #frame_vendas_dia, #frame_vendas_semana, #frame_vendas_mes, #frame_produtos_baixo_estoque, #layout_relatorios_1, #layout_relatorios_2, #layout_relatorios_3, #layout_relatorios_4 {\n"
"    background-color: #dbdbdb;\n"
"	font-size: 20px;\n"
"	border-radius: 20px;\n"
"	color: #F0F8FF;\n"
"}\n"
"\n"
"#frame_vendas_dia QLabel, \n"
"#frame_vendas_semana QLabel, \n"
"#frame_vendas_mes QLabel, \n"
"#frame_produtos_baixo_estoque QLabel,\n"
"#layout_relatorios_1 QLabel,\n"
" #layout_relatorios_2 QLabel, \n"
"#layout_relatorios_3 QLabel,\n"
" #layout_relatorios_4 QLabel{\n"
"    color: #black"
                        "; /* Cor dos textos */\n"
"    font-size: 20px; /* Tamanho dos textos */\n"
"}\n"
"\n"
"#btn_pdv, #btn_configuracoes, #btn_estoque, #btn_relatorios, #btn_tela_principal{\n"
"	border-radius: 10px\n"
"}\n"
"\n"
"#btn_adc_produto, #btn_finalizar_compra, #btn_adc_carrinho, #btn_adc_categoria, #btn_procurar_ft_adc_usuario, #btn_adc_usuario,#btn_adc_categoria_2, #btn_adc_user, #btn_procurar_ft_produto{\n"
"	  background-color: #005AFF; /* Fundo transparente */\n"
" 	 color: #F0F8FF; /* Cor do texto */\n"
"  	border-radius: 20px; /* Bordas arredondadas */\n"
"  	padding: 12px 24px; /* Espa\u00e7amento interno */\n"
"  font-size: 24px; /* Tamanho da fonte */\n"
"  cursor: pointer; /* Cursor de m\u00e3o */\n"
"  transition: background-color 0.3s, color 0.3s; /* Transi\u00e7\u00e3o suave */\n"
"}\n"
"#btn_adc_produto:hover, #btn_finalizar_compra:hover, #btn_adc_carrinho:hover, #btn_adc_categoria:hover, #btn_procurar_ft_adc_usuario:hover, #btn_adc_usuario:hover, #btn_adc_categoria_2:hover,  #btn_adc_user:hove, #btn_procu"
                        "rar_ft_produto:hover{\n"
"  background-color: #F0F8FF;\n"
"  border: 2px solid #005AFF;\n"
"  color: black; /* Cor do texto ao passar o mouse */\n"
"}\n"
"\n"
"#btn_adc_produto:pressed, #btn_finalizar_compra:pressed, #btn_adc_carrinho:pressed, #btn_adc_categoria:pressed, #btn_procurar_ft_adc_usuario:pressed, #btn_adc_usuario:pressed, btn_adc_categoria_2:pressed,  #btn_adc_user:pressed, #btn_procurar_ft_produto:pressed{\n"
"  background-color: #F0F8FF;\n"
"  border: 2px solid #005AFF;\n"
"  color: black; /* Cor do texto ao passar o mouse */\n"
"}\n"
"/*\n"
"#input_forma_pagamento{\n"
"	border: 2px solid #3498db;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-left-radius: 20px;\n"
"    border-bottom-right-radius: 20px;\n"
"    outline: none;\n"
"    font-size: 26px;\n"
"    font-weight: 600;\n"
"    padding: 6px 12px;\n"
"    width: 100%;\n"
"    background: white;\n"
"    transition: border-color 0.3s ease-in-out, background-color 0.3s ease-in-out;\n"
"}\n"
"\n"
""
                        "#input_forma_pagamento::editable {\n"
"    padding: 6px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"#input_forma_pagamento:hover {\n"
"    border: 2px solid #2980b9;\n"
"    background-color: #f0f8ff;\n"
"}\n"
"\n"
"#input_forma_pagamento:focus,#input_forma_pagamento:on {\n"
"    border: 2px solid #1c6ea4;\n"
"    background-color: #e0f0ff;\n"
"}\n"
"#input_forma_pagamento::drop-down {\n"
"    border: none;\n"
"    width: 30px;\n"
"}\n"
"#input_forma_pagamento::down-arrow {\n"
"    image: url(:/icons/down-arrow.png);\n"
"    width: 16px;\n"
"    height: 16px;\n"
"}\n"
"\n"
"#input_forma_pagamento QAbstractItemView {\n"
"    background-color: white;\n"
"    border: 2px solid #3498db;\n"
"    selection-background-color: #1c6ea4;\n"
"    selection-color: white;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border-top-left-radius: 20px;\n"
"    border-top-right-radius: 20px;\n"
"}\n"
"\n"
"#input_forma_pagamento QAbstractItemView::item {\n"
"    padding: 8px;\n"
"    text"
                        "-align: center;\n"
"}\n"
"*/\n"
"QLineEdit {\n"
"    border: 2px solid #3498db;\n"
"    border-radius: 20px;\n"
"    outline: none;\n"
"    font-size: 26px;\n"
"	font-weight: 600;\n"
"    padding: 4px;\n"
"    width: 100%;\n"
"    background: white;\n"
"    transition: border-color 0.3s ease-in-out, background-color 0.3s ease-in-out;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #2980b9;\n"
"    background-color: #f0f8ff;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #1c6ea4;\n"
"    background-color: #e0f0ff;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: #aaa;\n"
"    font-style: italic;\n"
"}\n"
"\n"
"QPushButton {\n"
"  background-color: #F0F8FF; /* Fundo transparente */\n"
"  color: #3C3744; /* Cor do texto */\n"
"  border-radius: 20px; /* Bordas arredondadas */\n"
"  padding: 12px 24px; /* Espa\u00e7amento interno */\n"
"  font-size: 16px; /* Tamanho da fonte */\n"
"  cursor: pointer; /* Cursor de m\u00e3o */\n"
"  transition: background-color 0.3s, color 0.3s; /* Transi"
                        "\u00e7\u00e3o suave */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #005AFF;\n"
"  border: 2px solid #F0F8FF;\n"
"  color: #F0F8FF; /* Cor do texto ao passar o mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #005AFF; /* Cor de fundo ao passar o mouse */\n"
"  border: 2px solid #F0F8FF;\n"
"  color: #F0F8FF; /* Cor do texto ao passar o mouse */\n"
"}\n"
"\n"
"/* Estiliza\u00e7\u00e3o do QComboBox */\n"
"QComboBox {\n"
"    border: 2px solid #3498db;\n"
"    border-top-left-radius: 20px;\n"
"    border-top-right-radius: 20px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    outline: none;\n"
"    font-size: 26px;\n"
"    font-weight: 600;\n"
"    padding: 6px 12px; /* Ajuste do espa\u00e7amento interno */\n"
"    width: 100%;\n"
"    background: white;\n"
"    transition: border-color 0.3s ease-in-out, background-color 0.3s ease-in-out;\n"
"}\n"
"\n"
"/* Centraliza o texto */\n"
"QComboBox::editable {\n"
"    padding: 6px;\n"
"    text-a"
                        "lign: center;\n"
"}\n"
"\n"
"/* Hover */\n"
"QComboBox:hover {\n"
"    border: 2px solid #2980b9;\n"
"    background-color: #f0f8ff;\n"
"}\n"
"\n"
"/* Quando o combobox \u00e9 clicado */\n"
"QComboBox:focus, QComboBox:on {\n"
"    border: 2px solid #1c6ea4;\n"
"    background-color: #e0f0ff;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"/* Remove a borda do bot\u00e3o dropdown */\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"    width: 30px;\n"
"}\n"
"\n"
"/* Personaliza a seta do dropdown */\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icons/down-arrow.png); /* Substitua pelo caminho da sua seta */\n"
"    width: 16px;\n"
"    height: 16px;\n"
"}\n"
"\n"
"/* Estiliza a lista suspensa (popup) */\n"
"QComboBox QAbstractItemView {\n"
"    background-color: white;\n"
"    border: 2px solid #3498db;\n"
"    selection-background-color: #1c6ea4;\n"
"    selection-color: white;\n"
"    border-bottom-left-radius: 20px;\n"
"    border-bottom-right-radius: 20p"
                        "x;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"}\n"
"\n"
"/* Centraliza os itens do menu suspenso */\n"
"QComboBox QAbstractItemView::item {\n"
"    padding: 8px;\n"
"    text-align: center;\n"
"}\n"
"")
        self.centralwidget = QWidget(TelaPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.menu = QWidget(self.centralwidget)
        self.menu.setObjectName(u"menu")
        self.menu.setMinimumSize(QSize(0, 75))
        self.menu.setStyleSheet(u"font-size: 26px;")
        self.horizontalLayout = QHBoxLayout(self.menu)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.layout_menu_lado_direito = QFrame(self.menu)
        self.layout_menu_lado_direito.setObjectName(u"layout_menu_lado_direito")
        self.layout_menu_lado_direito.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_menu_lado_direito.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.layout_menu_lado_direito)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(20, 0, 0, 0)
        self.img_logo = QLabel(self.layout_menu_lado_direito)
        self.img_logo.setObjectName(u"img_logo")

        self.horizontalLayout_2.addWidget(self.img_logo)


        self.horizontalLayout.addWidget(self.layout_menu_lado_direito)

        self.laout_menu_lado_esquerdo = QFrame(self.menu)
        self.laout_menu_lado_esquerdo.setObjectName(u"laout_menu_lado_esquerdo")
        self.laout_menu_lado_esquerdo.setFrameShape(QFrame.Shape.StyledPanel)
        self.laout_menu_lado_esquerdo.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.laout_menu_lado_esquerdo)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.txt_ola_user = QLabel(self.laout_menu_lado_esquerdo)
        self.txt_ola_user.setObjectName(u"txt_ola_user")

        self.horizontalLayout_3.addWidget(self.txt_ola_user)

        self.btn_sair = QPushButton(self.laout_menu_lado_esquerdo)
        self.btn_sair.setObjectName(u"btn_sair")
        self.btn_sair.setMinimumSize(QSize(50, 25))
        icon = QIcon()
        icon.addFile(u":/icons/exit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_sair.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.btn_sair)


        self.horizontalLayout.addWidget(self.laout_menu_lado_esquerdo, 0, Qt.AlignmentFlag.AlignRight)


        self.gridLayout_4.addWidget(self.menu, 0, 0, 1, 1)

        self.mainbody = QWidget(self.centralwidget)
        self.mainbody.setObjectName(u"mainbody")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainbody.sizePolicy().hasHeightForWidth())
        self.mainbody.setSizePolicy(sizePolicy1)
        self.horizontalLayout_4 = QHBoxLayout(self.mainbody)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.menu_lateral = QWidget(self.mainbody)
        self.menu_lateral.setObjectName(u"menu_lateral")
        self.menu_lateral.setMinimumSize(QSize(250, 0))
        self.menu_lateral.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.menu_lateral)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.layout_menu_lateral = QWidget(self.menu_lateral)
        self.layout_menu_lateral.setObjectName(u"layout_menu_lateral")
        self.verticalLayout_3 = QVBoxLayout(self.layout_menu_lateral)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 0, 0, 0)
        self.frame = QFrame(self.layout_menu_lateral)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_tela_principal = QPushButton(self.frame)
        self.btn_tela_principal.setObjectName(u"btn_tela_principal")
        self.btn_tela_principal.setMinimumSize(QSize(200, 50))
        self.btn_tela_principal.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_tela_principal.setIcon(icon1)

        self.verticalLayout_4.addWidget(self.btn_tela_principal)

        self.btn_pdv = QPushButton(self.frame)
        self.btn_pdv.setObjectName(u"btn_pdv")
        self.btn_pdv.setMinimumSize(QSize(200, 50))
        self.btn_pdv.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/dollar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_pdv.setIcon(icon2)

        self.verticalLayout_4.addWidget(self.btn_pdv)

        self.btn_estoque = QPushButton(self.frame)
        self.btn_estoque.setObjectName(u"btn_estoque")
        self.btn_estoque.setMinimumSize(QSize(200, 50))
        self.btn_estoque.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/box-open.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_estoque.setIcon(icon3)

        self.verticalLayout_4.addWidget(self.btn_estoque)

        self.btn_relatorios = QPushButton(self.frame)
        self.btn_relatorios.setObjectName(u"btn_relatorios")
        self.btn_relatorios.setMinimumSize(QSize(200, 50))
        self.btn_relatorios.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/analytics.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_relatorios.setIcon(icon4)

        self.verticalLayout_4.addWidget(self.btn_relatorios)

        self.btn_configuracoes = QPushButton(self.frame)
        self.btn_configuracoes.setObjectName(u"btn_configuracoes")
        self.btn_configuracoes.setMinimumSize(QSize(200, 50))
        self.btn_configuracoes.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/settings (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_configuracoes.setIcon(icon5)

        self.verticalLayout_4.addWidget(self.btn_configuracoes)


        self.verticalLayout_3.addWidget(self.frame)


        self.verticalLayout_2.addWidget(self.layout_menu_lateral)


        self.horizontalLayout_4.addWidget(self.menu_lateral)

        self._info_principal = QWidget(self.mainbody)
        self._info_principal.setObjectName(u"_info_principal")
        self.verticalLayout_5 = QVBoxLayout(self._info_principal)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(50, 50, 50, 50)
        self.stackedWidget = QStackedWidget(self._info_principal)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.telaprincipal = QWidget()
        self.telaprincipal.setObjectName(u"telaprincipal")
        self.telaprincipal.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.telaprincipal)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.layout_tela_principal = QFrame(self.telaprincipal)
        self.layout_tela_principal.setObjectName(u"layout_tela_principal")
        self.layout_tela_principal.setStyleSheet(u"")
        self.layout_tela_principal.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_tela_principal.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.layout_tela_principal)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_produtos_baixo_estoque = QFrame(self.layout_tela_principal)
        self.frame_produtos_baixo_estoque.setObjectName(u"frame_produtos_baixo_estoque")
        self.frame_produtos_baixo_estoque.setStyleSheet(u"	background-color: #dbdbdb;\n"
"	border-radius: 20px;\n"
"	font-size: 20px;")
        self.frame_produtos_baixo_estoque.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_produtos_baixo_estoque.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_produtos_baixo_estoque)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.txt_produtos_baixo_estoque = QLabel(self.frame_produtos_baixo_estoque)
        self.txt_produtos_baixo_estoque.setObjectName(u"txt_produtos_baixo_estoque")

        self.verticalLayout_14.addWidget(self.txt_produtos_baixo_estoque, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.txt_produtos_baixo_estoque_db = QLabel(self.frame_produtos_baixo_estoque)
        self.txt_produtos_baixo_estoque_db.setObjectName(u"txt_produtos_baixo_estoque_db")

        self.verticalLayout_14.addWidget(self.txt_produtos_baixo_estoque_db, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalSpacer_7 = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_14.addItem(self.verticalSpacer_7)


        self.gridLayout.addWidget(self.frame_produtos_baixo_estoque, 3, 0, 1, 3)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer_3, 4, 1, 1, 1)

        self.frame_vendas_semana = QFrame(self.layout_tela_principal)
        self.frame_vendas_semana.setObjectName(u"frame_vendas_semana")
        self.frame_vendas_semana.setMaximumSize(QSize(300, 300))
        self.frame_vendas_semana.setStyleSheet(u"	background-color: #dbdbdb;\n"
"	border-radius: 20px;\n"
"	font-size: 20px;")
        self.frame_vendas_semana.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_vendas_semana.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_vendas_semana)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.txt_vendas_semana = QLabel(self.frame_vendas_semana)
        self.txt_vendas_semana.setObjectName(u"txt_vendas_semana")

        self.verticalLayout_12.addWidget(self.txt_vendas_semana, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.txt_vendas_semana_db = QLabel(self.frame_vendas_semana)
        self.txt_vendas_semana_db.setObjectName(u"txt_vendas_semana_db")

        self.verticalLayout_12.addWidget(self.txt_vendas_semana_db, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_5 = QSpacerItem(20, 83, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_12.addItem(self.verticalSpacer_5)


        self.gridLayout.addWidget(self.frame_vendas_semana, 1, 1, 1, 1)

        self.frame_vendas_dia = QFrame(self.layout_tela_principal)
        self.frame_vendas_dia.setObjectName(u"frame_vendas_dia")
        self.frame_vendas_dia.setMaximumSize(QSize(300, 300))
        self.frame_vendas_dia.setStyleSheet(u"	background-color: #dbdbdb;\n"
"	border-radius: 20px;\n"
"	font-size: 20px;")
        self.frame_vendas_dia.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_vendas_dia.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_vendas_dia)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.txt_vendasdia = QLabel(self.frame_vendas_dia)
        self.txt_vendasdia.setObjectName(u"txt_vendasdia")

        self.verticalLayout_11.addWidget(self.txt_vendasdia, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.txt_vendas_dia_db = QLabel(self.frame_vendas_dia)
        self.txt_vendas_dia_db.setObjectName(u"txt_vendas_dia_db")

        self.verticalLayout_11.addWidget(self.txt_vendas_dia_db, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_11.addItem(self.verticalSpacer_4)


        self.gridLayout.addWidget(self.frame_vendas_dia, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer, 2, 1, 1, 1)

        self.frame_vendas_mes = QFrame(self.layout_tela_principal)
        self.frame_vendas_mes.setObjectName(u"frame_vendas_mes")
        self.frame_vendas_mes.setMaximumSize(QSize(300, 300))
        self.frame_vendas_mes.setStyleSheet(u"	background-color: #dbdbdb;\n"
"	border-radius: 20px;\n"
"	font-size: 20px;")
        self.frame_vendas_mes.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_vendas_mes.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_vendas_mes)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.txt_vendas_mes = QLabel(self.frame_vendas_mes)
        self.txt_vendas_mes.setObjectName(u"txt_vendas_mes")

        self.verticalLayout_13.addWidget(self.txt_vendas_mes, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.txt_vendas_mes_db = QLabel(self.frame_vendas_mes)
        self.txt_vendas_mes_db.setObjectName(u"txt_vendas_mes_db")

        self.verticalLayout_13.addWidget(self.txt_vendas_mes_db, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_6 = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_13.addItem(self.verticalSpacer_6)


        self.gridLayout.addWidget(self.frame_vendas_mes, 1, 2, 1, 1)


        self.verticalLayout_6.addWidget(self.layout_tela_principal)

        self.stackedWidget.addWidget(self.telaprincipal)
        self.telapdv = QWidget()
        self.telapdv.setObjectName(u"telapdv")
        self.telapdv.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.telapdv)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.stackedWidget_2 = QStackedWidget(self.telapdv)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.tela_pdv_1 = QWidget()
        self.tela_pdv_1.setObjectName(u"tela_pdv_1")
        self.verticalLayout_15 = QVBoxLayout(self.tela_pdv_1)
        self.verticalLayout_15.setSpacing(6)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(9, 9, 9, 9)
        self.tela_pdv_1_info_principal = QWidget(self.tela_pdv_1)
        self.tela_pdv_1_info_principal.setObjectName(u"tela_pdv_1_info_principal")
        self.verticalLayout_16 = QVBoxLayout(self.tela_pdv_1_info_principal)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.layout_pesquisar_produto = QFrame(self.tela_pdv_1_info_principal)
        self.layout_pesquisar_produto.setObjectName(u"layout_pesquisar_produto")
        self.layout_pesquisar_produto.setMinimumSize(QSize(500, 0))
        self.layout_pesquisar_produto.setMaximumSize(QSize(700, 16777215))
        self.layout_pesquisar_produto.setStyleSheet(u"")
        self.layout_pesquisar_produto.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_pesquisar_produto.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.layout_pesquisar_produto)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(80, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.input_pesquisar_produto = QLineEdit(self.layout_pesquisar_produto)
        self.input_pesquisar_produto.setObjectName(u"input_pesquisar_produto")
        self.input_pesquisar_produto.setMinimumSize(QSize(400, 0))
        self.input_pesquisar_produto.setMaximumSize(QSize(16777215, 16777215))
        self.input_pesquisar_produto.setStyleSheet(u"")
        self.input_pesquisar_produto.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.input_pesquisar_produto, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.btn_pesquisar_produto = QPushButton(self.layout_pesquisar_produto)
        self.btn_pesquisar_produto.setObjectName(u"btn_pesquisar_produto")
        self.btn_pesquisar_produto.setStyleSheet(u"background-color: none;")
        icon6 = QIcon()
        icon6.addFile(u":/icons/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_pesquisar_produto.setIcon(icon6)

        self.horizontalLayout_5.addWidget(self.btn_pesquisar_produto)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)


        self.verticalLayout_16.addWidget(self.layout_pesquisar_produto, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_15.addWidget(self.tela_pdv_1_info_principal, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.txt_caso_nao_produto_encontrado = QLabel(self.tela_pdv_1)
        self.txt_caso_nao_produto_encontrado.setObjectName(u"txt_caso_nao_produto_encontrado")
        self.txt_caso_nao_produto_encontrado.setStyleSheet(u"font-size:20px;")

        self.verticalLayout_15.addWidget(self.txt_caso_nao_produto_encontrado, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.scrollArea = QScrollArea(self.tela_pdv_1)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 63, 18))
        self.horizontalLayout_13 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_15.addWidget(self.scrollArea)

        self.stackedWidget_2.addWidget(self.tela_pdv_1)
        self.tela_pdv_2 = QWidget()
        self.tela_pdv_2.setObjectName(u"tela_pdv_2")
        self.verticalLayout_17 = QVBoxLayout(self.tela_pdv_2)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.tela_pdv_2_info_principal = QWidget(self.tela_pdv_2)
        self.tela_pdv_2_info_principal.setObjectName(u"tela_pdv_2_info_principal")
        self.verticalLayout_18 = QVBoxLayout(self.tela_pdv_2_info_principal)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.layout_pesquisar_produto_2 = QFrame(self.tela_pdv_2_info_principal)
        self.layout_pesquisar_produto_2.setObjectName(u"layout_pesquisar_produto_2")
        self.layout_pesquisar_produto_2.setMinimumSize(QSize(500, 0))
        self.layout_pesquisar_produto_2.setMaximumSize(QSize(700, 16777215))
        self.layout_pesquisar_produto_2.setStyleSheet(u"")
        self.layout_pesquisar_produto_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_pesquisar_produto_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.layout_pesquisar_produto_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_2 = QSpacerItem(80, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.input_pesquisar_produto_2 = QLineEdit(self.layout_pesquisar_produto_2)
        self.input_pesquisar_produto_2.setObjectName(u"input_pesquisar_produto_2")
        self.input_pesquisar_produto_2.setMinimumSize(QSize(400, 0))
        self.input_pesquisar_produto_2.setMaximumSize(QSize(16777215, 16777215))
        self.input_pesquisar_produto_2.setStyleSheet(u"")
        self.input_pesquisar_produto_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.input_pesquisar_produto_2, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.btn_pesquisar_produto_2 = QPushButton(self.layout_pesquisar_produto_2)
        self.btn_pesquisar_produto_2.setObjectName(u"btn_pesquisar_produto_2")
        self.btn_pesquisar_produto_2.setMaximumSize(QSize(50, 16777215))
        self.btn_pesquisar_produto_2.setStyleSheet(u"background-color: none;")
        self.btn_pesquisar_produto_2.setIcon(icon6)
        self.btn_pesquisar_produto_2.setIconSize(QSize(25, 25))

        self.horizontalLayout_6.addWidget(self.btn_pesquisar_produto_2, 0, Qt.AlignmentFlag.AlignRight)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)


        self.verticalLayout_18.addWidget(self.layout_pesquisar_produto_2, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.resultado_pesquisa_produto = QWidget(self.tela_pdv_2_info_principal)
        self.resultado_pesquisa_produto.setObjectName(u"resultado_pesquisa_produto")
        sizePolicy1.setHeightForWidth(self.resultado_pesquisa_produto.sizePolicy().hasHeightForWidth())
        self.resultado_pesquisa_produto.setSizePolicy(sizePolicy1)
        self.resultado_pesquisa_produto.setMinimumSize(QSize(350, 0))
        self.resultado_pesquisa_produto.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_8 = QHBoxLayout(self.resultado_pesquisa_produto)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.layout_nome_preco_produto = QFrame(self.resultado_pesquisa_produto)
        self.layout_nome_preco_produto.setObjectName(u"layout_nome_preco_produto")
        self.layout_nome_preco_produto.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_nome_preco_produto.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.layout_nome_preco_produto)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.txt_nome_preco_produto = QLabel(self.layout_nome_preco_produto)
        self.txt_nome_preco_produto.setObjectName(u"txt_nome_preco_produto")
        self.txt_nome_preco_produto.setStyleSheet(u"font-size:20px;")

        self.horizontalLayout_7.addWidget(self.txt_nome_preco_produto)


        self.horizontalLayout_8.addWidget(self.layout_nome_preco_produto)

        self.layout_quant_produto = QFrame(self.resultado_pesquisa_produto)
        self.layout_quant_produto.setObjectName(u"layout_quant_produto")
        self.layout_quant_produto.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_quant_produto.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.layout_quant_produto)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.btn_menos = QPushButton(self.layout_quant_produto)
        self.btn_menos.setObjectName(u"btn_menos")
        self.btn_menos.setStyleSheet(u"background-color: none;")
        icon7 = QIcon()
        icon7.addFile(u":/icons/minus-circle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_menos.setIcon(icon7)

        self.horizontalLayout_9.addWidget(self.btn_menos)

        self.txt_quantidade = QLabel(self.layout_quant_produto)
        self.txt_quantidade.setObjectName(u"txt_quantidade")
        self.txt_quantidade.setStyleSheet(u"font-size: 20px;")

        self.horizontalLayout_9.addWidget(self.txt_quantidade)

        self.btn_mais = QPushButton(self.layout_quant_produto)
        self.btn_mais.setObjectName(u"btn_mais")
        self.btn_mais.setStyleSheet(u"background-color: none;")
        icon8 = QIcon()
        icon8.addFile(u":/icons/add.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_mais.setIcon(icon8)

        self.horizontalLayout_9.addWidget(self.btn_mais)


        self.horizontalLayout_8.addWidget(self.layout_quant_produto)


        self.verticalLayout_18.addWidget(self.resultado_pesquisa_produto, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.btn_adc_carrinho = QPushButton(self.tela_pdv_2_info_principal)
        self.btn_adc_carrinho.setObjectName(u"btn_adc_carrinho")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_adc_carrinho.sizePolicy().hasHeightForWidth())
        self.btn_adc_carrinho.setSizePolicy(sizePolicy2)
        self.btn_adc_carrinho.setMinimumSize(QSize(200, 0))
        icon9 = QIcon()
        icon9.addFile(u":/icons/shopping-cart (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_adc_carrinho.setIcon(icon9)

        self.verticalLayout_18.addWidget(self.btn_adc_carrinho, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_17.addWidget(self.tela_pdv_2_info_principal)

        self.stackedWidget_2.addWidget(self.tela_pdv_2)
        self.tela_pdv_3 = QWidget()
        self.tela_pdv_3.setObjectName(u"tela_pdv_3")
        self.verticalLayout_19 = QVBoxLayout(self.tela_pdv_3)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.tela_pdv_3_info_principal_4 = QWidget(self.tela_pdv_3)
        self.tela_pdv_3_info_principal_4.setObjectName(u"tela_pdv_3_info_principal_4")
        self.verticalLayout_21 = QVBoxLayout(self.tela_pdv_3_info_principal_4)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.layout_pesquisar_produto_3 = QFrame(self.tela_pdv_3_info_principal_4)
        self.layout_pesquisar_produto_3.setObjectName(u"layout_pesquisar_produto_3")
        self.layout_pesquisar_produto_3.setMinimumSize(QSize(500, 0))
        self.layout_pesquisar_produto_3.setMaximumSize(QSize(700, 16777215))
        self.layout_pesquisar_produto_3.setStyleSheet(u"")
        self.layout_pesquisar_produto_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_pesquisar_produto_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.layout_pesquisar_produto_3)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_3 = QSpacerItem(80, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_3)

        self.input_pesquisar_produto_3 = QLineEdit(self.layout_pesquisar_produto_3)
        self.input_pesquisar_produto_3.setObjectName(u"input_pesquisar_produto_3")
        self.input_pesquisar_produto_3.setMinimumSize(QSize(400, 0))
        self.input_pesquisar_produto_3.setMaximumSize(QSize(16777215, 16777215))
        self.input_pesquisar_produto_3.setStyleSheet(u"")
        self.input_pesquisar_produto_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.input_pesquisar_produto_3, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.btn_pesquisar_produto_3 = QPushButton(self.layout_pesquisar_produto_3)
        self.btn_pesquisar_produto_3.setObjectName(u"btn_pesquisar_produto_3")
        self.btn_pesquisar_produto_3.setMaximumSize(QSize(50, 16777215))
        self.btn_pesquisar_produto_3.setStyleSheet(u"background-color: none;")
        icon10 = QIcon()
        icon10.addFile(u":/icons/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btn_pesquisar_produto_3.setIcon(icon10)
        self.btn_pesquisar_produto_3.setIconSize(QSize(25, 25))

        self.horizontalLayout_10.addWidget(self.btn_pesquisar_produto_3, 0, Qt.AlignmentFlag.AlignRight)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_8)


        self.verticalLayout_21.addWidget(self.layout_pesquisar_produto_3, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.layout_resultado_procurar_produto_1 = QWidget(self.tela_pdv_3_info_principal_4)
        self.layout_resultado_procurar_produto_1.setObjectName(u"layout_resultado_procurar_produto_1")
        sizePolicy1.setHeightForWidth(self.layout_resultado_procurar_produto_1.sizePolicy().hasHeightForWidth())
        self.layout_resultado_procurar_produto_1.setSizePolicy(sizePolicy1)
        self.layout_resultado_procurar_produto_1.setMinimumSize(QSize(350, 300))
        self.layout_resultado_procurar_produto_1.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_11 = QHBoxLayout(self.layout_resultado_procurar_produto_1)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.layout_nome_preco_produto_2 = QFrame(self.layout_resultado_procurar_produto_1)
        self.layout_nome_preco_produto_2.setObjectName(u"layout_nome_preco_produto_2")
        self.layout_nome_preco_produto_2.setStyleSheet(u"font-size:20px;")
        self.layout_nome_preco_produto_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_nome_preco_produto_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.layout_nome_preco_produto_2)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.txt_nome_produto_1 = QLabel(self.layout_nome_preco_produto_2)
        self.txt_nome_produto_1.setObjectName(u"txt_nome_produto_1")
        self.txt_nome_produto_1.setStyleSheet(u"font-size:20px;")

        self.verticalLayout_22.addWidget(self.txt_nome_produto_1)


        self.horizontalLayout_11.addWidget(self.layout_nome_preco_produto_2, 0, Qt.AlignmentFlag.AlignLeft)

        self.frame_3 = QFrame(self.layout_resultado_procurar_produto_1)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"font-size:20px;")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_3)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.txt_quantidade_1 = QLabel(self.frame_3)
        self.txt_quantidade_1.setObjectName(u"txt_quantidade_1")
        self.txt_quantidade_1.setStyleSheet(u"font-size: 20px;")

        self.verticalLayout_23.addWidget(self.txt_quantidade_1)


        self.horizontalLayout_11.addWidget(self.frame_3)

        self.layout_valores_produtos = QFrame(self.layout_resultado_procurar_produto_1)
        self.layout_valores_produtos.setObjectName(u"layout_valores_produtos")
        self.layout_valores_produtos.setStyleSheet(u"font-size:20px;")
        self.layout_valores_produtos.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_valores_produtos.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.layout_valores_produtos)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.txt_valor_1 = QLabel(self.layout_valores_produtos)
        self.txt_valor_1.setObjectName(u"txt_valor_1")
        self.txt_valor_1.setStyleSheet(u"font-size: 20px;")

        self.verticalLayout_24.addWidget(self.txt_valor_1)


        self.horizontalLayout_11.addWidget(self.layout_valores_produtos)


        self.verticalLayout_21.addWidget(self.layout_resultado_procurar_produto_1, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.layout_total_forma_pagamento = QFrame(self.tela_pdv_3_info_principal_4)
        self.layout_total_forma_pagamento.setObjectName(u"layout_total_forma_pagamento")
        self.layout_total_forma_pagamento.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_total_forma_pagamento.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.layout_total_forma_pagamento)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.input_forma_pagamento = QComboBox(self.layout_total_forma_pagamento)
        self.input_forma_pagamento.addItem("")
        self.input_forma_pagamento.addItem("")
        self.input_forma_pagamento.addItem("")
        self.input_forma_pagamento.addItem("")
        self.input_forma_pagamento.setObjectName(u"input_forma_pagamento")
        self.input_forma_pagamento.setMinimumSize(QSize(260, 0))
        self.input_forma_pagamento.setStyleSheet(u"font-size: 20px;")
        self.input_forma_pagamento.setEditable(False)
        self.input_forma_pagamento.setMaxVisibleItems(10)

        self.horizontalLayout_31.addWidget(self.input_forma_pagamento, 0, Qt.AlignmentFlag.AlignLeft)

        self.frame_11 = QFrame(self.layout_total_forma_pagamento)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_14 = QLabel(self.frame_11)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"font-size: 20px;")

        self.horizontalLayout_32.addWidget(self.label_14, 0, Qt.AlignmentFlag.AlignRight)


        self.horizontalLayout_31.addWidget(self.frame_11, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_21.addWidget(self.layout_total_forma_pagamento)

        self.btn_finalizar_compra = QPushButton(self.tela_pdv_3_info_principal_4)
        self.btn_finalizar_compra.setObjectName(u"btn_finalizar_compra")
        self.btn_finalizar_compra.setMinimumSize(QSize(300, 0))

        self.verticalLayout_21.addWidget(self.btn_finalizar_compra, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_19.addWidget(self.tela_pdv_3_info_principal_4)

        self.stackedWidget_2.addWidget(self.tela_pdv_3)

        self.verticalLayout_8.addWidget(self.stackedWidget_2)

        self.stackedWidget.addWidget(self.telapdv)
        self.telaestoque = QWidget()
        self.telaestoque.setObjectName(u"telaestoque")
        self.telaestoque.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.telaestoque)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.stackedWidget_3 = QStackedWidget(self.telaestoque)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.tela_estoque_1 = QWidget()
        self.tela_estoque_1.setObjectName(u"tela_estoque_1")
        self.verticalLayout_25 = QVBoxLayout(self.tela_estoque_1)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.layout_pesquisar_produto_estoque = QWidget(self.tela_estoque_1)
        self.layout_pesquisar_produto_estoque.setObjectName(u"layout_pesquisar_produto_estoque")
        self.verticalLayout_26 = QVBoxLayout(self.layout_pesquisar_produto_estoque)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 9, 0, 0)
        self.layout_pesquisar_produto_estoque_2 = QFrame(self.layout_pesquisar_produto_estoque)
        self.layout_pesquisar_produto_estoque_2.setObjectName(u"layout_pesquisar_produto_estoque_2")
        self.layout_pesquisar_produto_estoque_2.setMinimumSize(QSize(500, 0))
        self.layout_pesquisar_produto_estoque_2.setMaximumSize(QSize(700, 16777215))
        self.layout_pesquisar_produto_estoque_2.setStyleSheet(u"")
        self.layout_pesquisar_produto_estoque_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_pesquisar_produto_estoque_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.layout_pesquisar_produto_estoque_2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_5 = QSpacerItem(115, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_5)

        self.input_pesquisar_produto_4 = QLineEdit(self.layout_pesquisar_produto_estoque_2)
        self.input_pesquisar_produto_4.setObjectName(u"input_pesquisar_produto_4")
        self.input_pesquisar_produto_4.setMinimumSize(QSize(400, 0))
        self.input_pesquisar_produto_4.setMaximumSize(QSize(400, 16777215))
        self.input_pesquisar_produto_4.setStyleSheet(u"")
        self.input_pesquisar_produto_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_12.addWidget(self.input_pesquisar_produto_4, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.btn_pesquisar_produto_4 = QPushButton(self.layout_pesquisar_produto_estoque_2)
        self.btn_pesquisar_produto_4.setObjectName(u"btn_pesquisar_produto_4")
        self.btn_pesquisar_produto_4.setMaximumSize(QSize(50, 16777215))
        self.btn_pesquisar_produto_4.setStyleSheet(u"background-color: none;")
        self.btn_pesquisar_produto_4.setIcon(icon10)
        self.btn_pesquisar_produto_4.setIconSize(QSize(25, 25))

        self.horizontalLayout_12.addWidget(self.btn_pesquisar_produto_4, 0, Qt.AlignmentFlag.AlignRight)

        self.btn_adc_produto_estoque = QPushButton(self.layout_pesquisar_produto_estoque_2)
        self.btn_adc_produto_estoque.setObjectName(u"btn_adc_produto_estoque")
        self.btn_adc_produto_estoque.setStyleSheet(u"background-color: none;")
        icon11 = QIcon()
        icon11.addFile(u":/icons/add.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btn_adc_produto_estoque.setIcon(icon11)
        self.btn_adc_produto_estoque.setIconSize(QSize(20, 20))
        self.btn_adc_produto_estoque.setCheckable(False)

        self.horizontalLayout_12.addWidget(self.btn_adc_produto_estoque)


        self.verticalLayout_26.addWidget(self.layout_pesquisar_produto_estoque_2, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_25.addWidget(self.layout_pesquisar_produto_estoque, 0, Qt.AlignmentFlag.AlignTop)

        self.txt_caso_produto_nao_encontra_estoque = QLabel(self.tela_estoque_1)
        self.txt_caso_produto_nao_encontra_estoque.setObjectName(u"txt_caso_produto_nao_encontra_estoque")

        self.verticalLayout_25.addWidget(self.txt_caso_produto_nao_encontra_estoque, 0, Qt.AlignmentFlag.AlignHCenter)

        self.treeWidget = QTreeWidget(self.tela_estoque_1)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setTextAlignment(5, Qt.AlignCenter);
        __qtreewidgetitem.setTextAlignment(4, Qt.AlignCenter);
        __qtreewidgetitem.setTextAlignment(3, Qt.AlignCenter);
        __qtreewidgetitem.setTextAlignment(2, Qt.AlignCenter);
        __qtreewidgetitem.setTextAlignment(1, Qt.AlignCenter);
        __qtreewidgetitem.setTextAlignment(0, Qt.AlignCenter);
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setMinimumSize(QSize(600, 0))

        self.verticalLayout_25.addWidget(self.treeWidget, 0, Qt.AlignmentFlag.AlignHCenter)

        self.stackedWidget_3.addWidget(self.tela_estoque_1)
        self.tela_estoque_2 = QWidget()
        self.tela_estoque_2.setObjectName(u"tela_estoque_2")
        self.verticalLayout_27 = QVBoxLayout(self.tela_estoque_2)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.widget = QWidget(self.tela_estoque_2)
        self.widget.setObjectName(u"widget")
        self.gridLayout_6 = QGridLayout(self.widget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.input_nome_produto = QLineEdit(self.widget)
        self.input_nome_produto.setObjectName(u"input_nome_produto")
        self.input_nome_produto.setMinimumSize(QSize(400, 0))
        self.input_nome_produto.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.input_nome_produto, 0, 0, 1, 1)

        self.input_quantidade_produto = QLineEdit(self.widget)
        self.input_quantidade_produto.setObjectName(u"input_quantidade_produto")
        self.input_quantidade_produto.setMinimumSize(QSize(400, 0))
        self.input_quantidade_produto.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.input_quantidade_produto, 2, 0, 1, 1)

        self.input_preco_produto = QLineEdit(self.widget)
        self.input_preco_produto.setObjectName(u"input_preco_produto")
        self.input_preco_produto.setMinimumSize(QSize(400, 0))
        self.input_preco_produto.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.input_preco_produto, 0, 1, 1, 1)

        self.input_categoria_produto = QComboBox(self.widget)
        self.input_categoria_produto.addItem("")
        self.input_categoria_produto.addItem("")
        self.input_categoria_produto.addItem("")
        self.input_categoria_produto.setObjectName(u"input_categoria_produto")
        self.input_categoria_produto.setMinimumSize(QSize(400, 0))

        self.gridLayout_6.addWidget(self.input_categoria_produto, 2, 1, 1, 1)

        self.btn_procurar_ft_produto = QPushButton(self.widget)
        self.btn_procurar_ft_produto.setObjectName(u"btn_procurar_ft_produto")

        self.gridLayout_6.addWidget(self.btn_procurar_ft_produto, 4, 0, 1, 1)

        self.img_produto_adc_estoque = QLabel(self.widget)
        self.img_produto_adc_estoque.setObjectName(u"img_produto_adc_estoque")

        self.gridLayout_6.addWidget(self.img_produto_adc_estoque, 4, 1, 1, 1)


        self.verticalLayout_27.addWidget(self.widget)

        self.btn_adc_produto = QPushButton(self.tela_estoque_2)
        self.btn_adc_produto.setObjectName(u"btn_adc_produto")
        self.btn_adc_produto.setMinimumSize(QSize(300, 0))

        self.verticalLayout_27.addWidget(self.btn_adc_produto, 0, Qt.AlignmentFlag.AlignHCenter)

        self.stackedWidget_3.addWidget(self.tela_estoque_2)

        self.verticalLayout_9.addWidget(self.stackedWidget_3)

        self.stackedWidget.addWidget(self.telaestoque)
        self.telarelatorios = QWidget()
        self.telarelatorios.setObjectName(u"telarelatorios")
        self.telarelatorios.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.telarelatorios)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget_3 = QWidget(self.telarelatorios)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_2 = QGridLayout(self.widget_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_10 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.verticalSpacer_10, 4, 1, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.verticalSpacer_9, 0, 1, 1, 1)

        self.layout_relatorios_3 = QFrame(self.widget_3)
        self.layout_relatorios_3.setObjectName(u"layout_relatorios_3")
        self.layout_relatorios_3.setMaximumSize(QSize(300, 300))
        self.layout_relatorios_3.setStyleSheet(u"background-color: rgb(219, 219, 219);\n"
"border-radius: 20px;")
        self.layout_relatorios_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_relatorios_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.layout_relatorios_3)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.txt_produtos_mais_vendidos = QLabel(self.layout_relatorios_3)
        self.txt_produtos_mais_vendidos.setObjectName(u"txt_produtos_mais_vendidos")

        self.verticalLayout_31.addWidget(self.txt_produtos_mais_vendidos, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)


        self.gridLayout_2.addWidget(self.layout_relatorios_3, 3, 1, 1, 1)

        self.layout_relatorios_1 = QFrame(self.widget_3)
        self.layout_relatorios_1.setObjectName(u"layout_relatorios_1")
        self.layout_relatorios_1.setStyleSheet(u"background-color: rgb(219, 219, 219);\n"
"border-radius: 20px;")
        self.layout_relatorios_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_relatorios_1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.layout_relatorios_1)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.txt_vendas_ultimos_6_meses = QLabel(self.layout_relatorios_1)
        self.txt_vendas_ultimos_6_meses.setObjectName(u"txt_vendas_ultimos_6_meses")

        self.verticalLayout_29.addWidget(self.txt_vendas_ultimos_6_meses, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)


        self.gridLayout_2.addWidget(self.layout_relatorios_1, 1, 0, 1, 3)

        self.layout_relatorios_2 = QFrame(self.widget_3)
        self.layout_relatorios_2.setObjectName(u"layout_relatorios_2")
        self.layout_relatorios_2.setMaximumSize(QSize(300, 300))
        self.layout_relatorios_2.setStyleSheet(u"background-color: rgb(219, 219, 219);\n"
"border-radius: 20px;")
        self.layout_relatorios_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_relatorios_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.layout_relatorios_2)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.txt_lucro_prejuizo = QLabel(self.layout_relatorios_2)
        self.txt_lucro_prejuizo.setObjectName(u"txt_lucro_prejuizo")

        self.verticalLayout_30.addWidget(self.txt_lucro_prejuizo, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)


        self.gridLayout_2.addWidget(self.layout_relatorios_2, 3, 0, 1, 1)

        self.layout_relatorios_4 = QFrame(self.widget_3)
        self.layout_relatorios_4.setObjectName(u"layout_relatorios_4")
        self.layout_relatorios_4.setMaximumSize(QSize(300, 300))
        self.layout_relatorios_4.setStyleSheet(u"background-color: rgb(219, 219, 219);\n"
"border-radius: 20px;")
        self.layout_relatorios_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_relatorios_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.layout_relatorios_4)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_4 = QLabel(self.layout_relatorios_4)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_32.addWidget(self.label_4, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)


        self.gridLayout_2.addWidget(self.layout_relatorios_4, 3, 2, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.verticalSpacer_11, 2, 1, 1, 1)


        self.verticalLayout_7.addWidget(self.widget_3)

        self.stackedWidget.addWidget(self.telarelatorios)
        self.telaconfiguracoes = QWidget()
        self.telaconfiguracoes.setObjectName(u"telaconfiguracoes")
        self.telaconfiguracoes.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.telaconfiguracoes)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.tabWidget = QTabWidget(self.telaconfiguracoes)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tela_config_1 = QWidget()
        self.tela_config_1.setObjectName(u"tela_config_1")
        self.verticalLayout_33 = QVBoxLayout(self.tela_config_1)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.stackedWidget_4 = QStackedWidget(self.tela_config_1)
        self.stackedWidget_4.setObjectName(u"stackedWidget_4")
        self.config_usuarios = QWidget()
        self.config_usuarios.setObjectName(u"config_usuarios")
        self.verticalLayout_35 = QVBoxLayout(self.config_usuarios)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.treeWidget_2 = QTreeWidget(self.config_usuarios)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setTextAlignment(7, Qt.AlignCenter);
        __qtreewidgetitem1.setTextAlignment(6, Qt.AlignCenter);
        __qtreewidgetitem1.setTextAlignment(5, Qt.AlignCenter);
        __qtreewidgetitem1.setTextAlignment(4, Qt.AlignCenter);
        __qtreewidgetitem1.setTextAlignment(3, Qt.AlignCenter);
        __qtreewidgetitem1.setTextAlignment(2, Qt.AlignCenter);
        __qtreewidgetitem1.setTextAlignment(1, Qt.AlignCenter);
        __qtreewidgetitem1.setTextAlignment(0, Qt.AlignCenter);
        self.treeWidget_2.setHeaderItem(__qtreewidgetitem1)
        QTreeWidgetItem(self.treeWidget_2)
        QTreeWidgetItem(self.treeWidget_2)
        QTreeWidgetItem(self.treeWidget_2)
        QTreeWidgetItem(self.treeWidget_2)
        QTreeWidgetItem(self.treeWidget_2)
        QTreeWidgetItem(self.treeWidget_2)
        QTreeWidgetItem(self.treeWidget_2)
        QTreeWidgetItem(self.treeWidget_2)
        QTreeWidgetItem(self.treeWidget_2)
        QTreeWidgetItem(self.treeWidget_2)
        QTreeWidgetItem(self.treeWidget_2)
        QTreeWidgetItem(self.treeWidget_2)
        self.treeWidget_2.setObjectName(u"treeWidget_2")
        self.treeWidget_2.setMinimumSize(QSize(850, 300))
        self.treeWidget_2.setStyleSheet(u"")

        self.verticalLayout_35.addWidget(self.treeWidget_2, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.btn_adc_user = QPushButton(self.config_usuarios)
        self.btn_adc_user.setObjectName(u"btn_adc_user")
        self.btn_adc_user.setMinimumSize(QSize(300, 0))

        self.verticalLayout_35.addWidget(self.btn_adc_user, 0, Qt.AlignmentFlag.AlignHCenter)

        self.stackedWidget_4.addWidget(self.config_usuarios)
        self.config_usuarios_2 = QWidget()
        self.config_usuarios_2.setObjectName(u"config_usuarios_2")
        self.verticalLayout_36 = QVBoxLayout(self.config_usuarios_2)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.layout_adc_usuario = QFrame(self.config_usuarios_2)
        self.layout_adc_usuario.setObjectName(u"layout_adc_usuario")
        self.layout_adc_usuario.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_adc_usuario.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.layout_adc_usuario)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.btn_adc_usuario = QPushButton(self.layout_adc_usuario)
        self.btn_adc_usuario.setObjectName(u"btn_adc_usuario")

        self.gridLayout_3.addWidget(self.btn_adc_usuario, 7, 0, 1, 1)

        self.input_senha_adc_usuario = QLineEdit(self.layout_adc_usuario)
        self.input_senha_adc_usuario.setObjectName(u"input_senha_adc_usuario")
        self.input_senha_adc_usuario.setMaximumSize(QSize(400, 16777215))
        self.input_senha_adc_usuario.setStyleSheet(u"")
        self.input_senha_adc_usuario.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_senha_adc_usuario.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.input_senha_adc_usuario, 2, 0, 1, 1)

        self.input_nome_adc_usuario = QLineEdit(self.layout_adc_usuario)
        self.input_nome_adc_usuario.setObjectName(u"input_nome_adc_usuario")
        self.input_nome_adc_usuario.setMaximumSize(QSize(400, 16777215))
        font = QFont()
        font.setWeight(QFont.DemiBold)
        font.setItalic(False)
        self.input_nome_adc_usuario.setFont(font)
        self.input_nome_adc_usuario.setStyleSheet(u"")
        self.input_nome_adc_usuario.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.input_nome_adc_usuario, 0, 0, 1, 1)

        self.btn_procurar_ft_adc_usuario = QPushButton(self.layout_adc_usuario)
        self.btn_procurar_ft_adc_usuario.setObjectName(u"btn_procurar_ft_adc_usuario")
        self.btn_procurar_ft_adc_usuario.setMinimumSize(QSize(250, 0))

        self.gridLayout_3.addWidget(self.btn_procurar_ft_adc_usuario, 5, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.input_telefone_adc_usuario = QLineEdit(self.layout_adc_usuario)
        self.input_telefone_adc_usuario.setObjectName(u"input_telefone_adc_usuario")
        self.input_telefone_adc_usuario.setMaximumSize(QSize(400, 16777215))
        self.input_telefone_adc_usuario.setStyleSheet(u"")
        self.input_telefone_adc_usuario.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.input_telefone_adc_usuario, 4, 0, 1, 1)

        self.input_email_adc_usuario = QLineEdit(self.layout_adc_usuario)
        self.input_email_adc_usuario.setObjectName(u"input_email_adc_usuario")
        self.input_email_adc_usuario.setMaximumSize(QSize(400, 16777215))
        self.input_email_adc_usuario.setStyleSheet(u"")
        self.input_email_adc_usuario.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.input_email_adc_usuario, 1, 0, 1, 1)

        self.input_cpf_adc_usuario = QLineEdit(self.layout_adc_usuario)
        self.input_cpf_adc_usuario.setObjectName(u"input_cpf_adc_usuario")
        self.input_cpf_adc_usuario.setMaximumSize(QSize(400, 16777215))
        self.input_cpf_adc_usuario.setStyleSheet(u"")
        self.input_cpf_adc_usuario.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.input_cpf_adc_usuario, 3, 0, 1, 1)

        self.label_img_adc_usuario = QLabel(self.layout_adc_usuario)
        self.label_img_adc_usuario.setObjectName(u"label_img_adc_usuario")

        self.gridLayout_3.addWidget(self.label_img_adc_usuario, 6, 0, 1, 1)


        self.verticalLayout_36.addWidget(self.layout_adc_usuario)

        self.stackedWidget_4.addWidget(self.config_usuarios_2)

        self.verticalLayout_33.addWidget(self.stackedWidget_4)

        self.tabWidget.addTab(self.tela_config_1, "")
        self.tela_config_2 = QWidget()
        self.tela_config_2.setObjectName(u"tela_config_2")
        self.verticalLayout = QVBoxLayout(self.tela_config_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget_5 = QStackedWidget(self.tela_config_2)
        self.stackedWidget_5.setObjectName(u"stackedWidget_5")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_37 = QVBoxLayout(self.page)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.widget_4 = QWidget(self.page)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_38 = QVBoxLayout(self.widget_4)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.tabela_categoria = QTreeWidget(self.widget_4)
        __qtreewidgetitem2 = QTreeWidgetItem()
        __qtreewidgetitem2.setTextAlignment(1, Qt.AlignCenter);
        __qtreewidgetitem2.setTextAlignment(0, Qt.AlignCenter);
        self.tabela_categoria.setHeaderItem(__qtreewidgetitem2)
        self.tabela_categoria.setObjectName(u"tabela_categoria")

        self.verticalLayout_38.addWidget(self.tabela_categoria, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.btn_adc_categoria = QPushButton(self.widget_4)
        self.btn_adc_categoria.setObjectName(u"btn_adc_categoria")

        self.verticalLayout_38.addWidget(self.btn_adc_categoria, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_37.addWidget(self.widget_4)

        self.stackedWidget_5.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_39 = QVBoxLayout(self.page_2)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.layout_adc_categoria = QFrame(self.page_2)
        self.layout_adc_categoria.setObjectName(u"layout_adc_categoria")
        self.layout_adc_categoria.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_adc_categoria.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.layout_adc_categoria)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.input_nome_adc_categoria = QLineEdit(self.layout_adc_categoria)
        self.input_nome_adc_categoria.setObjectName(u"input_nome_adc_categoria")
        self.input_nome_adc_categoria.setMaximumSize(QSize(400, 16777215))
        self.input_nome_adc_categoria.setStyleSheet(u"")
        self.input_nome_adc_categoria.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.input_nome_adc_categoria, 0, 0, 1, 1)

        self.btn_adc_categoria_2 = QPushButton(self.layout_adc_categoria)
        self.btn_adc_categoria_2.setObjectName(u"btn_adc_categoria_2")

        self.gridLayout_5.addWidget(self.btn_adc_categoria_2, 1, 0, 1, 1)


        self.verticalLayout_39.addWidget(self.layout_adc_categoria)

        self.stackedWidget_5.addWidget(self.page_2)

        self.verticalLayout.addWidget(self.stackedWidget_5)

        self.tabWidget.addTab(self.tela_config_2, "")

        self.verticalLayout_10.addWidget(self.tabWidget)

        self.stackedWidget.addWidget(self.telaconfiguracoes)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self._info_principal)


        self.gridLayout_4.addWidget(self.mainbody, 1, 0, 1, 1)

        TelaPrincipal.setCentralWidget(self.centralwidget)

        self.retranslateUi(TelaPrincipal)

        self.stackedWidget.setCurrentIndex(2)
        self.stackedWidget_2.setCurrentIndex(2)
        self.input_forma_pagamento.setCurrentIndex(-1)
        self.stackedWidget_3.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget_4.setCurrentIndex(0)
        self.stackedWidget_5.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(TelaPrincipal)
    # setupUi

    def retranslateUi(self, TelaPrincipal):
        TelaPrincipal.setWindowTitle(QCoreApplication.translate("TelaPrincipal", u"MainWindow", None))
        self.img_logo.setText(QCoreApplication.translate("TelaPrincipal", u"TextLabel", None))
        self.txt_ola_user.setText(QCoreApplication.translate("TelaPrincipal", u"Ol\u00e1, Admin", None))
        self.btn_sair.setText("")
        self.btn_tela_principal.setText(QCoreApplication.translate("TelaPrincipal", u"TELA PRINCIPAL", None))
        self.btn_pdv.setText(QCoreApplication.translate("TelaPrincipal", u"PDV", None))
        self.btn_estoque.setText(QCoreApplication.translate("TelaPrincipal", u"ESTOQUE", None))
        self.btn_relatorios.setText(QCoreApplication.translate("TelaPrincipal", u"RELATORIOS", None))
        self.btn_configuracoes.setText(QCoreApplication.translate("TelaPrincipal", u"CONFIGURA\u00c7\u00d5ES", None))
        self.txt_produtos_baixo_estoque.setText(QCoreApplication.translate("TelaPrincipal", u"Produtos com Baixo Estoque", None))
        self.txt_produtos_baixo_estoque_db.setText(QCoreApplication.translate("TelaPrincipal", u"TextLabel", None))
        self.txt_vendas_semana.setText(QCoreApplication.translate("TelaPrincipal", u"Vendas da Semana", None))
        self.txt_vendas_semana_db.setText(QCoreApplication.translate("TelaPrincipal", u"TextLabel", None))
        self.txt_vendasdia.setText(QCoreApplication.translate("TelaPrincipal", u"Vendas do Dia", None))
        self.txt_vendas_dia_db.setText(QCoreApplication.translate("TelaPrincipal", u"TextLabel", None))
        self.txt_vendas_mes.setText(QCoreApplication.translate("TelaPrincipal", u"Vendas do M\u00eas", None))
        self.txt_vendas_mes_db.setText(QCoreApplication.translate("TelaPrincipal", u"TextLabel", None))
        self.input_pesquisar_produto.setPlaceholderText(QCoreApplication.translate("TelaPrincipal", u"Procurar Produto", None))
        self.btn_pesquisar_produto.setText("")
        self.txt_caso_nao_produto_encontrado.setText("")
        self.input_pesquisar_produto_2.setPlaceholderText(QCoreApplication.translate("TelaPrincipal", u"Procurar Produto", None))
        self.btn_pesquisar_produto_2.setText("")
        self.txt_nome_preco_produto.setText(QCoreApplication.translate("TelaPrincipal", u"Ma\u00e7\u00e3 R$1,00", None))
        self.btn_menos.setText("")
        self.txt_quantidade.setText(QCoreApplication.translate("TelaPrincipal", u"  01", None))
        self.btn_mais.setText("")
        self.btn_adc_carrinho.setText(QCoreApplication.translate("TelaPrincipal", u"Adcionar ao Carrinho", None))
        self.input_pesquisar_produto_3.setPlaceholderText(QCoreApplication.translate("TelaPrincipal", u"Procurar Produto", None))
        self.btn_pesquisar_produto_3.setText("")
        self.txt_nome_produto_1.setText(QCoreApplication.translate("TelaPrincipal", u"Ma\u00e7\u00e3 ", None))
        self.txt_quantidade_1.setText(QCoreApplication.translate("TelaPrincipal", u"QTD. 01", None))
        self.txt_valor_1.setText(QCoreApplication.translate("TelaPrincipal", u"R$1,00", None))
        self.input_forma_pagamento.setItemText(0, QCoreApplication.translate("TelaPrincipal", u"Pix", None))
        self.input_forma_pagamento.setItemText(1, QCoreApplication.translate("TelaPrincipal", u"Cart\u00e3o de Cr\u00e9dito", None))
        self.input_forma_pagamento.setItemText(2, QCoreApplication.translate("TelaPrincipal", u"Cart\u00e3o de D\u00e9bito", None))
        self.input_forma_pagamento.setItemText(3, QCoreApplication.translate("TelaPrincipal", u"Dinheiro", None))

        self.input_forma_pagamento.setCurrentText("")
        self.input_forma_pagamento.setPlaceholderText(QCoreApplication.translate("TelaPrincipal", u"Forma de Pagamento", None))
        self.label_14.setText(QCoreApplication.translate("TelaPrincipal", u" TOTAL R$55,00", None))
        self.btn_finalizar_compra.setText(QCoreApplication.translate("TelaPrincipal", u"Finalizar Compra", None))
        self.input_pesquisar_produto_4.setPlaceholderText(QCoreApplication.translate("TelaPrincipal", u"Procurar Produto", None))
        self.btn_pesquisar_produto_4.setText("")
        self.btn_adc_produto_estoque.setText("")
        self.txt_caso_produto_nao_encontra_estoque.setText("")
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("TelaPrincipal", u"IMAGEM", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("TelaPrincipal", u"CATEGORIA", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("TelaPrincipal", u"QUANTIDADE", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("TelaPrincipal", u"PRE\u00c7O", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("TelaPrincipal", u"NOME", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("TelaPrincipal", u"ID", None));
        self.input_nome_produto.setPlaceholderText(QCoreApplication.translate("TelaPrincipal", u"NOME", None))
        self.input_quantidade_produto.setPlaceholderText(QCoreApplication.translate("TelaPrincipal", u"QUANTIDADE", None))
        self.input_preco_produto.setInputMask("")
        self.input_preco_produto.setPlaceholderText(QCoreApplication.translate("TelaPrincipal", u"PRE\u00c7O UN.", None))
        self.input_categoria_produto.setItemText(0, QCoreApplication.translate("TelaPrincipal", u"COMIDA", None))
        self.input_categoria_produto.setItemText(1, QCoreApplication.translate("TelaPrincipal", u"ROUPA", None))
        self.input_categoria_produto.setItemText(2, QCoreApplication.translate("TelaPrincipal", u"LIMPEZA", None))

        self.input_categoria_produto.setPlaceholderText(QCoreApplication.translate("TelaPrincipal", u"CATEGORIA", None))
        self.btn_procurar_ft_produto.setText(QCoreApplication.translate("TelaPrincipal", u"Procurar Foto do Produto", None))
        self.img_produto_adc_estoque.setText("")
        self.btn_adc_produto.setText(QCoreApplication.translate("TelaPrincipal", u"Adcionar Produto", None))
        self.txt_produtos_mais_vendidos.setText(QCoreApplication.translate("TelaPrincipal", u"Produtos mais Vendidos", None))
        self.txt_vendas_ultimos_6_meses.setText(QCoreApplication.translate("TelaPrincipal", u"Vendas dos Ultimos 6 meses", None))
        self.txt_lucro_prejuizo.setText(QCoreApplication.translate("TelaPrincipal", u"Lucro/Prejuizo", None))
        self.label_4.setText(QCoreApplication.translate("TelaPrincipal", u"TextLabel", None))
        ___qtreewidgetitem1 = self.treeWidget_2.headerItem()
        ___qtreewidgetitem1.setText(7, QCoreApplication.translate("TelaPrincipal", u"Local IMG", None));
        ___qtreewidgetitem1.setText(6, QCoreApplication.translate("TelaPrincipal", u"Cargo", None));
        ___qtreewidgetitem1.setText(5, QCoreApplication.translate("TelaPrincipal", u"Sexo", None));
        ___qtreewidgetitem1.setText(4, QCoreApplication.translate("TelaPrincipal", u"Data Contrata\u00e7\u00e3o", None));
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("TelaPrincipal", u"Idade", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("TelaPrincipal", u"CPF", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("TelaPrincipal", u"Email", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("TelaPrincipal", u"Nome", None));

        __sortingEnabled = self.treeWidget_2.isSortingEnabled()
        self.treeWidget_2.setSortingEnabled(False)
        ___qtreewidgetitem2 = self.treeWidget_2.topLevelItem(0)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("TelaPrincipal", u"1", None));
        ___qtreewidgetitem3 = self.treeWidget_2.topLevelItem(1)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("TelaPrincipal", u"New Item", None));
        ___qtreewidgetitem4 = self.treeWidget_2.topLevelItem(2)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("TelaPrincipal", u"New Item", None));
        ___qtreewidgetitem5 = self.treeWidget_2.topLevelItem(3)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("TelaPrincipal", u"New Item", None));
        ___qtreewidgetitem6 = self.treeWidget_2.topLevelItem(4)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("TelaPrincipal", u"New Item", None));
        ___qtreewidgetitem7 = self.treeWidget_2.topLevelItem(5)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("TelaPrincipal", u"New Item", None));
        ___qtreewidgetitem8 = self.treeWidget_2.topLevelItem(6)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("TelaPrincipal", u"New Item", None));
        ___qtreewidgetitem9 = self.treeWidget_2.topLevelItem(7)
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("TelaPrincipal", u"New Item", None));
        ___qtreewidgetitem10 = self.treeWidget_2.topLevelItem(8)
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("TelaPrincipal", u"New Item", None));
        ___qtreewidgetitem11 = self.treeWidget_2.topLevelItem(9)
        ___qtreewidgetitem11.setText(0, QCoreApplication.translate("TelaPrincipal", u"New Item", None));
        ___qtreewidgetitem12 = self.treeWidget_2.topLevelItem(10)
        ___qtreewidgetitem12.setText(0, QCoreApplication.translate("TelaPrincipal", u"New Item", None));
        ___qtreewidgetitem13 = self.treeWidget_2.topLevelItem(11)
        ___qtreewidgetitem13.setText(0, QCoreApplication.translate("TelaPrincipal", u"New Item", None));
        self.treeWidget_2.setSortingEnabled(__sortingEnabled)

        self.btn_adc_user.setText(QCoreApplication.translate("TelaPrincipal", u"Adcionar Usuario", None))
        self.btn_adc_usuario.setText(QCoreApplication.translate("TelaPrincipal", u"Criar Usuario", None))
        self.input_senha_adc_usuario.setPlaceholderText(QCoreApplication.translate("TelaPrincipal", u"Senha", None))
        self.input_nome_adc_usuario.setPlaceholderText(QCoreApplication.translate("TelaPrincipal", u"Nome", None))
        self.btn_procurar_ft_adc_usuario.setText(QCoreApplication.translate("TelaPrincipal", u"Procurar Foto", None))
        self.input_telefone_adc_usuario.setInputMask("")
        self.input_telefone_adc_usuario.setPlaceholderText(QCoreApplication.translate("TelaPrincipal", u"Telefone", None))
        self.input_email_adc_usuario.setPlaceholderText(QCoreApplication.translate("TelaPrincipal", u"Email", None))
        self.input_cpf_adc_usuario.setPlaceholderText(QCoreApplication.translate("TelaPrincipal", u"CPF", None))
        self.label_img_adc_usuario.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tela_config_1), QCoreApplication.translate("TelaPrincipal", u"Tab 1", None))
        ___qtreewidgetitem14 = self.tabela_categoria.headerItem()
        ___qtreewidgetitem14.setText(1, QCoreApplication.translate("TelaPrincipal", u"Categorias", None));
        ___qtreewidgetitem14.setText(0, QCoreApplication.translate("TelaPrincipal", u"ID", None));
        self.btn_adc_categoria.setText(QCoreApplication.translate("TelaPrincipal", u"Adicionar Categoria", None))
        self.input_nome_adc_categoria.setInputMask("")
        self.input_nome_adc_categoria.setText("")
        self.input_nome_adc_categoria.setPlaceholderText(QCoreApplication.translate("TelaPrincipal", u"Nome da Categoria", None))
        self.btn_adc_categoria_2.setText(QCoreApplication.translate("TelaPrincipal", u"Criar Categoria", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tela_config_2), QCoreApplication.translate("TelaPrincipal", u"Page", None))
    # retranslateUi

