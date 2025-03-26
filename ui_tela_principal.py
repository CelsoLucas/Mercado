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
    QMainWindow, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QTabWidget,
    QTextEdit, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)
from imgs import icons_rc

class Ui_TelaPrincipal(object):
    def setupUi(self, TelaPrincipal):
        if not TelaPrincipal.objectName():
            TelaPrincipal.setObjectName(u"TelaPrincipal")
        TelaPrincipal.resize(1476, 835)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TelaPrincipal.sizePolicy().hasHeightForWidth())
        TelaPrincipal.setSizePolicy(sizePolicy)
        TelaPrincipal.setStyleSheet(u"/* Estilo geral para a janela principal */\n"
"QMainWindow {\n"
"    background-color: #F5F6FA;\n"
"}\n"
"\n"
"/* Menu superior */\n"
"#menu {\n"
"    background-color: #FFFFFF;\n"
"    border-bottom: 1px solid #E0E4E8;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"#img_logo {\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #2D3748;\n"
"}\n"
"\n"
"#txt_ola_user {\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"    font-size: 16px;\n"
"    color: #4A5568;\n"
"}\n"
"\n"
"#btn_sair {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"#btn_sair:hover {\n"
"    background-color: #EDF2F7;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* Menu lateral */\n"
"#menu_lateral {\n"
"    background-color: #2D3748;\n"
"    border-right: 1px solid #E0E4E8;\n"
"}\n"
"\n"
"#btn_tela_principal, #btn_pdv, #btn_estoque, #btn_relatorios, #btn_configuracoes {\n"
"    background-color: #2D3748;\n"
"    color: #E2E8F0;\n"
"    font"
                        "-family: \"Segoe UI\", sans-serif;\n"
"    font-size: 16px;\n"
"    font-weight: 500;\n"
"    padding: 15px;\n"
"    text-align: left;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    margin: 5px 10px;\n"
"}\n"
"\n"
"#btn_tela_principal:hover, #btn_pdv:hover, #btn_estoque:hover, \n"
"#btn_relatorios:hover, #btn_configuracoes:hover {\n"
"    background-color: #4A5568;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"/* \u00c1rea principal */\n"
"#_info_principal {\n"
"    background-color: #F5F6FA;\n"
"    padding: 20px;\n"
"}\n"
"\n"
"/* Bot\u00f5es gerais */\n"
"QPushButton {\n"
"    background-color: #4C51BF;\n"
"    color: #FFFFFF;\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"    padding: 10px 20px;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5A67D8;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #434190;\n"
"}\n"
"\n"
"/* Inputs */\n"
"QLineEdit, QTextEdit {\n"
"    ba"
                        "ckground-color: #FFFFFF;\n"
"    border: 1px solid #E2E8F0;\n"
"    border-radius: 6px;\n"
"    padding: 8px;\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"    font-size: 14px;\n"
"    color: #2D3748;\n"
"}\n"
"\n"
"QLineEdit:focus, QTextEdit:focus {\n"
"    border: 1px solid #4C51BF;\n"
"}\n"
"\n"
"/* ComboBox */\n"
"QComboBox {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #E2E8F0;\n"
"    border-radius: 6px;\n"
"    padding: 8px;\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"    font-size: 14px;\n"
"    color: #2D3748;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #CBD5E0;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"    width: 20px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #E2E8F0;\n"
"    selection-background-color: #4C51BF;\n"
"    selection-color: #FFFFFF;\n"
"}\n"
"\n"
"/* Frames */\n"
"QFrame {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#layout_dados_sem_tabela, #lado_es"
                        "querdo, #lado_direito {\n"
"    background-color: #FFFFFF;\n"
"    border-radius: 10px;\n"
"    padding: 15px;\n"
"}\n"
"\n"
"/* Labels */\n"
"QLabel {\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"    color: #2D3748;\n"
"}\n"
"\n"
"#txt_resumo_mov, #txt_mov_gaveta, #txt_recebimento_vendas {\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"#txt_data, #txt_abertura_db, #txt_operador_db {\n"
"    font-size: 14px;\n"
"    color: #4A5568;\n"
"}\n"
"\n"
"/* Tabelas */\n"
"QTreeWidget {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #E2E8F0;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QTreeWidget::item {\n"
"    padding: 8px;\n"
"}\n"
"\n"
"QTreeWidget::item:hover {\n"
"    background-color: #EDF2F7;\n"
"}\n"
"\n"
"QTreeWidget::item:selected {\n"
"    background-color: #4C51BF;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #E2E8F0;\n"
"    padding"
                        ": 8px;\n"
"    border: none;\n"
"    font-weight: bold;\n"
"    color: #2D3748;\n"
"}\n"
"\n"
"/* Scroll Area */\n"
"QScrollArea {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background: #E2E8F0;\n"
"    width: 10px;\n"
"    margin: 0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #A0AEC0;\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    height: 0;\n"
"}\n"
"\n"
"/* Tab Widget */\n"
"QTabWidget::pane {\n"
"    border: 1px solid #E2E8F0;\n"
"    background-color: #FFFFFF;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: #E2E8F0;\n"
"    color: #4A5568;\n"
"    padding: 10px 20px;\n"
"    margin-right: 2px;\n"
"    border-top-left-radius: 6px;\n"
"    border-top-right-radius: 6px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: #FFFFFF;\n"
"    color: #2D3748;\n"
""
                        "    border-bottom: 2px solid #4C51BF;\n"
"}\n"
"\n"
"QTabBar::tab:hover:!selected {\n"
"    background-color: #EDF2F7;\n"
"}\n"
"\n"
"/* Estilo espec\u00edfico para relat\u00f3rios */\n"
"#layout_relatorios_1, #layout_relatorios_2, #layout_relatorios_3, #layout_relatorios_4 {\n"
"    background-color: #FFFFFF;\n"
"    border-radius: 10px;\n"
"    padding: 15px;\n"
"}\n"
"\n"
"/* Bot\u00f5es de a\u00e7\u00e3o (ex.: Abrir Caixa, Fechar Caixa) */\n"
"#btn_abrir_caixa, #btn_fechar_caixa, #btn_sangria, #btn_suprimento {\n"
"    background-color: #38A169;\n"
"}\n"
"\n"
"#btn_abrir_caixa:hover, #btn_fechar_caixa:hover, #btn_sangria:hover, #btn_suprimento:hover {\n"
"    background-color: #48BB78;\n"
"}\n"
"\n"
"/* Bot\u00f5es de cancelar */\n"
"#btn_cancelar_sangria, #btn_cancelar_suprimento {\n"
"    background-color: #E53E3E;\n"
"}\n"
"\n"
"#btn_cancelar_sangria:hover, #btn_cancelar_suprimento:hover {\n"
"    background-color: #F56565;\n"
"}")
        self.centralwidget = QWidget(TelaPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_42 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
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
        self.img_logo.setMinimumSize(QSize(300, 55))
        self.img_logo.setMaximumSize(QSize(300, 16777215))
        self.img_logo.setPixmap(QPixmap(u":/icons/Design sem nome (8).png"))
        self.img_logo.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.img_logo)


        self.horizontalLayout.addWidget(self.layout_menu_lado_direito, 0, Qt.AlignmentFlag.AlignLeft)

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


        self.verticalLayout_42.addWidget(self.menu)

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

        self.verticalLayout_4.addWidget(self.btn_tela_principal)

        self.btn_pdv = QPushButton(self.frame)
        self.btn_pdv.setObjectName(u"btn_pdv")
        self.btn_pdv.setMinimumSize(QSize(200, 50))
        self.btn_pdv.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.btn_pdv)

        self.btn_estoque = QPushButton(self.frame)
        self.btn_estoque.setObjectName(u"btn_estoque")
        self.btn_estoque.setMinimumSize(QSize(200, 50))
        self.btn_estoque.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.btn_estoque)

        self.btn_relatorios = QPushButton(self.frame)
        self.btn_relatorios.setObjectName(u"btn_relatorios")
        self.btn_relatorios.setMinimumSize(QSize(200, 50))
        self.btn_relatorios.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.btn_relatorios)

        self.btn_configuracoes = QPushButton(self.frame)
        self.btn_configuracoes.setObjectName(u"btn_configuracoes")
        self.btn_configuracoes.setMinimumSize(QSize(200, 50))
        self.btn_configuracoes.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.btn_configuracoes)

        self.btn_modo_claro_escuro = QComboBox(self.frame)
        self.btn_modo_claro_escuro.addItem("")
        self.btn_modo_claro_escuro.addItem("")
        self.btn_modo_claro_escuro.setObjectName(u"btn_modo_claro_escuro")
        self.btn_modo_claro_escuro.setMinimumSize(QSize(150, 0))

        self.verticalLayout_4.addWidget(self.btn_modo_claro_escuro, 0, Qt.AlignmentFlag.AlignHCenter)


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
        self.stackedWidget_7 = QStackedWidget(self.telaprincipal)
        self.stackedWidget_7.setObjectName(u"stackedWidget_7")
        self.tela_principal_opcs = QWidget()
        self.tela_principal_opcs.setObjectName(u"tela_principal_opcs")
        self.verticalLayout_11 = QVBoxLayout(self.tela_principal_opcs)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.layout_btn_opcs = QFrame(self.tela_principal_opcs)
        self.layout_btn_opcs.setObjectName(u"layout_btn_opcs")
        self.layout_btn_opcs.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_btn_opcs.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.layout_btn_opcs)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_btn_abrir_fechar = QFrame(self.layout_btn_opcs)
        self.frame_btn_abrir_fechar.setObjectName(u"frame_btn_abrir_fechar")
        self.frame_btn_abrir_fechar.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_btn_abrir_fechar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_btn_abrir_fechar)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.btn_abrir_caixa = QPushButton(self.frame_btn_abrir_fechar)
        self.btn_abrir_caixa.setObjectName(u"btn_abrir_caixa")

        self.horizontalLayout_14.addWidget(self.btn_abrir_caixa)

        self.btn_fechar_caixa = QPushButton(self.frame_btn_abrir_fechar)
        self.btn_fechar_caixa.setObjectName(u"btn_fechar_caixa")

        self.horizontalLayout_14.addWidget(self.btn_fechar_caixa)


        self.verticalLayout_12.addWidget(self.frame_btn_abrir_fechar)

        self.frame_btn_sangria_suprimento = QFrame(self.layout_btn_opcs)
        self.frame_btn_sangria_suprimento.setObjectName(u"frame_btn_sangria_suprimento")
        self.frame_btn_sangria_suprimento.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_btn_sangria_suprimento.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_btn_sangria_suprimento)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.btn_sangria = QPushButton(self.frame_btn_sangria_suprimento)
        self.btn_sangria.setObjectName(u"btn_sangria")

        self.horizontalLayout_15.addWidget(self.btn_sangria)

        self.btn_suprimento = QPushButton(self.frame_btn_sangria_suprimento)
        self.btn_suprimento.setObjectName(u"btn_suprimento")

        self.horizontalLayout_15.addWidget(self.btn_suprimento)


        self.verticalLayout_12.addWidget(self.frame_btn_sangria_suprimento)


        self.verticalLayout_11.addWidget(self.layout_btn_opcs, 0, Qt.AlignmentFlag.AlignTop)

        self.layout_txts = QFrame(self.tela_principal_opcs)
        self.layout_txts.setObjectName(u"layout_txts")
        self.layout_txts.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_txts.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.layout_txts)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.txt_resumo_mov = QLabel(self.layout_txts)
        self.txt_resumo_mov.setObjectName(u"txt_resumo_mov")

        self.horizontalLayout_31.addWidget(self.txt_resumo_mov)

        self.txt_data = QLabel(self.layout_txts)
        self.txt_data.setObjectName(u"txt_data")

        self.horizontalLayout_31.addWidget(self.txt_data)

        self.txt_abertura_db = QLabel(self.layout_txts)
        self.txt_abertura_db.setObjectName(u"txt_abertura_db")

        self.horizontalLayout_31.addWidget(self.txt_abertura_db)

        self.txt_operador_db = QLabel(self.layout_txts)
        self.txt_operador_db.setObjectName(u"txt_operador_db")

        self.horizontalLayout_31.addWidget(self.txt_operador_db)


        self.verticalLayout_11.addWidget(self.layout_txts)

        self.layout_dados_mov = QFrame(self.tela_principal_opcs)
        self.layout_dados_mov.setObjectName(u"layout_dados_mov")
        sizePolicy1.setHeightForWidth(self.layout_dados_mov.sizePolicy().hasHeightForWidth())
        self.layout_dados_mov.setSizePolicy(sizePolicy1)
        self.layout_dados_mov.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_dados_mov.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.layout_dados_mov)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.layout_dados_sem_tabela = QFrame(self.layout_dados_mov)
        self.layout_dados_sem_tabela.setObjectName(u"layout_dados_sem_tabela")
        self.layout_dados_sem_tabela.setMinimumSize(QSize(0, 250))
        self.layout_dados_sem_tabela.setMaximumSize(QSize(16777215, 400))
        self.layout_dados_sem_tabela.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_dados_sem_tabela.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.layout_dados_sem_tabela)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.lado_esquerdo = QFrame(self.layout_dados_sem_tabela)
        self.lado_esquerdo.setObjectName(u"lado_esquerdo")
        self.lado_esquerdo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lado_esquerdo.setFrameShape(QFrame.Shape.StyledPanel)
        self.lado_esquerdo.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.lado_esquerdo)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.lado_esquerdo_2 = QFrame(self.lado_esquerdo)
        self.lado_esquerdo_2.setObjectName(u"lado_esquerdo_2")
        self.lado_esquerdo_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.lado_esquerdo_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.lado_esquerdo_2)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.icon_recebimento_vendas = QLabel(self.lado_esquerdo_2)
        self.icon_recebimento_vendas.setObjectName(u"icon_recebimento_vendas")
        self.icon_recebimento_vendas.setMaximumSize(QSize(100, 100))
        self.icon_recebimento_vendas.setPixmap(QPixmap(u":/icons/salary_477833.png"))
        self.icon_recebimento_vendas.setScaledContents(True)

        self.verticalLayout_52.addWidget(self.icon_recebimento_vendas)

        self.txt_recebimento_vendas = QLabel(self.lado_esquerdo_2)
        self.txt_recebimento_vendas.setObjectName(u"txt_recebimento_vendas")
        self.txt_recebimento_vendas.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_52.addWidget(self.txt_recebimento_vendas, 0, Qt.AlignmentFlag.AlignLeft)

        self.txt_total_vendas_db = QLabel(self.lado_esquerdo_2)
        self.txt_total_vendas_db.setObjectName(u"txt_total_vendas_db")
        self.txt_total_vendas_db.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_52.addWidget(self.txt_total_vendas_db, 0, Qt.AlignmentFlag.AlignLeft)

        self.verticalSpacer_4 = QSpacerItem(20, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_52.addItem(self.verticalSpacer_4)


        self.horizontalLayout_19.addWidget(self.lado_esquerdo_2)

        self.lado_esquerdo_3 = QFrame(self.lado_esquerdo)
        self.lado_esquerdo_3.setObjectName(u"lado_esquerdo_3")
        self.lado_esquerdo_3.setStyleSheet(u"")
        self.lado_esquerdo_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.lado_esquerdo_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.lado_esquerdo_3)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_53.addItem(self.verticalSpacer_7)

        self.layout_pix = QFrame(self.lado_esquerdo_3)
        self.layout_pix.setObjectName(u"layout_pix")
        self.layout_pix.setMaximumSize(QSize(16777215, 30))
        self.layout_pix.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_pix.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.layout_pix)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.txt_pix = QLabel(self.layout_pix)
        self.txt_pix.setObjectName(u"txt_pix")

        self.horizontalLayout_23.addWidget(self.txt_pix)

        self.txt_total_vendas_pix_db = QLabel(self.layout_pix)
        self.txt_total_vendas_pix_db.setObjectName(u"txt_total_vendas_pix_db")

        self.horizontalLayout_23.addWidget(self.txt_total_vendas_pix_db)


        self.verticalLayout_53.addWidget(self.layout_pix)

        self.layout_debito = QFrame(self.lado_esquerdo_3)
        self.layout_debito.setObjectName(u"layout_debito")
        self.layout_debito.setMaximumSize(QSize(16777215, 30))
        self.layout_debito.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_debito.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.layout_debito)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.txt_debito = QLabel(self.layout_debito)
        self.txt_debito.setObjectName(u"txt_debito")

        self.horizontalLayout_22.addWidget(self.txt_debito)

        self.txt_total_vendas_debito_db = QLabel(self.layout_debito)
        self.txt_total_vendas_debito_db.setObjectName(u"txt_total_vendas_debito_db")

        self.horizontalLayout_22.addWidget(self.txt_total_vendas_debito_db)


        self.verticalLayout_53.addWidget(self.layout_debito)

        self.layout_credito = QFrame(self.lado_esquerdo_3)
        self.layout_credito.setObjectName(u"layout_credito")
        self.layout_credito.setMaximumSize(QSize(16777215, 30))
        self.layout_credito.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_credito.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.layout_credito)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.txt_credito = QLabel(self.layout_credito)
        self.txt_credito.setObjectName(u"txt_credito")

        self.horizontalLayout_21.addWidget(self.txt_credito)

        self.txt_total_vendas_credito_db = QLabel(self.layout_credito)
        self.txt_total_vendas_credito_db.setObjectName(u"txt_total_vendas_credito_db")

        self.horizontalLayout_21.addWidget(self.txt_total_vendas_credito_db)


        self.verticalLayout_53.addWidget(self.layout_credito)

        self.layout_dinheiro = QFrame(self.lado_esquerdo_3)
        self.layout_dinheiro.setObjectName(u"layout_dinheiro")
        self.layout_dinheiro.setMaximumSize(QSize(16777215, 30))
        self.layout_dinheiro.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_dinheiro.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.layout_dinheiro)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.txt_dinheiro = QLabel(self.layout_dinheiro)
        self.txt_dinheiro.setObjectName(u"txt_dinheiro")

        self.horizontalLayout_20.addWidget(self.txt_dinheiro)

        self.txt_total_venda_dinheiro_db = QLabel(self.layout_dinheiro)
        self.txt_total_venda_dinheiro_db.setObjectName(u"txt_total_venda_dinheiro_db")

        self.horizontalLayout_20.addWidget(self.txt_total_venda_dinheiro_db)


        self.verticalLayout_53.addWidget(self.layout_dinheiro)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_53.addItem(self.verticalSpacer_8)


        self.horizontalLayout_19.addWidget(self.lado_esquerdo_3)


        self.horizontalLayout_18.addWidget(self.lado_esquerdo)

        self.lado_direito = QFrame(self.layout_dados_sem_tabela)
        self.lado_direito.setObjectName(u"lado_direito")
        self.lado_direito.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lado_direito.setFrameShape(QFrame.Shape.StyledPanel)
        self.lado_direito.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.lado_direito)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.lado_direito_2 = QFrame(self.lado_direito)
        self.lado_direito_2.setObjectName(u"lado_direito_2")
        self.lado_direito_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.lado_direito_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.lado_direito_2)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.icon_mov_gaveta = QLabel(self.lado_direito_2)
        self.icon_mov_gaveta.setObjectName(u"icon_mov_gaveta")
        self.icon_mov_gaveta.setMaximumSize(QSize(100, 100))
        self.icon_mov_gaveta.setPixmap(QPixmap(u":/icons/cash-register_3467857.png"))
        self.icon_mov_gaveta.setScaledContents(True)

        self.verticalLayout_55.addWidget(self.icon_mov_gaveta)

        self.txt_mov_gaveta = QLabel(self.lado_direito_2)
        self.txt_mov_gaveta.setObjectName(u"txt_mov_gaveta")
        self.txt_mov_gaveta.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_55.addWidget(self.txt_mov_gaveta, 0, Qt.AlignmentFlag.AlignLeft)

        self.txt_total_gaveta_db = QLabel(self.lado_direito_2)
        self.txt_total_gaveta_db.setObjectName(u"txt_total_gaveta_db")
        self.txt_total_gaveta_db.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_55.addWidget(self.txt_total_gaveta_db)

        self.verticalSpacer_3 = QSpacerItem(20, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_55.addItem(self.verticalSpacer_3)


        self.horizontalLayout_24.addWidget(self.lado_direito_2)

        self.lado_direito_3 = QFrame(self.lado_direito)
        self.lado_direito_3.setObjectName(u"lado_direito_3")
        self.lado_direito_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.lado_direito_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.lado_direito_3)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_54.addItem(self.verticalSpacer_5)

        self.layout_titulo = QFrame(self.lado_direito_3)
        self.layout_titulo.setObjectName(u"layout_titulo")
        self.layout_titulo.setMaximumSize(QSize(16777215, 30))
        self.layout_titulo.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_titulo.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.layout_titulo)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.icon_adc = QLabel(self.layout_titulo)
        self.icon_adc.setObjectName(u"icon_adc")
        self.icon_adc.setMaximumSize(QSize(20, 20))
        self.icon_adc.setStyleSheet(u"")
        self.icon_adc.setPixmap(QPixmap(u":/icons/circle_14034453.png"))
        self.icon_adc.setScaledContents(True)

        self.horizontalLayout_26.addWidget(self.icon_adc)

        self.txt_adicoes = QLabel(self.layout_titulo)
        self.txt_adicoes.setObjectName(u"txt_adicoes")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        font.setBold(True)
        self.txt_adicoes.setFont(font)

        self.horizontalLayout_26.addWidget(self.txt_adicoes)


        self.verticalLayout_54.addWidget(self.layout_titulo)

        self.layout_saldo_inicial = QFrame(self.lado_direito_3)
        self.layout_saldo_inicial.setObjectName(u"layout_saldo_inicial")
        self.layout_saldo_inicial.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_saldo_inicial.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.layout_saldo_inicial)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.txt_saldo_inicial = QLabel(self.layout_saldo_inicial)
        self.txt_saldo_inicial.setObjectName(u"txt_saldo_inicial")

        self.horizontalLayout_27.addWidget(self.txt_saldo_inicial)

        self.txt_saldo_inicial_db = QLabel(self.layout_saldo_inicial)
        self.txt_saldo_inicial_db.setObjectName(u"txt_saldo_inicial_db")

        self.horizontalLayout_27.addWidget(self.txt_saldo_inicial_db)


        self.verticalLayout_54.addWidget(self.layout_saldo_inicial)

        self.layout_vendas_dinheiro = QFrame(self.lado_direito_3)
        self.layout_vendas_dinheiro.setObjectName(u"layout_vendas_dinheiro")
        self.layout_vendas_dinheiro.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_vendas_dinheiro.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.layout_vendas_dinheiro)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.txt_vendas_dinheiro = QLabel(self.layout_vendas_dinheiro)
        self.txt_vendas_dinheiro.setObjectName(u"txt_vendas_dinheiro")

        self.horizontalLayout_28.addWidget(self.txt_vendas_dinheiro)

        self.txt_vendas_dinheiro_db = QLabel(self.layout_vendas_dinheiro)
        self.txt_vendas_dinheiro_db.setObjectName(u"txt_vendas_dinheiro_db")

        self.horizontalLayout_28.addWidget(self.txt_vendas_dinheiro_db)


        self.verticalLayout_54.addWidget(self.layout_vendas_dinheiro)

        self.layout_suprimento = QFrame(self.lado_direito_3)
        self.layout_suprimento.setObjectName(u"layout_suprimento")
        self.layout_suprimento.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_suprimento.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.layout_suprimento)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.txt_suprimento = QLabel(self.layout_suprimento)
        self.txt_suprimento.setObjectName(u"txt_suprimento")

        self.horizontalLayout_29.addWidget(self.txt_suprimento)

        self.txt_suprimento_db = QLabel(self.layout_suprimento)
        self.txt_suprimento_db.setObjectName(u"txt_suprimento_db")

        self.horizontalLayout_29.addWidget(self.txt_suprimento_db)


        self.verticalLayout_54.addWidget(self.layout_suprimento)

        self.layout_titulo_sangria = QFrame(self.lado_direito_3)
        self.layout_titulo_sangria.setObjectName(u"layout_titulo_sangria")
        self.layout_titulo_sangria.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_titulo_sangria.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.layout_titulo_sangria)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.icnon_retirada = QLabel(self.layout_titulo_sangria)
        self.icnon_retirada.setObjectName(u"icnon_retirada")
        self.icnon_retirada.setMaximumSize(QSize(20, 20))
        self.icnon_retirada.setPixmap(QPixmap(u":/icons/Red_Arrow_Down-512.webp"))
        self.icnon_retirada.setScaledContents(True)

        self.horizontalLayout_30.addWidget(self.icnon_retirada, 0, Qt.AlignmentFlag.AlignLeft)

        self.txt_retiradas = QLabel(self.layout_titulo_sangria)
        self.txt_retiradas.setObjectName(u"txt_retiradas")
        sizePolicy.setHeightForWidth(self.txt_retiradas.sizePolicy().hasHeightForWidth())
        self.txt_retiradas.setSizePolicy(sizePolicy)
        self.txt_retiradas.setFont(font)

        self.horizontalLayout_30.addWidget(self.txt_retiradas)


        self.verticalLayout_54.addWidget(self.layout_titulo_sangria)

        self.layout_sangria = QFrame(self.lado_direito_3)
        self.layout_sangria.setObjectName(u"layout_sangria")
        self.layout_sangria.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_sangria.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.layout_sangria)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.txt_sangria = QLabel(self.layout_sangria)
        self.txt_sangria.setObjectName(u"txt_sangria")

        self.horizontalLayout_25.addWidget(self.txt_sangria)

        self.txt_total_sangria_db = QLabel(self.layout_sangria)
        self.txt_total_sangria_db.setObjectName(u"txt_total_sangria_db")

        self.horizontalLayout_25.addWidget(self.txt_total_sangria_db)


        self.verticalLayout_54.addWidget(self.layout_sangria)

        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_54.addItem(self.verticalSpacer_6)


        self.horizontalLayout_24.addWidget(self.lado_direito_3)


        self.horizontalLayout_18.addWidget(self.lado_direito)


        self.verticalLayout_51.addWidget(self.layout_dados_sem_tabela)

        self.layout_hist_mov = QFrame(self.layout_dados_mov)
        self.layout_hist_mov.setObjectName(u"layout_hist_mov")
        self.layout_hist_mov.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_hist_mov.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.layout_hist_mov)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.tabela_hist_mov = QTreeWidget(self.layout_hist_mov)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setTextAlignment(4, Qt.AlignCenter);
        __qtreewidgetitem.setTextAlignment(3, Qt.AlignCenter);
        __qtreewidgetitem.setTextAlignment(2, Qt.AlignCenter);
        __qtreewidgetitem.setTextAlignment(1, Qt.AlignCenter);
        __qtreewidgetitem.setTextAlignment(0, Qt.AlignCenter);
        self.tabela_hist_mov.setHeaderItem(__qtreewidgetitem)
        self.tabela_hist_mov.setObjectName(u"tabela_hist_mov")
        self.tabela_hist_mov.setMinimumSize(QSize(800, 0))

        self.verticalLayout_56.addWidget(self.tabela_hist_mov)


        self.verticalLayout_51.addWidget(self.layout_hist_mov)


        self.verticalLayout_11.addWidget(self.layout_dados_mov)

        self.stackedWidget_7.addWidget(self.tela_principal_opcs)
        self.tela_principal_abrir_caixa = QWidget()
        self.tela_principal_abrir_caixa.setObjectName(u"tela_principal_abrir_caixa")
        self.verticalLayout_13 = QVBoxLayout(self.tela_principal_abrir_caixa)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_12 = QFrame(self.tela_principal_abrir_caixa)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(300, 300))
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_12)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.txt_quantidade_caixa_abrir = QLabel(self.frame_12)
        self.txt_quantidade_caixa_abrir.setObjectName(u"txt_quantidade_caixa_abrir")

        self.verticalLayout_14.addWidget(self.txt_quantidade_caixa_abrir)

        self.input_quantidade_caixa_abrir = QLineEdit(self.frame_12)
        self.input_quantidade_caixa_abrir.setObjectName(u"input_quantidade_caixa_abrir")

        self.verticalLayout_14.addWidget(self.input_quantidade_caixa_abrir)

        self.btn_confirmar_abrir = QPushButton(self.frame_12)
        self.btn_confirmar_abrir.setObjectName(u"btn_confirmar_abrir")

        self.verticalLayout_14.addWidget(self.btn_confirmar_abrir)


        self.verticalLayout_13.addWidget(self.frame_12, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.stackedWidget_7.addWidget(self.tela_principal_abrir_caixa)
        self.tela_principal_fechar_caixa = QWidget()
        self.tela_principal_fechar_caixa.setObjectName(u"tela_principal_fechar_caixa")
        self.verticalLayout_44 = QVBoxLayout(self.tela_principal_fechar_caixa)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.frame_13 = QFrame(self.tela_principal_fechar_caixa)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(300, 300))
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_13)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.txt_quantidade_caixa_fechar = QLabel(self.frame_13)
        self.txt_quantidade_caixa_fechar.setObjectName(u"txt_quantidade_caixa_fechar")

        self.verticalLayout_43.addWidget(self.txt_quantidade_caixa_fechar)

        self.input_quantidade_caixa_fechar = QLineEdit(self.frame_13)
        self.input_quantidade_caixa_fechar.setObjectName(u"input_quantidade_caixa_fechar")

        self.verticalLayout_43.addWidget(self.input_quantidade_caixa_fechar)

        self.btn_confirmar_fechar = QPushButton(self.frame_13)
        self.btn_confirmar_fechar.setObjectName(u"btn_confirmar_fechar")

        self.verticalLayout_43.addWidget(self.btn_confirmar_fechar)


        self.verticalLayout_44.addWidget(self.frame_13, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.stackedWidget_7.addWidget(self.tela_principal_fechar_caixa)
        self.tela_principal_sangria = QWidget()
        self.tela_principal_sangria.setObjectName(u"tela_principal_sangria")
        self.verticalLayout_47 = QVBoxLayout(self.tela_principal_sangria)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.frame_14 = QFrame(self.tela_principal_sangria)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_14)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.txt_sangria_titulo = QLabel(self.frame_14)
        self.txt_sangria_titulo.setObjectName(u"txt_sangria_titulo")
        self.txt_sangria_titulo.setStyleSheet(u"font-size: 26px;")

        self.verticalLayout_46.addWidget(self.txt_sangria_titulo, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_47.addWidget(self.frame_14, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.frame_15 = QFrame(self.tela_principal_sangria)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(500, 400))
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_15)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.txt_valor_sangria = QLabel(self.frame_15)
        self.txt_valor_sangria.setObjectName(u"txt_valor_sangria")

        self.verticalLayout_45.addWidget(self.txt_valor_sangria)

        self.input_valor_sangria = QLineEdit(self.frame_15)
        self.input_valor_sangria.setObjectName(u"input_valor_sangria")

        self.verticalLayout_45.addWidget(self.input_valor_sangria)

        self.txt_vendedor_responsavel_sangria = QLabel(self.frame_15)
        self.txt_vendedor_responsavel_sangria.setObjectName(u"txt_vendedor_responsavel_sangria")

        self.verticalLayout_45.addWidget(self.txt_vendedor_responsavel_sangria)

        self.input_vendedor_responsavel_sangria = QLineEdit(self.frame_15)
        self.input_vendedor_responsavel_sangria.setObjectName(u"input_vendedor_responsavel_sangria")

        self.verticalLayout_45.addWidget(self.input_vendedor_responsavel_sangria)

        self.txt_obs_sangria = QLabel(self.frame_15)
        self.txt_obs_sangria.setObjectName(u"txt_obs_sangria")

        self.verticalLayout_45.addWidget(self.txt_obs_sangria)

        self.input_obs_sangria = QTextEdit(self.frame_15)
        self.input_obs_sangria.setObjectName(u"input_obs_sangria")

        self.verticalLayout_45.addWidget(self.input_obs_sangria)

        self.frame_16 = QFrame(self.frame_15)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.btn_cancelar_sangria = QPushButton(self.frame_16)
        self.btn_cancelar_sangria.setObjectName(u"btn_cancelar_sangria")

        self.horizontalLayout_16.addWidget(self.btn_cancelar_sangria)

        self.btn_confirmar_sangria = QPushButton(self.frame_16)
        self.btn_confirmar_sangria.setObjectName(u"btn_confirmar_sangria")

        self.horizontalLayout_16.addWidget(self.btn_confirmar_sangria)


        self.verticalLayout_45.addWidget(self.frame_16)


        self.verticalLayout_47.addWidget(self.frame_15, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.verticalSpacer = QSpacerItem(20, 150, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_47.addItem(self.verticalSpacer)

        self.stackedWidget_7.addWidget(self.tela_principal_sangria)
        self.tela_principal_suprimento = QWidget()
        self.tela_principal_suprimento.setObjectName(u"tela_principal_suprimento")
        self.verticalLayout_50 = QVBoxLayout(self.tela_principal_suprimento)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.frame_17 = QFrame(self.tela_principal_suprimento)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frame_17)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.txt_tirulo_suprimento = QLabel(self.frame_17)
        self.txt_tirulo_suprimento.setObjectName(u"txt_tirulo_suprimento")
        self.txt_tirulo_suprimento.setStyleSheet(u"font-size: 26px;")

        self.verticalLayout_49.addWidget(self.txt_tirulo_suprimento)


        self.verticalLayout_50.addWidget(self.frame_17, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.frame_18 = QFrame(self.tela_principal_suprimento)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(500, 400))
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_18)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.txt_valor_suprimento = QLabel(self.frame_18)
        self.txt_valor_suprimento.setObjectName(u"txt_valor_suprimento")
        self.txt_valor_suprimento.setStyleSheet(u"")

        self.verticalLayout_48.addWidget(self.txt_valor_suprimento)

        self.input_valor_suprimento = QLineEdit(self.frame_18)
        self.input_valor_suprimento.setObjectName(u"input_valor_suprimento")

        self.verticalLayout_48.addWidget(self.input_valor_suprimento)

        self.txt_vendedor_responsavel_suprimento = QLabel(self.frame_18)
        self.txt_vendedor_responsavel_suprimento.setObjectName(u"txt_vendedor_responsavel_suprimento")

        self.verticalLayout_48.addWidget(self.txt_vendedor_responsavel_suprimento)

        self.input_vendedor_responsavel_suprimento = QLineEdit(self.frame_18)
        self.input_vendedor_responsavel_suprimento.setObjectName(u"input_vendedor_responsavel_suprimento")

        self.verticalLayout_48.addWidget(self.input_vendedor_responsavel_suprimento)

        self.txt_obs_suprimento = QLabel(self.frame_18)
        self.txt_obs_suprimento.setObjectName(u"txt_obs_suprimento")

        self.verticalLayout_48.addWidget(self.txt_obs_suprimento)

        self.input_obs_suprimento = QTextEdit(self.frame_18)
        self.input_obs_suprimento.setObjectName(u"input_obs_suprimento")

        self.verticalLayout_48.addWidget(self.input_obs_suprimento)

        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.btn_cancelar_suprimento = QPushButton(self.frame_19)
        self.btn_cancelar_suprimento.setObjectName(u"btn_cancelar_suprimento")

        self.horizontalLayout_17.addWidget(self.btn_cancelar_suprimento)

        self.btn_confirmar_suprimento = QPushButton(self.frame_19)
        self.btn_confirmar_suprimento.setObjectName(u"btn_confirmar_suprimento")

        self.horizontalLayout_17.addWidget(self.btn_confirmar_suprimento)


        self.verticalLayout_48.addWidget(self.frame_19)


        self.verticalLayout_50.addWidget(self.frame_18, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 150, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_50.addItem(self.verticalSpacer_2)

        self.stackedWidget_7.addWidget(self.tela_principal_suprimento)

        self.verticalLayout_6.addWidget(self.stackedWidget_7)

        self.stackedWidget.addWidget(self.telaprincipal)
        self.telapdv = QWidget()
        self.telapdv.setObjectName(u"telapdv")
        self.telapdv.setStyleSheet(u"")
        self.horizontalLayout_5 = QHBoxLayout(self.telapdv)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.stackedWidget_2 = QStackedWidget(self.telapdv)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setMaximumSize(QSize(16777215, 16777215))
        self.stackedWidget_2.setStyleSheet(u"")
        self.lado_esquerdo_pdv_1 = QWidget()
        self.lado_esquerdo_pdv_1.setObjectName(u"lado_esquerdo_pdv_1")
        self.verticalLayout_8 = QVBoxLayout(self.lado_esquerdo_pdv_1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_2 = QFrame(self.lado_esquerdo_pdv_1)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.input_pdv_produto = QLineEdit(self.frame_2)
        self.input_pdv_produto.setObjectName(u"input_pdv_produto")

        self.horizontalLayout_6.addWidget(self.input_pdv_produto)

        self.btn_pesquisar_produto = QPushButton(self.frame_2)
        self.btn_pesquisar_produto.setObjectName(u"btn_pesquisar_produto")
        icon1 = QIcon()
        icon1.addFile(u":/icons/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_pesquisar_produto.setIcon(icon1)

        self.horizontalLayout_6.addWidget(self.btn_pesquisar_produto)

        self.input_pdv_categoria = QComboBox(self.frame_2)
        self.input_pdv_categoria.setObjectName(u"input_pdv_categoria")

        self.horizontalLayout_6.addWidget(self.input_pdv_categoria, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_8.addWidget(self.frame_2, 0, Qt.AlignmentFlag.AlignTop)

        self.mostruario_cards2_2 = QScrollArea(self.lado_esquerdo_pdv_1)
        self.mostruario_cards2_2.setObjectName(u"mostruario_cards2_2")
        self.mostruario_cards2_2.setWidgetResizable(True)
        self.mostruario_cards = QWidget()
        self.mostruario_cards.setObjectName(u"mostruario_cards")
        self.mostruario_cards.setGeometry(QRect(0, 0, 72, 16))
        self.mostruario_cards2_2.setWidget(self.mostruario_cards)

        self.verticalLayout_8.addWidget(self.mostruario_cards2_2)

        self.stackedWidget_2.addWidget(self.lado_esquerdo_pdv_1)
        self.lado_esquerdo_pdv_2 = QWidget()
        self.lado_esquerdo_pdv_2.setObjectName(u"lado_esquerdo_pdv_2")
        self.verticalLayout_20 = QVBoxLayout(self.lado_esquerdo_pdv_2)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.layout_lado_estquerdo = QFrame(self.lado_esquerdo_pdv_2)
        self.layout_lado_estquerdo.setObjectName(u"layout_lado_estquerdo")
        self.layout_lado_estquerdo.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_lado_estquerdo.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.layout_lado_estquerdo)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.layout_nome_quant = QFrame(self.layout_lado_estquerdo)
        self.layout_nome_quant.setObjectName(u"layout_nome_quant")
        self.layout_nome_quant.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_nome_quant.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.layout_nome_quant)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.txt_pdv_nome = QLabel(self.layout_nome_quant)
        self.txt_pdv_nome.setObjectName(u"txt_pdv_nome")

        self.horizontalLayout_8.addWidget(self.txt_pdv_nome)

        self.txt_pdv_valor = QLabel(self.layout_nome_quant)
        self.txt_pdv_valor.setObjectName(u"txt_pdv_valor")

        self.horizontalLayout_8.addWidget(self.txt_pdv_valor, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_7.addWidget(self.layout_nome_quant, 0, Qt.AlignmentFlag.AlignVCenter)

        self.layout_btn_menos = QFrame(self.layout_lado_estquerdo)
        self.layout_btn_menos.setObjectName(u"layout_btn_menos")
        self.layout_btn_menos.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_btn_menos.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.layout_btn_menos)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.btn_pdv_menos = QPushButton(self.layout_btn_menos)
        self.btn_pdv_menos.setObjectName(u"btn_pdv_menos")
        icon2 = QIcon()
        icon2.addFile(u":/icons/minus-circle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_pdv_menos.setIcon(icon2)

        self.horizontalLayout_9.addWidget(self.btn_pdv_menos)


        self.horizontalLayout_7.addWidget(self.layout_btn_menos, 0, Qt.AlignmentFlag.AlignVCenter)

        self.input_pdv_quant = QLineEdit(self.layout_lado_estquerdo)
        self.input_pdv_quant.setObjectName(u"input_pdv_quant")

        self.horizontalLayout_7.addWidget(self.input_pdv_quant)

        self.layout_btn_mais = QFrame(self.layout_lado_estquerdo)
        self.layout_btn_mais.setObjectName(u"layout_btn_mais")
        self.layout_btn_mais.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_btn_mais.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.layout_btn_mais)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.btn_pdv_mais = QPushButton(self.layout_btn_mais)
        self.btn_pdv_mais.setObjectName(u"btn_pdv_mais")
        icon3 = QIcon()
        icon3.addFile(u":/icons/add.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_pdv_mais.setIcon(icon3)

        self.horizontalLayout_10.addWidget(self.btn_pdv_mais)


        self.horizontalLayout_7.addWidget(self.layout_btn_mais, 0, Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_20.addWidget(self.layout_lado_estquerdo, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.btn_adc_carrinho = QPushButton(self.lado_esquerdo_pdv_2)
        self.btn_adc_carrinho.setObjectName(u"btn_adc_carrinho")

        self.verticalLayout_20.addWidget(self.btn_adc_carrinho)

        self.stackedWidget_2.addWidget(self.lado_esquerdo_pdv_2)
        self.lado_esquerdo_pdv_3 = QWidget()
        self.lado_esquerdo_pdv_3.setObjectName(u"lado_esquerdo_pdv_3")
        self.verticalLayout_34 = QVBoxLayout(self.lado_esquerdo_pdv_3)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.layout_lado_estquerdo_2 = QFrame(self.lado_esquerdo_pdv_3)
        self.layout_lado_estquerdo_2.setObjectName(u"layout_lado_estquerdo_2")
        self.layout_lado_estquerdo_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_lado_estquerdo_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.layout_lado_estquerdo_2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.layout_nome_quant_2 = QFrame(self.layout_lado_estquerdo_2)
        self.layout_nome_quant_2.setObjectName(u"layout_nome_quant_2")
        self.layout_nome_quant_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_nome_quant_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.layout_nome_quant_2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.txt_pdv_nome_2 = QLabel(self.layout_nome_quant_2)
        self.txt_pdv_nome_2.setObjectName(u"txt_pdv_nome_2")

        self.horizontalLayout_13.addWidget(self.txt_pdv_nome_2)

        self.txt_pdv_valor_2 = QLabel(self.layout_nome_quant_2)
        self.txt_pdv_valor_2.setObjectName(u"txt_pdv_valor_2")

        self.horizontalLayout_13.addWidget(self.txt_pdv_valor_2, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_11.addWidget(self.layout_nome_quant_2, 0, Qt.AlignmentFlag.AlignVCenter)

        self.input_pdv_quant_2 = QLineEdit(self.layout_lado_estquerdo_2)
        self.input_pdv_quant_2.setObjectName(u"input_pdv_quant_2")

        self.horizontalLayout_11.addWidget(self.input_pdv_quant_2)


        self.verticalLayout_34.addWidget(self.layout_lado_estquerdo_2, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.btn_adc_carrinho_2 = QPushButton(self.lado_esquerdo_pdv_3)
        self.btn_adc_carrinho_2.setObjectName(u"btn_adc_carrinho_2")

        self.verticalLayout_34.addWidget(self.btn_adc_carrinho_2)

        self.stackedWidget_2.addWidget(self.lado_esquerdo_pdv_3)

        self.horizontalLayout_5.addWidget(self.stackedWidget_2)

        self.stackedWidget_6 = QStackedWidget(self.telapdv)
        self.stackedWidget_6.setObjectName(u"stackedWidget_6")
        self.stackedWidget_6.setMinimumSize(QSize(300, 0))
        self.stackedWidget_6.setMaximumSize(QSize(350, 16777215))
        self.stackedWidget_6.setStyleSheet(u"background-color: rgb(57, 192, 255);")
        self.lado_direito_pdv_1 = QWidget()
        self.lado_direito_pdv_1.setObjectName(u"lado_direito_pdv_1")
        self.verticalLayout_15 = QVBoxLayout(self.lado_direito_pdv_1)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.tabela_carrinho = QTreeWidget(self.lado_direito_pdv_1)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setTextAlignment(3, Qt.AlignCenter);
        __qtreewidgetitem1.setTextAlignment(2, Qt.AlignCenter);
        __qtreewidgetitem1.setTextAlignment(1, Qt.AlignCenter);
        self.tabela_carrinho.setHeaderItem(__qtreewidgetitem1)
        self.tabela_carrinho.setObjectName(u"tabela_carrinho")

        self.verticalLayout_15.addWidget(self.tabela_carrinho, 0, Qt.AlignmentFlag.AlignVCenter)

        self.btn_remover_produto_carrinho = QPushButton(self.lado_direito_pdv_1)
        self.btn_remover_produto_carrinho.setObjectName(u"btn_remover_produto_carrinho")

        self.verticalLayout_15.addWidget(self.btn_remover_produto_carrinho)

        self.layout_valor_total = QFrame(self.lado_direito_pdv_1)
        self.layout_valor_total.setObjectName(u"layout_valor_total")
        self.layout_valor_total.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_valor_total.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.layout_valor_total)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.txt_valor_total_texto = QLabel(self.layout_valor_total)
        self.txt_valor_total_texto.setObjectName(u"txt_valor_total_texto")

        self.verticalLayout_16.addWidget(self.txt_valor_total_texto)

        self.frame_4 = QFrame(self.layout_valor_total)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_4)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.txt_valor_total = QLabel(self.frame_4)
        self.txt_valor_total.setObjectName(u"txt_valor_total")

        self.verticalLayout_17.addWidget(self.txt_valor_total)


        self.verticalLayout_16.addWidget(self.frame_4)


        self.verticalLayout_15.addWidget(self.layout_valor_total, 0, Qt.AlignmentFlag.AlignVCenter)

        self.input_pdv_forma_pagamento = QComboBox(self.lado_direito_pdv_1)
        self.input_pdv_forma_pagamento.addItem("")
        self.input_pdv_forma_pagamento.addItem("")
        self.input_pdv_forma_pagamento.addItem("")
        self.input_pdv_forma_pagamento.addItem("")
        self.input_pdv_forma_pagamento.setObjectName(u"input_pdv_forma_pagamento")

        self.verticalLayout_15.addWidget(self.input_pdv_forma_pagamento)

        self.frame_pagamento = QFrame(self.lado_direito_pdv_1)
        self.frame_pagamento.setObjectName(u"frame_pagamento")
        self.frame_pagamento.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_pagamento.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_pagamento)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")

        self.verticalLayout_15.addWidget(self.frame_pagamento)

        self.btn_finaliza_compra = QPushButton(self.lado_direito_pdv_1)
        self.btn_finaliza_compra.setObjectName(u"btn_finaliza_compra")

        self.verticalLayout_15.addWidget(self.btn_finaliza_compra)

        self.stackedWidget_6.addWidget(self.lado_direito_pdv_1)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_19 = QVBoxLayout(self.page_6)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_6 = QLabel(self.page_6)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_19.addWidget(self.label_6, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.stackedWidget_6.addWidget(self.page_6)

        self.horizontalLayout_5.addWidget(self.stackedWidget_6)

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
        icon4 = QIcon()
        icon4.addFile(u":/icons/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btn_pesquisar_produto_4.setIcon(icon4)
        self.btn_pesquisar_produto_4.setIconSize(QSize(25, 25))

        self.horizontalLayout_12.addWidget(self.btn_pesquisar_produto_4, 0, Qt.AlignmentFlag.AlignRight)

        self.btn_adc_produto_estoque = QPushButton(self.layout_pesquisar_produto_estoque_2)
        self.btn_adc_produto_estoque.setObjectName(u"btn_adc_produto_estoque")
        self.btn_adc_produto_estoque.setStyleSheet(u"background-color: none;")
        icon5 = QIcon()
        icon5.addFile(u":/icons/add.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btn_adc_produto_estoque.setIcon(icon5)
        self.btn_adc_produto_estoque.setIconSize(QSize(25, 25))
        self.btn_adc_produto_estoque.setCheckable(False)

        self.horizontalLayout_12.addWidget(self.btn_adc_produto_estoque)

        self.btn_editar_produto = QPushButton(self.layout_pesquisar_produto_estoque_2)
        self.btn_editar_produto.setObjectName(u"btn_editar_produto")
        icon6 = QIcon()
        icon6.addFile(u":/icons/pencil.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_editar_produto.setIcon(icon6)
        self.btn_editar_produto.setIconSize(QSize(25, 25))

        self.horizontalLayout_12.addWidget(self.btn_editar_produto)


        self.verticalLayout_26.addWidget(self.layout_pesquisar_produto_estoque_2, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_25.addWidget(self.layout_pesquisar_produto_estoque, 0, Qt.AlignmentFlag.AlignTop)

        self.txt_caso_produto_nao_encontra_estoque = QLabel(self.tela_estoque_1)
        self.txt_caso_produto_nao_encontra_estoque.setObjectName(u"txt_caso_produto_nao_encontra_estoque")

        self.verticalLayout_25.addWidget(self.txt_caso_produto_nao_encontra_estoque, 0, Qt.AlignmentFlag.AlignHCenter)

        self.treeWidget = QTreeWidget(self.tela_estoque_1)
        __qtreewidgetitem2 = QTreeWidgetItem()
        __qtreewidgetitem2.setTextAlignment(4, Qt.AlignCenter);
        __qtreewidgetitem2.setTextAlignment(3, Qt.AlignCenter);
        __qtreewidgetitem2.setTextAlignment(2, Qt.AlignCenter);
        __qtreewidgetitem2.setTextAlignment(1, Qt.AlignCenter);
        __qtreewidgetitem2.setTextAlignment(0, Qt.AlignCenter);
        self.treeWidget.setHeaderItem(__qtreewidgetitem2)
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
        self.frame_8 = QFrame(self.widget)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(200, 200))
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_8)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.img_produto_estoque = QLabel(self.frame_8)
        self.img_produto_estoque.setObjectName(u"img_produto_estoque")
        self.img_produto_estoque.setMaximumSize(QSize(200, 200))
        self.img_produto_estoque.setStyleSheet(u"border: 1px solid;")

        self.verticalLayout_28.addWidget(self.img_produto_estoque)


        self.gridLayout_6.addWidget(self.frame_8, 4, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.frame_6 = QFrame(self.widget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_6)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.txt_quantidade_estoque = QLabel(self.frame_6)
        self.txt_quantidade_estoque.setObjectName(u"txt_quantidade_estoque")

        self.verticalLayout_23.addWidget(self.txt_quantidade_estoque, 0, Qt.AlignmentFlag.AlignBottom)

        self.input_quantidade_produto = QLineEdit(self.frame_6)
        self.input_quantidade_produto.setObjectName(u"input_quantidade_produto")
        self.input_quantidade_produto.setMinimumSize(QSize(400, 0))
        self.input_quantidade_produto.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_23.addWidget(self.input_quantidade_produto, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.gridLayout_6.addWidget(self.frame_6, 2, 0, 1, 1)

        self.btn_adc_foto_produto = QPushButton(self.widget)
        self.btn_adc_foto_produto.setObjectName(u"btn_adc_foto_produto")

        self.gridLayout_6.addWidget(self.btn_adc_foto_produto, 4, 0, 1, 1)

        self.frame_5 = QFrame(self.widget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_5)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.txt_preco_estoque = QLabel(self.frame_5)
        self.txt_preco_estoque.setObjectName(u"txt_preco_estoque")

        self.verticalLayout_22.addWidget(self.txt_preco_estoque, 0, Qt.AlignmentFlag.AlignBottom)

        self.input_preco_produto = QLineEdit(self.frame_5)
        self.input_preco_produto.setObjectName(u"input_preco_produto")
        self.input_preco_produto.setMinimumSize(QSize(400, 0))
        self.input_preco_produto.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_22.addWidget(self.input_preco_produto, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.gridLayout_6.addWidget(self.frame_5, 2, 1, 1, 1)

        self.frame_7 = QFrame(self.widget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_7)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.txt_categoria_estoque = QLabel(self.frame_7)
        self.txt_categoria_estoque.setObjectName(u"txt_categoria_estoque")

        self.verticalLayout_24.addWidget(self.txt_categoria_estoque)

        self.input_categoria_produto = QComboBox(self.frame_7)
        self.input_categoria_produto.setObjectName(u"input_categoria_produto")
        self.input_categoria_produto.setMinimumSize(QSize(400, 0))
        self.input_categoria_produto.setEditable(False)

        self.verticalLayout_24.addWidget(self.input_categoria_produto)


        self.gridLayout_6.addWidget(self.frame_7, 1, 1, 1, 1)

        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_3)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.txt_nome_estoque = QLabel(self.frame_3)
        self.txt_nome_estoque.setObjectName(u"txt_nome_estoque")

        self.verticalLayout_21.addWidget(self.txt_nome_estoque, 0, Qt.AlignmentFlag.AlignBottom)

        self.input_nome_produto = QLineEdit(self.frame_3)
        self.input_nome_produto.setObjectName(u"input_nome_produto")
        self.input_nome_produto.setMinimumSize(QSize(400, 0))
        self.input_nome_produto.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_21.addWidget(self.input_nome_produto, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.gridLayout_6.addWidget(self.frame_3, 1, 0, 1, 1)

        self.frame_30 = QFrame(self.widget)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_30)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.label = QLabel(self.frame_30)
        self.label.setObjectName(u"label")

        self.verticalLayout_40.addWidget(self.label)

        self.input_tipo_valor = QComboBox(self.frame_30)
        self.input_tipo_valor.addItem("")
        self.input_tipo_valor.addItem("")
        self.input_tipo_valor.setObjectName(u"input_tipo_valor")
        self.input_tipo_valor.setMinimumSize(QSize(200, 0))

        self.verticalLayout_40.addWidget(self.input_tipo_valor)


        self.gridLayout_6.addWidget(self.frame_30, 1, 2, 1, 1, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_27.addWidget(self.widget, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.btn_adc_produto = QPushButton(self.tela_estoque_2)
        self.btn_adc_produto.setObjectName(u"btn_adc_produto")
        self.btn_adc_produto.setMinimumSize(QSize(300, 0))

        self.verticalLayout_27.addWidget(self.btn_adc_produto, 0, Qt.AlignmentFlag.AlignHCenter)

        self.stackedWidget_3.addWidget(self.tela_estoque_2)
        self.tela_estoque_3 = QWidget()
        self.tela_estoque_3.setObjectName(u"tela_estoque_3")
        self.verticalLayout_62 = QVBoxLayout(self.tela_estoque_3)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.widget_2 = QWidget(self.tela_estoque_3)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_7 = QGridLayout(self.widget_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.frame_21 = QFrame(self.widget_2)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.frame_21)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.txt_categoria_estoque_2 = QLabel(self.frame_21)
        self.txt_categoria_estoque_2.setObjectName(u"txt_categoria_estoque_2")

        self.verticalLayout_61.addWidget(self.txt_categoria_estoque_2)

        self.input_categoria_produto_2 = QComboBox(self.frame_21)
        self.input_categoria_produto_2.setObjectName(u"input_categoria_produto_2")
        self.input_categoria_produto_2.setMinimumSize(QSize(400, 0))
        self.input_categoria_produto_2.setEditable(False)

        self.verticalLayout_61.addWidget(self.input_categoria_produto_2)


        self.gridLayout_7.addWidget(self.frame_21, 1, 1, 1, 1)

        self.frame_9 = QFrame(self.widget_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_57 = QVBoxLayout(self.frame_9)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.txt_nome_estoque_2 = QLabel(self.frame_9)
        self.txt_nome_estoque_2.setObjectName(u"txt_nome_estoque_2")

        self.verticalLayout_57.addWidget(self.txt_nome_estoque_2, 0, Qt.AlignmentFlag.AlignBottom)

        self.input_nome_produto_2 = QLineEdit(self.frame_9)
        self.input_nome_produto_2.setObjectName(u"input_nome_produto_2")
        self.input_nome_produto_2.setMinimumSize(QSize(400, 0))
        self.input_nome_produto_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_57.addWidget(self.input_nome_produto_2, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.gridLayout_7.addWidget(self.frame_9, 1, 0, 1, 1)

        self.frame_10 = QFrame(self.widget_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(200, 200))
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_58 = QVBoxLayout(self.frame_10)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.img_produto_estoque_2 = QLabel(self.frame_10)
        self.img_produto_estoque_2.setObjectName(u"img_produto_estoque_2")
        self.img_produto_estoque_2.setMaximumSize(QSize(200, 200))
        self.img_produto_estoque_2.setStyleSheet(u"border: 1px solid;")

        self.verticalLayout_58.addWidget(self.img_produto_estoque_2)


        self.gridLayout_7.addWidget(self.frame_10, 4, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.frame_20 = QFrame(self.widget_2)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_60 = QVBoxLayout(self.frame_20)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.txt_preco_estoque_2 = QLabel(self.frame_20)
        self.txt_preco_estoque_2.setObjectName(u"txt_preco_estoque_2")

        self.verticalLayout_60.addWidget(self.txt_preco_estoque_2, 0, Qt.AlignmentFlag.AlignBottom)

        self.input_preco_produto_2 = QLineEdit(self.frame_20)
        self.input_preco_produto_2.setObjectName(u"input_preco_produto_2")
        self.input_preco_produto_2.setMinimumSize(QSize(400, 0))
        self.input_preco_produto_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_60.addWidget(self.input_preco_produto_2, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.gridLayout_7.addWidget(self.frame_20, 2, 1, 1, 1)

        self.frame_11 = QFrame(self.widget_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.frame_11)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.txt_quantidade_estoque_2 = QLabel(self.frame_11)
        self.txt_quantidade_estoque_2.setObjectName(u"txt_quantidade_estoque_2")

        self.verticalLayout_59.addWidget(self.txt_quantidade_estoque_2, 0, Qt.AlignmentFlag.AlignBottom)

        self.input_quantidade_produto_2 = QLineEdit(self.frame_11)
        self.input_quantidade_produto_2.setObjectName(u"input_quantidade_produto_2")
        self.input_quantidade_produto_2.setMinimumSize(QSize(400, 0))
        self.input_quantidade_produto_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_59.addWidget(self.input_quantidade_produto_2, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.gridLayout_7.addWidget(self.frame_11, 2, 0, 1, 1)

        self.btn_adc_foto_produto_2 = QPushButton(self.widget_2)
        self.btn_adc_foto_produto_2.setObjectName(u"btn_adc_foto_produto_2")

        self.gridLayout_7.addWidget(self.btn_adc_foto_produto_2, 4, 0, 1, 1)

        self.frame_31 = QFrame(self.widget_2)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_31)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.label_2 = QLabel(self.frame_31)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_41.addWidget(self.label_2)

        self.input_tipo_valor_2 = QComboBox(self.frame_31)
        self.input_tipo_valor_2.addItem("")
        self.input_tipo_valor_2.addItem("")
        self.input_tipo_valor_2.setObjectName(u"input_tipo_valor_2")
        self.input_tipo_valor_2.setMinimumSize(QSize(200, 0))

        self.verticalLayout_41.addWidget(self.input_tipo_valor_2)


        self.gridLayout_7.addWidget(self.frame_31, 1, 2, 1, 1)


        self.verticalLayout_62.addWidget(self.widget_2, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.btn_adc_produto_2 = QPushButton(self.tela_estoque_3)
        self.btn_adc_produto_2.setObjectName(u"btn_adc_produto_2")
        self.btn_adc_produto_2.setMinimumSize(QSize(300, 0))

        self.verticalLayout_62.addWidget(self.btn_adc_produto_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.stackedWidget_3.addWidget(self.tela_estoque_3)

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
        self.layout_relatorios_3.setMinimumSize(QSize(300, 0))
        self.layout_relatorios_3.setMaximumSize(QSize(500, 300))
        self.layout_relatorios_3.setStyleSheet(u"background-color: rgb(219, 219, 219);\n"
"border-radius: 20px;")
        self.layout_relatorios_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_relatorios_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.layout_relatorios_3)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.txt_produtos_mais_vendidos = QLabel(self.layout_relatorios_3)
        self.txt_produtos_mais_vendidos.setObjectName(u"txt_produtos_mais_vendidos")

        self.verticalLayout_31.addWidget(self.txt_produtos_mais_vendidos, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.frame_estoque_alerta = QFrame(self.layout_relatorios_3)
        self.frame_estoque_alerta.setObjectName(u"frame_estoque_alerta")
        sizePolicy1.setHeightForWidth(self.frame_estoque_alerta.sizePolicy().hasHeightForWidth())
        self.frame_estoque_alerta.setSizePolicy(sizePolicy1)
        self.frame_estoque_alerta.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_estoque_alerta.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_31.addWidget(self.frame_estoque_alerta)


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

        self.frame_produtos_mai_vendidos = QFrame(self.layout_relatorios_1)
        self.frame_produtos_mai_vendidos.setObjectName(u"frame_produtos_mai_vendidos")
        sizePolicy1.setHeightForWidth(self.frame_produtos_mai_vendidos.sizePolicy().hasHeightForWidth())
        self.frame_produtos_mai_vendidos.setSizePolicy(sizePolicy1)
        self.frame_produtos_mai_vendidos.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_produtos_mai_vendidos.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_29.addWidget(self.frame_produtos_mai_vendidos)


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

        self.top_5_operadores = QFrame(self.layout_relatorios_2)
        self.top_5_operadores.setObjectName(u"top_5_operadores")
        sizePolicy1.setHeightForWidth(self.top_5_operadores.sizePolicy().hasHeightForWidth())
        self.top_5_operadores.setSizePolicy(sizePolicy1)
        self.top_5_operadores.setFrameShape(QFrame.Shape.StyledPanel)
        self.top_5_operadores.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_30.addWidget(self.top_5_operadores)


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

        self.frame_formas_pagamento = QFrame(self.layout_relatorios_4)
        self.frame_formas_pagamento.setObjectName(u"frame_formas_pagamento")
        sizePolicy1.setHeightForWidth(self.frame_formas_pagamento.sizePolicy().hasHeightForWidth())
        self.frame_formas_pagamento.setSizePolicy(sizePolicy1)
        self.frame_formas_pagamento.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_formas_pagamento.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_32.addWidget(self.frame_formas_pagamento)


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
        __qtreewidgetitem3 = QTreeWidgetItem()
        __qtreewidgetitem3.setTextAlignment(5, Qt.AlignCenter);
        __qtreewidgetitem3.setTextAlignment(4, Qt.AlignCenter);
        __qtreewidgetitem3.setTextAlignment(3, Qt.AlignCenter);
        __qtreewidgetitem3.setTextAlignment(2, Qt.AlignCenter);
        __qtreewidgetitem3.setTextAlignment(1, Qt.AlignCenter);
        __qtreewidgetitem3.setTextAlignment(0, Qt.AlignCenter);
        self.treeWidget_2.setHeaderItem(__qtreewidgetitem3)
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
        self.frame_24 = QFrame(self.layout_adc_usuario)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_65 = QVBoxLayout(self.frame_24)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.txt_senha = QLabel(self.frame_24)
        self.txt_senha.setObjectName(u"txt_senha")

        self.verticalLayout_65.addWidget(self.txt_senha)

        self.input_senha_adc_usuario = QLineEdit(self.frame_24)
        self.input_senha_adc_usuario.setObjectName(u"input_senha_adc_usuario")
        self.input_senha_adc_usuario.setMaximumSize(QSize(400, 16777215))
        self.input_senha_adc_usuario.setStyleSheet(u"")
        self.input_senha_adc_usuario.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_senha_adc_usuario.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_65.addWidget(self.input_senha_adc_usuario)


        self.gridLayout_3.addWidget(self.frame_24, 3, 0, 1, 1)

        self.frame_22 = QFrame(self.layout_adc_usuario)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_63 = QVBoxLayout(self.frame_22)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.txt_nome = QLabel(self.frame_22)
        self.txt_nome.setObjectName(u"txt_nome")

        self.verticalLayout_63.addWidget(self.txt_nome)

        self.input_nome_adc_usuario = QLineEdit(self.frame_22)
        self.input_nome_adc_usuario.setObjectName(u"input_nome_adc_usuario")
        self.input_nome_adc_usuario.setMaximumSize(QSize(400, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setWeight(QFont.DemiBold)
        font1.setItalic(False)
        self.input_nome_adc_usuario.setFont(font1)
        self.input_nome_adc_usuario.setStyleSheet(u"")
        self.input_nome_adc_usuario.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_63.addWidget(self.input_nome_adc_usuario)


        self.gridLayout_3.addWidget(self.frame_22, 0, 0, 1, 1)

        self.frame_23 = QFrame(self.layout_adc_usuario)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_64 = QVBoxLayout(self.frame_23)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.txt_email = QLabel(self.frame_23)
        self.txt_email.setObjectName(u"txt_email")

        self.verticalLayout_64.addWidget(self.txt_email)

        self.input_email_adc_usuario = QLineEdit(self.frame_23)
        self.input_email_adc_usuario.setObjectName(u"input_email_adc_usuario")
        self.input_email_adc_usuario.setMaximumSize(QSize(400, 16777215))
        self.input_email_adc_usuario.setStyleSheet(u"")
        self.input_email_adc_usuario.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_64.addWidget(self.input_email_adc_usuario)


        self.gridLayout_3.addWidget(self.frame_23, 0, 1, 1, 1)

        self.frame_25 = QFrame(self.layout_adc_usuario)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_66 = QVBoxLayout(self.frame_25)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.txt_cpf = QLabel(self.frame_25)
        self.txt_cpf.setObjectName(u"txt_cpf")

        self.verticalLayout_66.addWidget(self.txt_cpf)

        self.input_cpf_adc_usuario = QLineEdit(self.frame_25)
        self.input_cpf_adc_usuario.setObjectName(u"input_cpf_adc_usuario")
        self.input_cpf_adc_usuario.setMaximumSize(QSize(400, 16777215))
        self.input_cpf_adc_usuario.setStyleSheet(u"")
        self.input_cpf_adc_usuario.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_66.addWidget(self.input_cpf_adc_usuario)


        self.gridLayout_3.addWidget(self.frame_25, 3, 1, 1, 1)

        self.frame_28 = QFrame(self.layout_adc_usuario)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_68 = QVBoxLayout(self.frame_28)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.txt_permissoes = QLabel(self.frame_28)
        self.txt_permissoes.setObjectName(u"txt_permissoes")

        self.verticalLayout_68.addWidget(self.txt_permissoes)

        self.frame_29 = QFrame(self.frame_28)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.perm_n = QRadioButton(self.frame_29)
        self.perm_n.setObjectName(u"perm_n")

        self.horizontalLayout_33.addWidget(self.perm_n)

        self.perm_s = QRadioButton(self.frame_29)
        self.perm_s.setObjectName(u"perm_s")

        self.horizontalLayout_33.addWidget(self.perm_s)


        self.verticalLayout_68.addWidget(self.frame_29)


        self.gridLayout_3.addWidget(self.frame_28, 4, 1, 1, 1)

        self.frame_26 = QFrame(self.layout_adc_usuario)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_67 = QVBoxLayout(self.frame_26)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.txt_telefone = QLabel(self.frame_26)
        self.txt_telefone.setObjectName(u"txt_telefone")

        self.verticalLayout_67.addWidget(self.txt_telefone)

        self.input_telefone_adc_usuario = QLineEdit(self.frame_26)
        self.input_telefone_adc_usuario.setObjectName(u"input_telefone_adc_usuario")
        self.input_telefone_adc_usuario.setMaximumSize(QSize(400, 16777215))
        self.input_telefone_adc_usuario.setStyleSheet(u"")
        self.input_telefone_adc_usuario.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_67.addWidget(self.input_telefone_adc_usuario)


        self.gridLayout_3.addWidget(self.frame_26, 4, 0, 1, 1)


        self.verticalLayout_36.addWidget(self.layout_adc_usuario)

        self.frame_27 = QFrame(self.config_usuarios_2)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.btn_procurar_ft_adc_usuario = QPushButton(self.frame_27)
        self.btn_procurar_ft_adc_usuario.setObjectName(u"btn_procurar_ft_adc_usuario")
        self.btn_procurar_ft_adc_usuario.setMinimumSize(QSize(250, 0))
        self.btn_procurar_ft_adc_usuario.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_32.addWidget(self.btn_procurar_ft_adc_usuario)

        self.label_img_adc_usuario = QLabel(self.frame_27)
        self.label_img_adc_usuario.setObjectName(u"label_img_adc_usuario")
        self.label_img_adc_usuario.setMaximumSize(QSize(200, 200))

        self.horizontalLayout_32.addWidget(self.label_img_adc_usuario)


        self.verticalLayout_36.addWidget(self.frame_27)

        self.btn_adc_usuario = QPushButton(self.config_usuarios_2)
        self.btn_adc_usuario.setObjectName(u"btn_adc_usuario")

        self.verticalLayout_36.addWidget(self.btn_adc_usuario)

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
        __qtreewidgetitem4 = QTreeWidgetItem()
        __qtreewidgetitem4.setTextAlignment(1, Qt.AlignCenter);
        __qtreewidgetitem4.setTextAlignment(0, Qt.AlignCenter);
        self.tabela_categoria.setHeaderItem(__qtreewidgetitem4)
        self.tabela_categoria.setObjectName(u"tabela_categoria")
        self.tabela_categoria.setMinimumSize(QSize(400, 300))

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


        self.verticalLayout_42.addWidget(self.mainbody)

        TelaPrincipal.setCentralWidget(self.centralwidget)

        self.retranslateUi(TelaPrincipal)

        self.btn_modo_claro_escuro.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_7.setCurrentIndex(3)
        self.stackedWidget_2.setCurrentIndex(2)
        self.stackedWidget_6.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(2)
        self.input_categoria_produto.setCurrentIndex(-1)
        self.input_categoria_produto_2.setCurrentIndex(-1)
        self.input_tipo_valor_2.setCurrentIndex(-1)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget_4.setCurrentIndex(1)
        self.stackedWidget_5.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(TelaPrincipal)
    # setupUi

    def retranslateUi(self, TelaPrincipal):
        TelaPrincipal.setWindowTitle(QCoreApplication.translate("TelaPrincipal", u"MainWindow", None))
        self.img_logo.setText("")
        self.txt_ola_user.setText("")
        self.btn_sair.setText("")
        self.btn_tela_principal.setText(QCoreApplication.translate("TelaPrincipal", u"TELA PRINCIPAL", None))
        self.btn_pdv.setText(QCoreApplication.translate("TelaPrincipal", u"PDV", None))
        self.btn_estoque.setText(QCoreApplication.translate("TelaPrincipal", u"ESTOQUE", None))
        self.btn_relatorios.setText(QCoreApplication.translate("TelaPrincipal", u"RELATORIOS", None))
        self.btn_configuracoes.setText(QCoreApplication.translate("TelaPrincipal", u"CONFIGURA\u00c7\u00d5ES", None))
        self.btn_modo_claro_escuro.setItemText(0, QCoreApplication.translate("TelaPrincipal", u"Modo Claro", None))
        self.btn_modo_claro_escuro.setItemText(1, QCoreApplication.translate("TelaPrincipal", u"Modo Escuro", None))

        self.btn_abrir_caixa.setText(QCoreApplication.translate("TelaPrincipal", u"Abrir Caixa", None))
        self.btn_fechar_caixa.setText(QCoreApplication.translate("TelaPrincipal", u"Fechar Caixa", None))
        self.btn_sangria.setText(QCoreApplication.translate("TelaPrincipal", u"Registrar Sangria", None))
        self.btn_suprimento.setText(QCoreApplication.translate("TelaPrincipal", u"Registrar Suprimento", None))
        self.txt_resumo_mov.setText(QCoreApplication.translate("TelaPrincipal", u"Resumo da Movimenta\u00e7\u00e3o", None))
        self.txt_data.setText(QCoreApplication.translate("TelaPrincipal", u"Data:", None))
        self.txt_abertura_db.setText(QCoreApplication.translate("TelaPrincipal", u"Abertura:", None))
        self.txt_operador_db.setText(QCoreApplication.translate("TelaPrincipal", u"Operador:", None))
        self.icon_recebimento_vendas.setText("")
        self.txt_recebimento_vendas.setText(QCoreApplication.translate("TelaPrincipal", u"Recebimentos de Vendas", None))
        self.txt_total_vendas_db.setText(QCoreApplication.translate("TelaPrincipal", u"Total de Vendas: R$ 0,00", None))
        self.txt_pix.setText(QCoreApplication.translate("TelaPrincipal", u"Pix", None))
        self.txt_total_vendas_pix_db.setText(QCoreApplication.translate("TelaPrincipal", u"R$ 0,00", None))
        self.txt_debito.setText(QCoreApplication.translate("TelaPrincipal", u"D\u00e9bito", None))
        self.txt_total_vendas_debito_db.setText(QCoreApplication.translate("TelaPrincipal", u"R$0,00", None))
        self.txt_credito.setText(QCoreApplication.translate("TelaPrincipal", u"Cr\u00e9dito", None))
        self.txt_total_vendas_credito_db.setText(QCoreApplication.translate("TelaPrincipal", u"R$0,00", None))
        self.txt_dinheiro.setText(QCoreApplication.translate("TelaPrincipal", u"Dinheiro", None))
        self.txt_total_venda_dinheiro_db.setText(QCoreApplication.translate("TelaPrincipal", u"R$0,00", None))
        self.icon_mov_gaveta.setText("")
        self.txt_mov_gaveta.setText(QCoreApplication.translate("TelaPrincipal", u"Movimenta\u00e7\u00e3o da Gaveta", None))
        self.txt_total_gaveta_db.setText(QCoreApplication.translate("TelaPrincipal", u"Total em Gaveta: R$ 0,00", None))
        self.icon_adc.setText("")
        self.txt_adicoes.setText(QCoreApplication.translate("TelaPrincipal", u"Adi\u00e7\u00f5es", None))
        self.txt_saldo_inicial.setText(QCoreApplication.translate("TelaPrincipal", u"Saldo Incial", None))
        self.txt_saldo_inicial_db.setText(QCoreApplication.translate("TelaPrincipal", u"R$ 0,00", None))
        self.txt_vendas_dinheiro.setText(QCoreApplication.translate("TelaPrincipal", u"Vendas em Dinheiro", None))
        self.txt_vendas_dinheiro_db.setText(QCoreApplication.translate("TelaPrincipal", u"R$ 0,00", None))
        self.txt_suprimento.setText(QCoreApplication.translate("TelaPrincipal", u"Suprimento", None))
        self.txt_suprimento_db.setText(QCoreApplication.translate("TelaPrincipal", u"R$ 0,00", None))
        self.icnon_retirada.setText("")
        self.txt_retiradas.setText(QCoreApplication.translate("TelaPrincipal", u"Retiradas", None))
        self.txt_sangria.setText(QCoreApplication.translate("TelaPrincipal", u"Sangria", None))
        self.txt_total_sangria_db.setText(QCoreApplication.translate("TelaPrincipal", u"R$ 0,00", None))
        ___qtreewidgetitem = self.tabela_hist_mov.headerItem()
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("TelaPrincipal", u"Valor(R$)", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("TelaPrincipal", u"Observa\u00e7\u00e3o", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("TelaPrincipal", u"Forma de Pagamento", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("TelaPrincipal", u"Descri\u00e7\u00e3o", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("TelaPrincipal", u"Data e hora", None));
        self.txt_quantidade_caixa_abrir.setText(QCoreApplication.translate("TelaPrincipal", u"Quantidade no Caixa", None))
        self.btn_confirmar_abrir.setText(QCoreApplication.translate("TelaPrincipal", u"Confirmar", None))
        self.txt_quantidade_caixa_fechar.setText(QCoreApplication.translate("TelaPrincipal", u"Quantidade no Caixa", None))
        self.btn_confirmar_fechar.setText(QCoreApplication.translate("TelaPrincipal", u"Confirmar", None))
        self.txt_sangria_titulo.setText(QCoreApplication.translate("TelaPrincipal", u"Registrar Sangria (retirada de dinheiro do caixa)", None))
        self.txt_valor_sangria.setText(QCoreApplication.translate("TelaPrincipal", u"Valor da Sangria*", None))
        self.txt_vendedor_responsavel_sangria.setText(QCoreApplication.translate("TelaPrincipal", u"ID do Vendedor Respons\u00e1vel*", None))
        self.txt_obs_sangria.setText(QCoreApplication.translate("TelaPrincipal", u"Observa\u00e7\u00e3o", None))
        self.btn_cancelar_sangria.setText(QCoreApplication.translate("TelaPrincipal", u"Cancelar", None))
        self.btn_confirmar_sangria.setText(QCoreApplication.translate("TelaPrincipal", u"Confirmar", None))
        self.txt_tirulo_suprimento.setText(QCoreApplication.translate("TelaPrincipal", u"Registrar Suprimento (adi\u00e7\u00e3o de dinheiro ao Caixa)", None))
        self.txt_valor_suprimento.setText(QCoreApplication.translate("TelaPrincipal", u"Valor do Suprimento*", None))
        self.txt_vendedor_responsavel_suprimento.setText(QCoreApplication.translate("TelaPrincipal", u"ID do Vendedor Responsavel*", None))
        self.txt_obs_suprimento.setText(QCoreApplication.translate("TelaPrincipal", u"Observa\u00e7\u00e3o", None))
        self.btn_cancelar_suprimento.setText(QCoreApplication.translate("TelaPrincipal", u"Cancelar", None))
        self.btn_confirmar_suprimento.setText(QCoreApplication.translate("TelaPrincipal", u"Confirmar", None))
        self.btn_pesquisar_produto.setText("")
        self.input_pdv_categoria.setPlaceholderText(QCoreApplication.translate("TelaPrincipal", u"TODOS", None))
        self.txt_pdv_nome.setText("")
        self.txt_pdv_valor.setText("")
        self.btn_pdv_menos.setText("")
        self.btn_pdv_mais.setText("")
        self.btn_adc_carrinho.setText(QCoreApplication.translate("TelaPrincipal", u"Adicionar ao Carrinho", None))
        self.txt_pdv_nome_2.setText("")
        self.txt_pdv_valor_2.setText("")
        self.input_pdv_quant_2.setPlaceholderText(QCoreApplication.translate("TelaPrincipal", u"KG", None))
        self.btn_adc_carrinho_2.setText(QCoreApplication.translate("TelaPrincipal", u"Adicionar ao Carrinho", None))
        ___qtreewidgetitem1 = self.tabela_carrinho.headerItem()
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("TelaPrincipal", u"Total", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("TelaPrincipal", u"Pre\u00e7o Un.", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("TelaPrincipal", u"Qtd.", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("TelaPrincipal", u"Produto", None));
        self.btn_remover_produto_carrinho.setText(QCoreApplication.translate("TelaPrincipal", u"Remover Produto do Carrinho", None))
        self.txt_valor_total_texto.setText(QCoreApplication.translate("TelaPrincipal", u"Valor Total", None))
        self.txt_valor_total.setText("")
        self.input_pdv_forma_pagamento.setItemText(0, QCoreApplication.translate("TelaPrincipal", u"Pix", None))
        self.input_pdv_forma_pagamento.setItemText(1, QCoreApplication.translate("TelaPrincipal", u"D\u00e9bito", None))
        self.input_pdv_forma_pagamento.setItemText(2, QCoreApplication.translate("TelaPrincipal", u"Cr\u00e9dito", None))
        self.input_pdv_forma_pagamento.setItemText(3, QCoreApplication.translate("TelaPrincipal", u"Dinheiro", None))

        self.input_pdv_forma_pagamento.setPlaceholderText(QCoreApplication.translate("TelaPrincipal", u"Forma de Pagamento", None))
        self.btn_finaliza_compra.setText(QCoreApplication.translate("TelaPrincipal", u"Finalizar Compra", None))
        self.label_6.setText(QCoreApplication.translate("TelaPrincipal", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Compra Realizada! </span></p><p align=\"center\"><span style=\" font-size:16pt;\">Obrigado Por Comprar no Mercado do Celsadas</span></p></body></html>", None))
        self.input_pesquisar_produto_4.setPlaceholderText(QCoreApplication.translate("TelaPrincipal", u"Procurar Produto", None))
        self.btn_pesquisar_produto_4.setText("")
        self.btn_adc_produto_estoque.setText("")
        self.btn_editar_produto.setText("")
        self.txt_caso_produto_nao_encontra_estoque.setText("")
        ___qtreewidgetitem2 = self.treeWidget.headerItem()
        ___qtreewidgetitem2.setText(4, QCoreApplication.translate("TelaPrincipal", u"CATEGORIA", None));
        ___qtreewidgetitem2.setText(3, QCoreApplication.translate("TelaPrincipal", u"QUANTIDADE", None));
        ___qtreewidgetitem2.setText(2, QCoreApplication.translate("TelaPrincipal", u"PRE\u00c7O", None));
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("TelaPrincipal", u"NOME", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("TelaPrincipal", u"ID", None));
        self.img_produto_estoque.setText("")
        self.txt_quantidade_estoque.setText(QCoreApplication.translate("TelaPrincipal", u"Quantidade", None))
        self.input_quantidade_produto.setPlaceholderText(QCoreApplication.translate("TelaPrincipal", u"QUANTIDADE", None))
        self.btn_adc_foto_produto.setText(QCoreApplication.translate("TelaPrincipal", u"Adicionar Foto", None))
        self.txt_preco_estoque.setText(QCoreApplication.translate("TelaPrincipal", u"Pre\u00e7o Un.", None))
        self.input_preco_produto.setInputMask("")
        self.input_preco_produto.setPlaceholderText(QCoreApplication.translate("TelaPrincipal", u"PRE\u00c7O UN.", None))
        self.txt_categoria_estoque.setText(QCoreApplication.translate("TelaPrincipal", u"Categoria", None))
        self.input_categoria_produto.setPlaceholderText(QCoreApplication.translate("TelaPrincipal", u"CATEGORIA", None))
        self.txt_nome_estoque.setText(QCoreApplication.translate("TelaPrincipal", u"Nome", None))
        self.input_nome_produto.setPlaceholderText(QCoreApplication.translate("TelaPrincipal", u"NOME", None))
        self.label.setText(QCoreApplication.translate("TelaPrincipal", u"Tipo de Valor", None))
        self.input_tipo_valor.setItemText(0, QCoreApplication.translate("TelaPrincipal", u"Por Unidade", None))
        self.input_tipo_valor.setItemText(1, QCoreApplication.translate("TelaPrincipal", u"Por KG", None))

        self.btn_adc_produto.setText(QCoreApplication.translate("TelaPrincipal", u"Adicionar Produto", None))
        self.txt_categoria_estoque_2.setText(QCoreApplication.translate("TelaPrincipal", u"Categoria", None))
        self.input_categoria_produto_2.setPlaceholderText(QCoreApplication.translate("TelaPrincipal", u"CATEGORIA", None))
        self.txt_nome_estoque_2.setText(QCoreApplication.translate("TelaPrincipal", u"Nome", None))
        self.input_nome_produto_2.setPlaceholderText(QCoreApplication.translate("TelaPrincipal", u"NOME", None))
        self.img_produto_estoque_2.setText("")
        self.txt_preco_estoque_2.setText(QCoreApplication.translate("TelaPrincipal", u"Pre\u00e7o Un.", None))
        self.input_preco_produto_2.setInputMask("")
        self.input_preco_produto_2.setPlaceholderText(QCoreApplication.translate("TelaPrincipal", u"PRE\u00c7O UN.", None))
        self.txt_quantidade_estoque_2.setText(QCoreApplication.translate("TelaPrincipal", u"Quantidade", None))
        self.input_quantidade_produto_2.setPlaceholderText(QCoreApplication.translate("TelaPrincipal", u"QUANTIDADE", None))
        self.btn_adc_foto_produto_2.setText(QCoreApplication.translate("TelaPrincipal", u"Adicionar Foto", None))
        self.label_2.setText(QCoreApplication.translate("TelaPrincipal", u"Tipo de Valor", None))
        self.input_tipo_valor_2.setItemText(0, QCoreApplication.translate("TelaPrincipal", u"Por Unidade", None))
        self.input_tipo_valor_2.setItemText(1, QCoreApplication.translate("TelaPrincipal", u"Por KG", None))

        self.input_tipo_valor_2.setPlaceholderText(QCoreApplication.translate("TelaPrincipal", u"Tipo de Valor", None))
        self.btn_adc_produto_2.setText(QCoreApplication.translate("TelaPrincipal", u"Adicionar Produto", None))
        self.txt_produtos_mais_vendidos.setText(QCoreApplication.translate("TelaPrincipal", u"Estoque em Alerta", None))
        self.txt_vendas_ultimos_6_meses.setText(QCoreApplication.translate("TelaPrincipal", u"PRODUTOS MAIS VENDIDOS", None))
        self.txt_lucro_prejuizo.setText(QCoreApplication.translate("TelaPrincipal", u"Desempenho por Operador (TOP 5)", None))
        self.label_4.setText(QCoreApplication.translate("TelaPrincipal", u"Taxa de Pagamento por Forma", None))
        ___qtreewidgetitem3 = self.treeWidget_2.headerItem()
        ___qtreewidgetitem3.setText(5, QCoreApplication.translate("TelaPrincipal", u"PERMISS\u00c3O", None));
        ___qtreewidgetitem3.setText(4, QCoreApplication.translate("TelaPrincipal", u"TELEFONE", None));
        ___qtreewidgetitem3.setText(3, QCoreApplication.translate("TelaPrincipal", u"CPF", None));
        ___qtreewidgetitem3.setText(2, QCoreApplication.translate("TelaPrincipal", u"EMAIL", None));
        ___qtreewidgetitem3.setText(1, QCoreApplication.translate("TelaPrincipal", u"NOME", None));
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("TelaPrincipal", u"ID", None));
        self.btn_adc_user.setText(QCoreApplication.translate("TelaPrincipal", u"Adicionar Usuario", None))
        self.txt_senha.setText(QCoreApplication.translate("TelaPrincipal", u"Senha", None))
        self.input_senha_adc_usuario.setPlaceholderText(QCoreApplication.translate("TelaPrincipal", u"Senha", None))
        self.txt_nome.setText(QCoreApplication.translate("TelaPrincipal", u"Nome", None))
        self.input_nome_adc_usuario.setPlaceholderText(QCoreApplication.translate("TelaPrincipal", u"Nome", None))
        self.txt_email.setText(QCoreApplication.translate("TelaPrincipal", u"Email", None))
        self.input_email_adc_usuario.setPlaceholderText(QCoreApplication.translate("TelaPrincipal", u"Email", None))
        self.txt_cpf.setText(QCoreApplication.translate("TelaPrincipal", u"CPF", None))
        self.input_cpf_adc_usuario.setPlaceholderText(QCoreApplication.translate("TelaPrincipal", u"CPF", None))
        self.txt_permissoes.setText(QCoreApplication.translate("TelaPrincipal", u"Permiss\u00f5es", None))
        self.perm_n.setText(QCoreApplication.translate("TelaPrincipal", u"N\u00e3o", None))
        self.perm_s.setText(QCoreApplication.translate("TelaPrincipal", u"Sim", None))
        self.txt_telefone.setText(QCoreApplication.translate("TelaPrincipal", u"Telefone", None))
        self.input_telefone_adc_usuario.setInputMask("")
        self.input_telefone_adc_usuario.setPlaceholderText(QCoreApplication.translate("TelaPrincipal", u"Telefone", None))
        self.btn_procurar_ft_adc_usuario.setText(QCoreApplication.translate("TelaPrincipal", u"Procurar Foto", None))
        self.label_img_adc_usuario.setText("")
        self.btn_adc_usuario.setText(QCoreApplication.translate("TelaPrincipal", u"Criar Usuario", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tela_config_1), QCoreApplication.translate("TelaPrincipal", u"Tab 1", None))
        ___qtreewidgetitem4 = self.tabela_categoria.headerItem()
        ___qtreewidgetitem4.setText(1, QCoreApplication.translate("TelaPrincipal", u"CATEGORIA", None));
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("TelaPrincipal", u"ID", None));
        self.btn_adc_categoria.setText(QCoreApplication.translate("TelaPrincipal", u"Adicionar Categoria", None))
        self.input_nome_adc_categoria.setInputMask("")
        self.input_nome_adc_categoria.setText("")
        self.input_nome_adc_categoria.setPlaceholderText(QCoreApplication.translate("TelaPrincipal", u"Nome da Categoria", None))
        self.btn_adc_categoria_2.setText(QCoreApplication.translate("TelaPrincipal", u"Criar Categoria", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tela_config_2), QCoreApplication.translate("TelaPrincipal", u"Page", None))
    # retranslateUi

