from tkinter import *
import os


def gerarInterface():

    """
    INFORMAÇÕES NECESSÁRIAS
    """
    diretorio_atual = os.getcwd()

    with open(f"{diretorio_atual}\\AutoLike_4.2\\model\\system_files\\user_instagram.txt") as file:
        usuario = file.read()


    janela = Tk()


    " IMAGEM "
    logo = PhotoImage(file=f"{diretorio_atual}\\AutoLike_4.2\\view\\images\\logo.png")

    frame_imagem = Frame(janela, width=900, height=100, bg="Salmon").pack(side=TOP)
    Label(frame_imagem, image=logo, bg="salmon").place(x=400, y=15)


    " EMAIL "
    imagem_editar = PhotoImage(file=f"{diretorio_atual}\\AutoLike_4.2\\view\\images\\lapis.png")

    frame_email = Frame(janela, width=900, height=100, bg="Peach Puff").pack(side=TOP)
    Label(frame_email, text="E-mail atual", font=("arial", 13, "bold"), bg="Peach Puff").place(x=20, y=120)
    entry_email = Entry(frame_email, font=("arial", 12), width=88)
    entry_email.insert(0, usuario)
    entry_email.place(x=20, y=160)
    Button(frame_email, image=imagem_editar, bg="AntiqueWhite2", activebackground="AntiqueWhite", command=lambda: __gerarInterfaceLogin(janela)).place(x=840, y=150)


    " OPÇÕES "
    frame_opcoes = Frame(janela, width=900, height=130, bg="Peach Puff").pack(side=TOP)

    Label(frame_opcoes, text="Selecione uma opção", font=("arial", 13, "bold"), bg="Peach Puff").place(x=370, y=230)
    list_opcoes = Listbox(frame_opcoes, width=30, height=2, font=("arial", 10), justify=CENTER, selectmode=SINGLE)
    list_opcoes.insert(1, "Curtir fotos com Hashtag")
    list_opcoes.insert(2, "Curtir fotos com Banco de Dados")
    list_opcoes.place(x=350, y=270)


    " BOTÃO ENVIAR "
    frame_enviar = Frame(janela, width=900, height=70, bg="Peach Puff").pack(side=TOP)

    Button(frame_enviar, text="Selecionar", font=("arial", 11, "bold"),
    bg="AntiqueWhite2", activebackground="AntiqueWhite").place(x=410, y=340)


    janela.resizable(width=False, height=False)
    janela.title("AutoLike")

    " RESPONSIVIDADE (pirata) "
    largura, altura = (janela.winfo_screenwidth()), (janela.winfo_screenheight())
    janela.geometry(f"900x400+{int(largura/3.5)}+{int(altura/4.5)}")

    janela.mainloop()


def __gerarInterfaceLogin(janela):

    janela.destroy()
    
    """
    INFORMAÇÕES NECESSÁRIAS
    """
    diretorio_atual = os.getcwd()


    top = Tk()

    def on_closing():
        top.destroy()
        __gerarInterface()


    " IMAGEM "
    logo = PhotoImage(file=f"{diretorio_atual}\\AutoLike_4.2\\view\\images\\logo.png")

    frame_imagem = Frame(top, width=500, height=100, bg="Salmon").pack(side=TOP)
    Label(frame_imagem, image=logo, bg="salmon").place(x=210, y=15)


    " LOGIN E SENHA "
    frame_login_senha = Frame(top, width=500, height=100, bg="Peach Puff").pack(side=TOP)

    Label(frame_login_senha, text="Login", font=("arial", 13, "bold"), bg="Peach Puff").place(x=30, y=130)
    entry_login = Entry(frame_login_senha, font=("arial", 12), width=40).place(x=90, y=130)

    Label(frame_login_senha, text="Senha", font=("arial", 13, "bold"), bg="Peach Puff").place(x=30, y=170)
    entry_senha = Entry(frame_login_senha, font=("arial", 12), width=40).place(x=90, y=170)


    " BOTÃO ENVIAR "
    frame_enviar = Frame(top, width=900, height=70, bg="Peach Puff").pack(side=TOP)

    Button(frame_enviar, text="Enviar", font=("arial", 11, "bold"),
    bg="AntiqueWhite2", activebackground="AntiqueWhite").place(x=230, y=220)


    top.resizable(width=False, height=False)
    top.title("AutoLike")

    " RESPONSIVIDADE (pirata) "
    largura, altura = (top.winfo_screenwidth()), (top.winfo_screenheight())
    top.geometry(f"500x270+{int(largura/2.5)}+{int(altura/3.5)}")

    top.protocol("WM_DELETE_WINDOW", on_closing)
    top.mainloop()



if __name__ == "__main__":
    gerarInterface()
