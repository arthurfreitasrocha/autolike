import curtir

from tkinter import *
from os import getcwd



def __preConfiguracao():

    # Escrevendo o diretório raiz do programa num bloco de notas
    diretorio_raiz = getcwd()

    with open('Bot\\diretorio_raiz.txt', 'w') as f:
        f.write(diretorio_raiz)


    # Tenta abrir o arquivo contendo as informações do último usuário logado
    try:
        diretorio_ultimo_usuario = f'{diretorio_raiz}\\ultimo_usuario.txt'
        with open(diretorio_ultimo_usuario, 'r') as f:
            conteudo = f.read()

        conteudo_splitted = conteudo.split('-')
        return conteudo_splitted

    except:
        return ['', '']


def iniciarInterface():

    ultimo_usuario = __preConfiguracao()
    USUARIO = ultimo_usuario[0]
    SENHA = ultimo_usuario[1]

    # CORES
    PRIMARY = "#1d3557"
    SECONDARY = "#ffffff"
    TITLE_BACKGROUND = "#15263e"
    TEXT = "#000000"
    BUTTON = "#f1faee"


    janela = Tk()

    # Background
    background = Frame(janela)
    background["width"] = 375
    background["height"] = 500
    background["bg"] = PRIMARY
    background.pack(side=TOP)


    # Título página
    background_titulo = Frame(background)
    background_titulo["width"] = 375
    background_titulo["height"] = 100
    background_titulo["bg"] = TITLE_BACKGROUND
    background_titulo.place(x=0, y=0)

    titulo = Label(background_titulo)
    titulo["text"] = "LOGIN NO INSTAGRAM"
    titulo["font"] = ("ADAM.CGPRO", 18)
    titulo["fg"] = SECONDARY
    titulo["bg"] = TITLE_BACKGROUND
    titulo.place(relx=0.5, rely=0.5, anchor=CENTER)


    # Formulário
    background_forms = Frame(background)
    background_forms["width"] = 268
    background_forms["height"] = 135
    background_forms["bg"] = PRIMARY
    background_forms.place(x=54, y=140)

    # Formulário -> Usuário
    usuario = Label(background_forms)
    usuario["text"] = "Usuário"
    usuario["font"] = ("Open Sans Regular", 14)
    usuario["fg"] = SECONDARY
    usuario["bg"] = PRIMARY
    usuario.place(x=0, y=0)

    usuario_input = Entry(background_forms)
    usuario_input["width"] = 30
    usuario_input["bd"] = 0
    usuario_input["font"] = ("Open Sans Regular", 12)
    usuario_input["fg"] = TEXT
    usuario_input["bg"] = SECONDARY
    usuario_input.insert(0, USUARIO)
    usuario_input.place(x=0, y=35)

    # Formulário -> Senha
    senha = Label(background_forms)
    senha["text"] = "Senha"
    senha["font"] = ("Open Sans Regular", 14)
    senha["fg"] = SECONDARY
    senha["bg"] = PRIMARY
    senha.place(x=0, y=75)

    senha_input = Entry(background_forms)
    senha_input["width"] = 30
    senha_input["bd"] = 0
    senha_input["font"] = ("Open Sans Regular", 12)
    senha_input["fg"] = TEXT
    senha_input["bg"] = SECONDARY
    senha_input.insert(0, SENHA)
    senha_input.place(x=0, y=110)


    # Botão
    background_button = Frame(background)
    background_button["width"] = 268
    background_button["height"] = 30
    background_button["bg"] = PRIMARY
    background_button.place(x=54, y=320)

    button = Button(background_button)
    button["width"] = 268
    button["bd"] = 0
    button["text"] = "FAZER LOGIN"
    button["font"] = ("Open Sans Bold", 12)
    button["fg"] = PRIMARY
    button["bg"] = BUTTON
    button["cursor"] = "hand2"
    button["activeforeground"] = PRIMARY
    button["activebackground"] = BUTTON
    button["command"] = lambda:curtir.iniciarInterface(janela, usuario_input.get(), senha_input.get())
    button.place(relx=0.5, rely=0.5, anchor=CENTER)


    # Rodapé
    background_footer = Frame(background)
    background_footer["width"] = 350
    background_footer["height"] = 100
    background_footer["bg"] = PRIMARY
    background_footer.place(x=14, y=400)

    background_line = Frame(background_footer)
    background_line["width"] = 350
    background_line["height"] = 10
    background_line["bg"] = PRIMARY
    background_line.pack(side=TOP)

    linha = Frame(background_line)
    linha["width"] = 350
    linha["height"] = 1
    linha["bg"] = SECONDARY
    linha.place(x=0, y=0)

    # Rodapé -> AutoLike
    background_autolike = Frame(background_footer)
    background_autolike["width"] = 350
    background_autolike["height"] = 23
    background_autolike["bg"] = PRIMARY
    background_autolike.pack(side=TOP)

    autolike_version = Label(background_autolike)
    autolike_version["text"] = "AutoLike v5.0"
    autolike_version["font"] = ("Open Sans Regular", 10)
    autolike_version["fg"] = SECONDARY
    autolike_version["bg"] = PRIMARY
    autolike_version.place(relx=0.5, rely=0.5, anchor=CENTER)

    # Rodapé -> Copyright
    background_copyright = Frame(background_footer)
    background_copyright["width"] = 350
    background_copyright["height"] = 25
    background_copyright["bg"] = PRIMARY
    background_copyright.pack(side=TOP)

    name_copyright = Label(background_copyright)
    name_copyright["text"] = "© Arthur Freitas Rocha. Todos os direitos reservados."
    name_copyright["font"] = ("Open Sans Regular", 10)
    name_copyright["fg"] = SECONDARY
    name_copyright["bg"] = PRIMARY
    name_copyright.place(relx=0.5, rely=0.5, anchor=CENTER)


    # Configurações Janela
    DIMENSAO_MONITOR = [janela.winfo_screenwidth(), janela.winfo_screenheight()]
    DIMENSAO_WIDGET = [375, 480]

    # Configurações Janela -> Centralizar
    margin_left = int((DIMENSAO_MONITOR[0]/2)-(DIMENSAO_WIDGET[0]/2))
    margin_top = int((DIMENSAO_MONITOR[1]/2)-(DIMENSAO_WIDGET[1]/1.8))

    #  Configurações Janela -> Aplicar
    janela.geometry(f"{DIMENSAO_WIDGET[0]}x{DIMENSAO_WIDGET[1]}+{margin_left}+{margin_top}")
    janela.title("Login")
    janela.mainloop()



iniciarInterface()