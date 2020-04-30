from tkinter import *

class CurtirFotosEscolhaBancoDeDadosMetodoCurtidas:

    def interface(self):

        janela = Tk()

        # WINDOW GEOMETRY
        lado = janela.winfo_screenwidth()
        cima = janela.winfo_screenheight()
        l = int(lado/3)
        c = int(cima/5)
        g = '{}x{}+{}+{}'.format(500, 400, l, c)

        # ADDITIONAL CONFIGURATION
        file = open('app_version.txt', 'r')
        app_version = file.read()
        file.close()


        # WINDOW CONFIGURATION
        janela.resizable(width=False, height=False)
        janela.title('AutoLike {} - Curtir Fotos De Perfil Específico - Banco de Dados'.format(app_version))
        janela.geometry(g)
        janela.mainloop()

    def __init__(self):

        pass