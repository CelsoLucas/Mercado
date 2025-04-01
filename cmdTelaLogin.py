import smtplib
import random
import string
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from PySide6.QtWidgets import QMessageBox
import hashlib
from conexao_db import conexaoDB
import dns.resolver


class CmdTelaLogin:
    def __init__(self, tela):
        self.tela = tela
        self.codigos_temporarios = {}
        self.conexao = conexaoDB()
        
    def voltar(self):
        self.tela.stackedWidget.setCurrentIndex(0)

    def gerar_codigo_recuperacao(self):
        """Gera um código de 6 dígitos"""
        return ''.join(random.choices(string.digits, k=6))

    def validar_email(self, email):
        try:
            dominio = email.split('@')[1]
            registros_mx = dns.resolver.resolve(dominio, 'MX')
            return bool(registros_mx)
        except:
            return False
        
    def enviar_email_recuperacao(self):
        """Envia email com código de recuperação usando o email do QLineEdit"""
        email_destinatario = self.tela.input_email.text().strip()

        email_valido = self.validar_email(email_destinatario)
        if email_valido == False:
            QMessageBox.warning(None, "error", "Digite um email valido!")
            return
        
        cursor = self.conexao.get_cursor()
        comando = "select * from usuarios where email = %s"
        cursor.execute(comando, (email_destinatario,))
        resultado = cursor.fetchone()
        if resultado is None:
            QMessageBox.warning(None, "error", f"Nenhuma conta usando o email {email_destinatario} encontrada!")
            return
        
        if not email_destinatario:
            QMessageBox.warning(None, "Erro", "Por favor, insira um email válido!")
            return False

        # Configurações do servidor de email
        email_remetente = "mercadocelsadas@gmail.com"
        senha_email = "jkna zlcx ahxi kyqe"  # Senha de aplicativo para Gmail

        # Gera o código
        codigo = self.gerar_codigo_recuperacao()
        self.codigos_temporarios[email_destinatario] = codigo

        # Configura o email
        assunto = "Recuperação de Senha"
        corpo = f"""
        Olá,
        
        Recebemos uma solicitação para redefinir sua senha. Use o código abaixo:
        
        Código de verificação: {codigo}
        
        Este código expira em 15 minutos.
        Se você não solicitou isso, ignore este email.
        
        Atenciosamente,
        Sua Equipe
        """

        msg = MIMEMultipart()
        msg['From'] = email_remetente
        msg['To'] = email_destinatario
        msg['Subject'] = assunto
        msg.attach(MIMEText(corpo, 'plain'))

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email_remetente, senha_email)
            server.send_message(msg)
            server.quit()
            
            QMessageBox.information(None, "Sucesso", 
                                  f"Código enviado para {email_destinatario}")
            return True
        except Exception as e:
            QMessageBox.critical(None, "Erro", f"Erro ao enviar email: {str(e)}")
            return False

    def verificar_e_mudar_senha(self):
        email = self.tela.input_email.text().strip()
        codigo_digitado = self.tela.input_cod.text().strip()  # Assumindo um QLineEdit para o código
        nova_senha = self.tela.input_nova_senha.text().strip()
        nova_senha_conf = self.tela.input_confirmar_senha.text().strip()   # Assumindo um QLineEdit para a nova senha
        if not all([email, codigo_digitado, nova_senha, nova_senha_conf]):
            QMessageBox.warning(None, "Erro", "Preencha todos os campos!")
            return
        
        # Verifica o código
        if email in self.codigos_temporarios and self.codigos_temporarios[email] == codigo_digitado:
            if nova_senha != nova_senha_conf:
                QMessageBox.warning(None, "error", "As senhas devem ser iguais!")
                return
            # Criptografa a nova senha com SHA-256
            senha_criptografada = hashlib.sha256(nova_senha.encode()).hexdigest()

            # Conecta ao banco de dados

            # Atualiza a senha no banco
            cursor = self.conexao.get_cursor()
            query = "UPDATE usuarios SET senha = %s WHERE email = %s"
            cursor.execute(query, (senha_criptografada, email))
            self.conexao.commit()

            # Verifica se alguma linha foi afetada
            if cursor.rowcount > 0:
                QMessageBox.information(None, "Sucesso", "Senha alterada com sucesso!")
                del self.codigos_temporarios[email]  # Remove o código após sucesso
                self.tela.stackedWidget.setCurrentIndex(0)
            else:
                QMessageBox.warning(None, "Erro", "Email não encontrado no sistema!")
                return
            cursor.close()
            self.conexao.close()
        else:
            QMessageBox.warning(None, "Erro", "Código inválido! Verifique seu Email!")
            return