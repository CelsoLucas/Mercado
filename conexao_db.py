import mysql.connector

class conexaoDB:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="celsadas",
            password="33880188",
            database="mercado"
        )
    
    def get_cursor(self):
        return self.conexao.cursor()
    
    def commit(self):
        self.conexao.commit()