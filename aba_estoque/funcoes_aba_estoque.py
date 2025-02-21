from aba_estoque.conexao_db import conexaoDB
import customtkinter as ctk
from tkinter import ttk, Scrollbar

class estoque():
    def __init__(self, aba):
        self.aba_estoque = aba

    def mostrarEstoque(self):
        pass
    
    def adcEstoque(self, nome, preco, quant, categoria):
        
        self.conexao = conexaoDB()
        comando = """insert into estoque (nome, preco, quantidade, categoria)
                     values (nome, preco, quant, categoria)
                  """
        valores = (nome, preco, quant, categoria)
        self.conexao.insert_bd(comando, valores)

        comando = "select * from estoque"
        resultado = self.conexao.select_bd(comando)
        
        for i in resultado:
            id, nome, preco, quantidade, categoria = resultado
        self.tabela_estoque.insert("", "end", values=(id, nome, preco, quantidade, categoria))
        self.tabela_estoque.update()




