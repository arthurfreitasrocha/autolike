from tkinter import *
import os
from tkinter import font


def __gerarInterface():

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
    entry_email = Entry(frame_email, font=("arial", 12), width=88, state=NORMAL)
    entry_email.insert(0, usuario)
    entry_email.place(x=20, y=160)
    Button(frame_email, image=imagem_editar, bg="AntiqueWhite2", activebackground="AntiqueWhite").place(x=840, y=150)


    " OPÇÕES "
    frame_opcoes = Frame(janela, width=900, height=130, bg="Peach Puff").pack(side=TOP)

    Label(frame_opcoes, text="Selecione uma opção", font=("arial", 13, "bold"), bg="Peach Puff").place(x=370, y=230)
    list_opcoes = Listbox(frame_opcoes, width=30, height=2, font=("arial", 10), justify=CENTER, selectmode=SINGLE)
    list_opcoes.insert(1, "Curtir fotos com Hashtag")
    list_opcoes.insert(2, "Curtir fotos com Banco de Dados")
    list_opcoes.place(x=350, y=270)


    " BOTÃO ENVIAR "
    frame_enviar = Frame(janela, width=900, height=70, bg="Peach Puff").pack(side=TOP)

    Button(frame_email, text="Selecionar", font=("arial", 11, "bold"), bg="AntiqueWhite2", activebackground="AntiqueWhite").place(x=410, y=340)


    janela.resizable(width=False, height=False)
    janela.title("AutoLike")

    " RESPONSIVIDADE (pirata) "
    largura, altura = (janela.winfo_screenwidth()), (janela.winfo_screenheight())
    janela.geometry(f"900x400+{int(largura/3.5)}+{int(altura/4.5)}")

    janela.mainloop()



def iniciar():

    janela = __gerarInterface()




if __name__ == "__main__":
    iniciar()
