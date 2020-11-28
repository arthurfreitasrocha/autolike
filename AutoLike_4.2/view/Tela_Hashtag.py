from tkinter import *
import os

from .Tela_Inicio import gerarInterface

def gerarInterfaceHashtag(janela):

    """
    INFORMAÇÕES NECESSÁRIAS
    """
    diretorio_atual = os.getcwd()

    def fechar_janela():
        janela.destroy()
        gerarInterface()

    janela = Tk()

    " IMAGEM "
    logo = PhotoImage(file=f"{diretorio_atual}\\view\\images\\logo.png")

    frame_imagem = Frame(janela, width=500, height=100, bg="Salmon").pack(side=TOP)
    Label(frame_imagem, image=logo, bg="salmon").place(x=210, y=15)


    " LOGIN E SENHA "
    frame_login_senha = Frame(janela, width=500, height=100, bg="Peach Puff").pack(side=TOP)

    Label(frame_login_senha, text="Login", font=("arial", 13, "bold"), bg="Peach Puff").place(x=30, y=130)
    entry_login = Entry(frame_login_senha, font=("arial", 12), width=40)
    entry_login.place(x=90, y=130)

    Label(frame_login_senha, text="Senha", font=("arial", 13, "bold"), bg="Peach Puff").place(x=30, y=170)
    entry_senha = Entry(frame_login_senha, font=("arial", 12), width=40)
    entry_senha.place(x=90, y=170)


    " BOTÃO ENVIAR "
    frame_enviar = Frame(janela, width=900, height=70, bg="Peach Puff").pack(side=TOP)

    Button(frame_enviar, text="Enviar", font=("arial", 11, "bold"),
    bg="AntiqueWhite2", activebackground="AntiqueWhite").place(x=230, y=220)


    janela.resizable(width=False, height=False)
    janela.title("AutoLike")

    " RESPONSIVIDADE (pirata) "
    largura, altura = (janela.winfo_screenwidth()), (janela.winfo_screenheight())
    janela.geometry(f"500x270+{int(largura/2.5)}+{int(altura/3.5)}")

    janela.protocol("WM_DELETE_WINDOW", fechar_janela)
    janela.mainloop()


if __name__ == "__main__":
    gerarInterface()
