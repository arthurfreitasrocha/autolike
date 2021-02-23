from tkinter import *

from Bot.fluxo import iniciarFluxo



def __preConfiguracao(usuario, senha):

    # Lê o diretorio raiz
    with open('Bot\\diretorio_raiz.txt', 'r') as f:
        diretorio_raiz = f.read()

    # Escreve num bloco de notas a última conta que o usuário informou
    diretorio_ultimo_usuario = f'{diretorio_raiz}\\ultimo_usuario.txt'
    with open(diretorio_ultimo_usuario, 'w') as f:
        conteudo = f'{usuario}-{senha}'
        f.write(conteudo)


def iniciarInterface(janela, usuario, senha):

    __preConfiguracao(usuario, senha)

    # CORES
    PRIMARY = "#1d3557"
    SECONDARY = "#ffffff"
    TITLE_BACKGROUND = "#15263e"
    TEXT = "#000000"
    BUTTON = "#f1faee"

    janela.destroy()
    janela = Tk()

    # Background
    background = Frame(janela)
    background["width"] = 375
    background["height"] = 560
    background["bg"] = PRIMARY
    background.pack(side=TOP)


    # Título página
    background_titulo = Frame(background)
    background_titulo["width"] = 375
    background_titulo["height"] = 100
    background_titulo["bg"] = TITLE_BACKGROUND
    background_titulo.place(x=0, y=0)

    titulo = Label(background_titulo)
    titulo["text"] = "CURTIR PUBLICAÇÕES"
    titulo["font"] = ("ADAM.CGPRO", 18)
    titulo["fg"] = SECONDARY
    titulo["bg"] = TITLE_BACKGROUND
    titulo.place(relx=0.5, rely=0.5, anchor=CENTER)


    # Formulário
    background_forms = Frame(background)
    background_forms["width"] = 268
    background_forms["height"] = 220
    background_forms["bg"] = PRIMARY
    background_forms.place(x=54, y=140)

    # Formulário -> Hashtag
    hashtag = Label(background_forms)
    hashtag["text"] = "Hashtag"
    hashtag["font"] = ("Open Sans Regular", 14)
    hashtag["fg"] = SECONDARY
    hashtag["bg"] = PRIMARY
    hashtag.place(x=0, y=0)

    hashtag_input = Entry(background_forms)
    hashtag_input["width"] = 15
    hashtag_input["bd"] = 0
    hashtag_input["font"] = ("Open Sans Regular", 12)
    hashtag_input["fg"] = TEXT
    hashtag_input["bg"] = SECONDARY
    hashtag_input.place(x=0, y=35)

    # Formulário -> Número de perfis a serem acesssados
    perfis = Label(background_forms)
    perfis["text"] = "Quant. Perfis"
    perfis["font"] = ("Open Sans Regular", 14)
    perfis["fg"] = SECONDARY
    perfis["bg"] = PRIMARY
    perfis.place(x=145, y=0)

    perfis_input = Entry(background_forms)
    perfis_input["width"] = 15
    perfis_input["bd"] = 0
    perfis_input["font"] = ("Open Sans Regular", 12)
    perfis_input["fg"] = TEXT
    perfis_input["bg"] = SECONDARY
    perfis_input.place(x=150, y=35)

    # Formulário -> Comentário
    comentario = Label(background_forms)
    comentario["text"] = "Comentário"
    comentario["font"] = ("Open Sans Regular", 14)
    comentario["fg"] = SECONDARY
    comentario["bg"] = PRIMARY
    comentario.place(x=0, y=75)

    comentario_input = Text(background_forms)
    comentario_input["width"] = 30
    comentario_input["height"] = 30
    comentario_input["bd"] = 0
    comentario_input["font"] = ("Open Sans Regular", 12)
    comentario_input["fg"] = TEXT
    comentario_input["bg"] = SECONDARY
    comentario_input.place(x=0, y=110)


    # Botão
    background_button = Frame(background)
    background_button["width"] = 268
    background_button["height"] = 30
    background_button["bg"] = PRIMARY
    background_button.place(x=54, y=400)

    button = Button(background_button)
    button["width"] = 268
    button["bd"] = 0
    button["text"] = "INICIAR"
    button["font"] = ("Open Sans Bold", 12)
    button["fg"] = PRIMARY
    button["bg"] = BUTTON
    button["cursor"] = "hand2"
    button["activeforeground"] = PRIMARY
    button["activebackground"] = BUTTON
    button["command"] = lambda:iniciarFluxo(janela, usuario, senha, hashtag_input.get(), int(perfis_input.get()), comentario_input.get("1.0", END))
    button.place(relx=0.5, rely=0.5, anchor=CENTER)


    # Rodapé
    background_footer = Frame(background)
    background_footer["width"] = 350
    background_footer["height"] = 100
    background_footer["bg"] = PRIMARY
    background_footer.place(x=14, y=480)

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
    DIMENSAO_WIDGET = [375, 560]

    # Configurações Janela -> Centralizar
    margin_left = int((DIMENSAO_MONITOR[0]/2)-(DIMENSAO_WIDGET[0]/2))
    margin_top = int((DIMENSAO_MONITOR[1]/2)-(DIMENSAO_WIDGET[1]/1.8))


    janela.geometry(f"{DIMENSAO_WIDGET[0]}x{DIMENSAO_WIDGET[1]}+{margin_left}+{margin_top}")
    janela.title("Curtir Publicações")
    janela.mainloop()
