from tkinter import *
from tkinter.ttk import *

class ProgressBar():

    def progress_bar_hashtag(self, hashtag, n_fotos_curtidas):

        pass


    def progress_bar_escolha(self, lista_usuarios, n_fotos_curtidas):

        def pb_situacao_geral(lista_usuarios):

            pass

        def pb_usuario_atual(n_fotos_curtidas):

            pass

        janela = Tk()

        # WINDOW GEOMETRY
        lado = janela.winfo_screenwidth()
        cima = janela.winfo_screenheight()
        l = int(lado)
        c = int(cima/2)
        g = '{}x{}+{}+{}'.format(300, 200, l, c) # preciso melhorar isso

        # VARIABLES
        var_usuario = 'nome_usuario'

        # USUARIO ATUAL
        # FRAME USUARIO ATUAL
        f_usuario_atual = Frame(janela, width=300, height=50)
        f_usuario_atual.pack(side=TOP)

        # LABEL USUARIO ATUAL
        l_usuario_atual = Label(f_usuario_atual, text='Usuário Atual:', font=('arial', 12))
        l_usuario_atual.place(x=20, y=20)

        # LABEL VAR USUARIO ATUAL
        l_var_usuario_atual = Label(f_usuario_atual, text=var_usuario, font=('arial', 12))
        l_var_usuario_atual.place(x=130, y=20)
        

        # PROGRESSBAR SITUATION
        # FRAME PROGRESSBAR SITUATION
        f_pb_usuario_atual = Frame(janela, width=300, height=150)
        f_pb_usuario_atual.pack(side=TOP)

        l_pb_usuario_atual = Label(f_pb_usuario_atual, text='Progresso Usuário Atual', font=('arial', 12, 'bold'))
        l_pb_usuario_atual.place(x=55, y=20)

        pb_usuario_atual = Progressbar(f_pb_usuario_atual, orient=HORIZONTAL, length=260, mode='determinate')
        pb_usuario_atual.place(x=20, y=50)

        l_pb_situacao_geral = Label(f_pb_usuario_atual, text='Progresso Geral', font=('arial', 12, 'bold'))
        l_pb_situacao_geral.place(x=85, y=80)

        pb_situacao_geral = Progressbar(f_pb_usuario_atual, orient=HORIZONTAL, length=260, mode='determinate')
        pb_situacao_geral.place(x=20, y=110)


        #pb_situacao_geral(lista_usuarios)
        #pb_usuario_atual(n_fotos_curtidas)


        # WINDOW CONFIGURATION
        janela.resizable(width=False, height=False)
        janela.title('AutoLike 3.0 - Progresso Atual')
        janela.geometry(g)
        janela.mainloop()
        

    def __init__(self, metodo, hashtag, lista_usuarios, n_fotos_curtidas):

        if metodo == 0:

            self.progress_bar_hashtag(hashtag, n_fotos_curtidas)

        elif metodo == 1:

            self.progress_bar_escolha(lista_usuarios, n_fotos_curtidas)


a = ProgressBar(1, '#teste', 5, 2)