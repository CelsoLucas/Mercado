    def telaprincipal(self):
        self.tela_principal.stackedWidget.setCurrentIndex(0)
        self.telaprin = cmdPaginaPrincipal(self.tela_principal)
        self.tela_principal.btn_abrir_caixa.clicked.connect(self.telaprin.tela_abrir_caixa)
        self.tela_principal.btn_fechar_caixa.clicked.connect(self.telaprin.tela_fechar_caixa)
        self.tela_principal.btn_sangria.clicked.connect(self.telaprin.tela_sangria)
        self.tela_principal.btn_suprimento.clicked.connect(self.telaprin.tela_suprimento)