import customtkinter as ctk
from PIL import Image
from aba_principal.ui_aba_principal import abaPrincipal
from aba_estoque.ui_aba_estoque import abaEstoque

class telaPrincipal(ctk.CTk):
    def __init__(self, usuario):
        super().__init__()  
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)
        self.configure(fg_color="#DBDBDB")
        
        self.img_logo = ctk.CTkImage(light_image=Image.open("imgs/logo_mercado.png"), size=(150, 100))

        self.txt_logo = ctk.CTkLabel(self, text="", image=self.img_logo)
        self.txt_logo.grid(row=0, column=0, sticky="nw", padx=20, pady=(10, 0))

        self.layout_superior_direito =  ctk.CTkFrame(self, fg_color="transparent", height=100, width=295)  
        self.layout_superior_direito.grid(row=0, column=1, sticky="ne", padx=20, pady=(10, 0))
        self.layout_superior_direito.grid_propagate(False)
        self.layout_superior_direito.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.txt_ola_user = ctk.CTkLabel(self.layout_superior_direito, text=f"Olá, {usuario}", font=("poppins", 24))
        self.txt_ola_user.grid(row=0, column=0, padx=20)

        self.btn_voltar = ctk.CTkButton(self.layout_superior_direito, text="Voltar", font=("poppins", 24))
        self.btn_voltar.grid(row=0, column=1)

        self.tabview = ctk.CTkTabview(self, width=1200, height=650, fg_color="white")
        self.tabview.grid(row=1, column=0, columnspan=2, sticky="nsew", pady=(0, 20), padx=20)

        abaPrincipal(self.tabview)
        abaEstoque(self.tabview)

if __name__ == "__main__":
    app = telaPrincipal("Celso")
    app.mainloop()