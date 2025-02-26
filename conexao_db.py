import mysql.connector

class conexaoDB():
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="celsadas",
            password="33880188",
            database="mercado"
        )
    
    def select_db(self, comando, valores):
        cursor = self.conexao.cursor()
        cursor.execute(comando, valores)
        return cursor.fetchall()