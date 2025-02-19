import customtkinter as ctk

class abaPrincipal():
    def __init__(self, tabview):
        self.aba_principal = tabview.add("Página Principal")
        self.aba_principal.rowconfigure(0, weight=1)
        self.aba_principal.columnconfigure(0, weight=1)

        self.frame1 = ctk.CTkFrame(self.aba_principal, width=225, height=225, fg_color="#DBDBDB")
        self.frame1.grid(row=0, column=0, padx=(200, 50), pady=(25, 0), sticky="nw")
        self.frame1.grid_propagate(False)
        self.frame1.columnconfigure(0, weight=1)
        self.frame1.rowconfigure(0, weight=1)
        self.frame1.rowconfigure(1, weight=1)

        self.txt_vendas_dia = ctk.CTkLabel(self.frame1, text="Vendas do Dia", font=("poppins", 22))
        self.txt_vendas_dia.grid(row=0, pady=10, padx=10, sticky="n")

        self.txt_vendas_dia_db = ctk.CTkLabel(self.frame1, text="R$", font=("poppins", 20))
        self.txt_vendas_dia_db.grid(row=1, pady=10, padx=10, sticky="n")

        self.frame2 = ctk.CTkFrame(self.aba_principal, width=225, height=225, fg_color="#DBDBDB")
        self.frame2.grid(row=0, column=1, padx=(50, 50), pady=(25, 0), sticky="n")
        self.frame2.grid_propagate(False)
        self.frame2.columnconfigure(0, weight=1)
        self.frame2.rowconfigure(0, weight=1)
        self.frame2.rowconfigure(1, weight=1)

        self.txt_vendas_semana = ctk.CTkLabel(self.frame2, text="Vendas da Semana", font=("poppins", 22))
        self.txt_vendas_semana.grid(row=0, pady=10, padx=10, sticky="n")

        self.txt_vendas_semana_db = ctk.CTkLabel(self.frame2, text="R$", font=("poppins", 20))
        self.txt_vendas_semana_db.grid(row=1, pady=10, padx=10, sticky="n")

        self.frame3 = ctk.CTkFrame(self.aba_principal, width=225, height=225, fg_color="#DBDBDB")
        self.frame3.grid(row=0, column=2, padx=(50, 200), pady=(25, 0), sticky="ne")
        self.frame3.grid_propagate(False)
        self.frame3.columnconfigure(0, weight=1)
        self.frame3.rowconfigure(0, weight=1)
        self.frame3.rowconfigure(1, weight=1)

        self.txt_vendas_mes = ctk.CTkLabel(self.frame3, text="Vendas do Mês", font=("poppins", 22))
        self.txt_vendas_mes.grid(row=0, pady=10, padx=10, sticky="n")

        self.txt_vendas_mes_db = ctk.CTkLabel(self.frame3, text="R$", font=("poppins", 20))
        self.txt_vendas_mes_db.grid(row=1, pady=10, padx=10, sticky="n")

        self.frame4 = ctk.CTkFrame(self.aba_principal, width=250, height=300, fg_color="#DBDBDB")
        self.frame4.grid(row=1, column=0, columnspan=3, padx=(200, 200), pady=(25, 25), sticky="nsew")
        self.frame4.grid_propagate(False)
        self.frame4.columnconfigure(0, weight=1)
        self.frame4.rowconfigure(0, weight=1)

        self.txt_produtos_baixo_estoque= ctk.CTkLabel(self.frame4, text="Produtos com Baixo Estoque", font=("poppins", 22))
        self.txt_produtos_baixo_estoque.grid(row=0, pady=10, padx=10, sticky="nw")

        self.txt_produtos_baixo_estoque_db = ctk.CTkLabel(self.frame4, text="produto", font=("poppins", 20))
        self.txt_produtos_baixo_estoque_db.grid(row=0, pady=10, padx=10, sticky="w")