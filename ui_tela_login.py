from customtkinter import *
from checker import checker

class telaLogin(CTk):
    def __init__(self):
        super().__init__()

        self.title("Login")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self._set_appearance_mode("blue")
        self.configure(fg_color="#DBDBDB")
        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()
        self.geometry(f"{largura_tela}x{altura_tela}")

        self.frame_login = CTkFrame(self, width=500, height=550, fg_color="white", corner_radius=20) 
        self.frame_login.grid(row=0, column=0)
        self.frame_login.grid_propagate(False)
        self.frame_login.grid_columnconfigure(0, weight=1)

        for i in range(6):
            self.frame_login.grid_rowconfigure(i, weight=1)

        self.txt_login = CTkLabel(self.frame_login, text="LOGIN", font=("poppins", 40, "bold"))
        self.txt_login.grid(pady=10, row=0, column=0)

        self.input_usuario = CTkEntry(self.frame_login,
                                      placeholder_text="Usuario",
                                      fg_color="transparent",
                                      border_width=0,
                                      font=("poppins", 20),
                                      width=410,
                                      text_color="#909090")
        self.input_usuario.grid(pady=(0, 30), row=2, column=0)

        # Linha abaixo do Entry (borda inferior)
        self.linha = CTkFrame(self.frame_login, height=2, fg_color="#909090", width=410)
        self.linha.grid(row=2, column=0)

        self.input_senha = CTkEntry(self.frame_login,
                                      placeholder_text="Senha",
                                      fg_color="transparent",
                                      border_width=0,
                                      font=("poppins", 20),
                                      width=410,
                                      text_color="#909090",
                                      show="*")
        self.input_senha.grid(pady=(0, 30), row=4, column=0)
        self.linha = CTkFrame(self.frame_login, height=2, fg_color="#909090", width=410)
        self.linha.grid(row=4, column=0)
        
        self.btn_login = CTkButton(self.frame_login, text="LOGIN", font=("poppins", 20), fg_color="#D9D9D9", text_color="black", width=176, height=53, command=lambda:
                                                        checker(self.input_usuario.get(),
                                                                  self.input_senha.get(),
                                                                  self.txt_validacao))
        self.btn_login.grid(pady=(10, 0), row=5, column=0)

        self.txt_validacao = CTkLabel(self.frame_login, text="", font=("poppins", 20))
        self.txt_validacao.grid(pady=(0, 50), row=6, column=0)    
