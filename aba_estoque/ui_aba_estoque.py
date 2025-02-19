import customtkinter as ctk
from PIL import Image

class abaEstoque():
    def __init__(self, tabview):
        self.aba_estoque = tabview.add("Estoque")
        self.aba_estoque.rowconfigure(0, weight=1)
        self.aba_estoque.columnconfigure(0, weight=1)

        self.input_procurar_produtos = ctk.CTkEntry(self.aba_estoque,
                                                    placeholder_text="Procurar Produto usando ID ou Nome", width=350, 
                                                    justify="center",
                                                    fg_color="transparent",
                                                    border_width=0,
                                                    font=("poppins", 20),
                                                    text_color="#909090")
        self.input_procurar_produtos.grid(row=0, column=0, pady=20, padx=20, sticky="n")

        self.linha = ctk.CTkFrame(self.aba_estoque, height=2, fg_color="#909090", width=350)
        self.linha.grid(row=0, column=0, pady=45, padx=20, sticky="n")

        self.icone_lupa = ctk.CTkImage(Image.open("imgs\icone_lupa.png"), size=(15, 15))

        self.btn_procurar_produto_icon = ctk.CTkButton(self.aba_estoque, text="", image=self.icone_lupa, width=20, height=20, corner_radius=100)
        self.btn_procurar_produto_icon.grid(row=0, column=0, pady=20, padx=(450, 20), sticky="n")

        self.icone_mais = ctk.CTkImage(Image.open("imgs\icone_mais.png"), size=(15, 15))

        self.btn_adc_produto_icon = ctk.CTkButton(self.aba_estoque, text="", image=self.icone_mais, width=20, height=20, corner_radius=100, command=lambda: self.janela_adc_produto())
        self.btn_adc_produto_icon.grid(row=0, column=0, pady=20, padx=(550, 20), sticky="n")


    def janela_adc_produto(self):
        self.frame_procurar_produto = ctk.CTkFrame(self.aba_estoque, width=1000, height=600, fg_color="white")
        self.frame_procurar_produto.grid(row=0, column=0, sticky="nsew")
        self.frame_procurar_produto.columnconfigure(0, weight=1)

        self.input_nome = ctk.CTkEntry(self.frame_procurar_produto,
                                       placeholder_text="Nome",
                                       width=350, 
                                       justify="center",
                                       fg_color="transparent",
                                       border_width=0,
                                       font=("poppins", 20),
                                       text_color="#909090")
        self.input_nome.grid(row=0, column=0, pady=(25, 0), padx=20, sticky="n")
        self.linha = ctk.CTkFrame(self.frame_procurar_produto, height=2, fg_color="#909090", width=350)
        self.linha.grid(row=0, column=0, pady=(55, 50), padx=20, sticky="n")

        self.input_preco = ctk.CTkEntry(self.frame_procurar_produto,
                                         placeholder_text="Preço Un. R$",
                                         width=350, 
                                         justify="center",
                                         fg_color="transparent",
                                         border_width=0,
                                         font=("poppins", 20),
                                         text_color="#909090")
        self.input_preco.grid(row=1, column=0, padx=20, sticky="n")
        self.linha = ctk.CTkFrame(self.frame_procurar_produto, height=2, fg_color="#909090", width=350)
        self.linha.grid(row=1, column=0, pady=(30, 50), padx=20, sticky="n")

        self.input_quantidade = ctk.CTkEntry(self.frame_procurar_produto,
                                             placeholder_text="Quantidade",
                                             width=350, 
                                             justify="center",
                                             fg_color="transparent",
                                             border_width=0,
                                             font=("poppins", 20),
                                             text_color="#909090")
        self.input_quantidade.grid(row=2, column=0, pady=(0, 25), padx=20, sticky="n")
        self.linha = ctk.CTkFrame(self.frame_procurar_produto, height=2, fg_color="#909090", width=350)
        self.linha.grid(row=2, column=0, pady=(30, 55), padx=20, sticky="n")

        self.btn_adc_produto = ctk.CTkButton(self.frame_procurar_produto,
                                             text="Adcionar Porduto",
                                             font=("poppins", 20))
        self.btn_adc_produto.grid(row=3, column=0, padx=20, sticky="n")