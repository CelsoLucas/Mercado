
class cmdTema():
    def __init__(self, window):
        self.window = window
        self.window.tela_principal.btn_modo_claro_escuro.currentIndexChanged.connect(self.status)    
    
    def status(self, index):
        if index == 0:  # Modo Claro
            self.tema_claro()
        elif index == 1:  # Modo Escuro
            self.tema_escuro()


    def tema_claro(self):
        self.window.setStyleSheet(u"/* Estilo geral para a janela principal */\n"
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
        
    def tema_escuro(self):
        self.window.setStyleSheet(u"/* Estilo geral para a janela principal */\n"
"QMainWindow {\n"
"    background-color: #0F172A; /* Azul escuro profundo */\n"
"}\n"
"\n"
"/* Menu superior */\n"
"#menu {\n"
"    background-color: #1E293B; /* Azul escuro acinzentado */\n"
"    border-bottom: 1px solid #334155;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"#img_logo {\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #22D3EE; /* Ciano brilhante */\n"
"}\n"
"\n"
"#txt_ola_user {\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"    font-size: 16px;\n"
"    color: #94A3B8; /* Cinza azulado claro */\n"
"}\n"
"\n"
"#btn_sair {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"#btn_sair:hover {\n"
"    background-color: #334155;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* Menu lateral */\n"
"#menu_lateral {\n"
"    background-color: #1E293B; /* Azul escuro acinzentado */\n"
"    border-right: 1px solid #334155;\n"
"}\n"
"\n"
"#btn_tela_principal"
                        ", #btn_pdv, #btn_estoque, #btn_relatorios, #btn_configuracoes {\n"
"    background-color: #1E293B;\n"
"    color: #CBD5E1; /* Cinza azulado claro */\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
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
"    background-color: #22D3EE; /* Ciano brilhante */\n"
"    color: #0F172A; /* Azul escuro para contraste */\n"
"}\n"
"\n"
"/* \u00c1rea principal */\n"
"#_info_principal {\n"
"    background-color: #0F172A;\n"
"    padding: 20px;\n"
"}\n"
"\n"
"/* Bot\u00f5es gerais */\n"
"QPushButton {\n"
"    background-color: #22D3EE; /* Ciano brilhante */\n"
"    color: #0F172A; /* Azul escuro para contraste */\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"    paddin"
                        "g: 10px 20px;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #67E8F9; /* Ciano mais claro */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0891B2; /* Ciano escuro */\n"
"}\n"
"\n"
"/* Inputs */\n"
"QLineEdit, QTextEdit {\n"
"    background-color: #334155; /* Cinza azulado escuro */\n"
"    border: 1px solid #475569;\n"
"    border-radius: 6px;\n"
"    padding: 8px;\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"    font-size: 14px;\n"
"    color: #F1F5F9; /* Branco azulado */\n"
"}\n"
"\n"
"QLineEdit:focus, QTextEdit:focus {\n"
"    border: 1px solid #22D3EE;\n"
"}\n"
"\n"
"/* ComboBox */\n"
"QComboBox {\n"
"    background-color: #334155;\n"
"    border: 1px solid #475569;\n"
"    border-radius: 6px;\n"
"    padding: 8px;\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"    font-size: 14px;\n"
"    color: #F1F5F9;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #67E8F9;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
" "
                        "   border: none;\n"
"    width: 20px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #334155;\n"
"    border: 1px solid #475569;\n"
"    selection-background-color: #22D3EE;\n"
"    selection-color: #0F172A;\n"
"}\n"
"\n"
"/* Frames */\n"
"QFrame {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#layout_dados_sem_tabela, #lado_esquerdo, #lado_direito {\n"
"    background-color: #1E293B;\n"
"    border-radius: 10px;\n"
"    padding: 15px;\n"
"}\n"
"\n"
"/* Labels */\n"
"QLabel {\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"    color: #CBD5E1; /* Cinza azulado claro */\n"
"}\n"
"\n"
"#txt_resumo_mov, #txt_mov_gaveta, #txt_recebimento_vendas {\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    color: #F1F5F9; /* Branco azulado */\n"
"}\n"
"\n"
"#txt_data, #txt_abertura_db, #txt_operador_db {\n"
"    font-size: 14px;\n"
"    color: #94A3B8; /* Cinza azulado claro */\n"
"}\n"
"\n"
"/* Tabelas */\n"
"QTreeWidget {\n"
"    background-color: #1E293B;\n"
"    border: 1px sol"
                        "id #475569;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"    font-size: 14px;\n"
"    color: #CBD5E1;\n"
"}\n"
"\n"
"QTreeWidget::item {\n"
"    padding: 8px;\n"
"}\n"
"\n"
"QTreeWidget::item:hover {\n"
"    background-color: #334155;\n"
"}\n"
"\n"
"QTreeWidget::item:selected {\n"
"    background-color: #22D3EE;\n"
"    color: #0F172A;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #475569;\n"
"    padding: 8px;\n"
"    border: none;\n"
"    font-weight: bold;\n"
"    color: #CBD5E1;\n"
"}\n"
"\n"
"/* Scroll Area */\n"
"QScrollArea {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background: #475569;\n"
"    width: 10px;\n"
"    margin: 0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #64748B;\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    hei"
                        "ght: 0;\n"
"}\n"
"\n"
"/* Tab Widget */\n"
"QTabWidget::pane {\n"
"    border: 1px solid #475569;\n"
"    background-color: #1E293B;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: #475569;\n"
"    color: #94A3B8;\n"
"    padding: 10px 20px;\n"
"    margin-right: 2px;\n"
"    border-top-left-radius: 6px;\n"
"    border-top-right-radius: 6px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: #1E293B;\n"
"    color: #F1F5F9;\n"
"    border-bottom: 2px solid #22D3EE;\n"
"}\n"
"\n"
"QTabBar::tab:hover:!selected {\n"
"    background-color: #334155;\n"
"}\n"
"\n"
"/* Estilo espec\u00edfico para relat\u00f3rios */\n"
"#layout_relatorios_1, #layout_relatorios_2, #layout_relatorios_3, #layout_relatorios_4 {\n"
"    background-color: #1E293B;\n"
"    border-radius: 10px;\n"
"    padding: 15px;\n"
"}\n"
"\n"
"/* Bot\u00f5es de a\u00e7\u00e3o (ex.: Abrir Caixa, Fechar Caixa) */\n"
"#btn_abrir_caixa, #btn_fechar_caixa, #btn_sangria, #btn_suprimento {\n"
"    background-col"
                        "or: #A855F7; /* Roxo vibrante */\n"
"    color: #0F172A; /* Azul escuro para contraste */\n"
"}\n"
"\n"
"#btn_abrir_caixa:hover, #btn_fechar_caixa:hover, #btn_sangria:hover, #btn_suprimento:hover {\n"
"    background-color: #C084FC; /* Roxo mais claro */\n"
"}\n"
"\n"
"/* Bot\u00f5es de cancelar */\n"
"#btn_cancelar_sangria, #btn_cancelar_suprimento {\n"
"    background-color: #EF4444; /* Vermelho escuro */\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"#btn_cancelar_sangria:hover, #btn_cancelar_suprimento:hover {\n"
"    background-color: #F87171; /* Vermelho mais claro */\n"
"}")