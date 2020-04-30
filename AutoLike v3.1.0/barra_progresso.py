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
        l = int(lado/3)
        c = int(cima/8)
        g = '{}x{}+{}+{}'.format(300, 200, l, c)

        var_usuario = 1
        l_usuario_atual = Label(janela, text='Usuário Atual:', font=('arial', 12))
        l_usuario_atual.grid(row=0, column=0)

        l_var_usuario_atual = Label(janela, text=var_usuario, font=('arial', 12))
        l_var_usuario_atual.grid(row=0, column=1)
        
        # PROGRESSBAR SITUATION
        l_pb_usuario_atual = Label(janela, text='Progresso Usuário Atual', font=('arial', 12, 'bold'))
        l_pb_usuario_atual.grid(row=1)

        pb_usuario_atual = Progressbar(janela, orient=HORIZONTAL, length=200, mode='determinate')
        pb_usuario_atual.grid(row=2)

        l_pb_situacao_geral = Label(janela, text='Progresso Geral', font=('arial', 12, 'bold'))
        l_pb_situacao_geral.grid(row=3)

        pb_situacao_geral = Progressbar(janela, orient=HORIZONTAL, length=200, mode='determinate')
        pb_situacao_geral.grid(row=4)


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