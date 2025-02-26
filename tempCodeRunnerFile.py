   def check_login(self):
        cursor = self.conexao.cursor()
        
        comando = "SELECT senha, img_local FROM usuarios WHERE email = %s"
        cursor.execute(comando, (self.tela_login.input_user.text(),))
        resultado = cursor.fetchone()
        
        if not resultado:
            QMessageBox.warning(self, "Erro", "Usuário inválido!")
            return
        
        senha_armazenada, foto_perfil = resultado
        
        # Gerar o hash da senha digitada pelo usuário
        comando_senha = "SELECT SHA2(%s, 256)"
        cursor.execute(comando_senha, (self.tela_login.input_senha.text(),))
        senha_digitada_hash = cursor.fetchone()[0]

        # Verificar se o hash da senha digitada corresponde ao armazenado no banco de dados
        if senha_digitada_hash != senha_armazenada:
            QMessageBox.warning(self, "Erro", "Senha inválida!")
        else:
            QMessageBox.information(self, "Sucesso", f"Bem-vindo, {self.tela_login.input_user.text()}!")
            self.init_tela_principal()
        
        cursor.close()