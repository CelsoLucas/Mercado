from customtkinter import CTk
from ui_tela_login import telaLogin

class main(CTk):
    def __init__(self):
        super().__init__()

        self.tela_login = telaLogin()
        self.tela_login.mainloop()

if __name__ == "__main__":
    app = main()
    app.mainloop()