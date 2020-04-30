from tkinter import *
from tkinter import messagebox

class CurtirFotosEscolhaBancoDeDadosMetodoCurtidas:

    # THIS FUNCTION RETURNS THE USER CHOICE
    def retorno(self):

        file = open('informacoes.txt', 'r')
        conteudo = file.read()
        file.close()

        return conteudo


    # THIS METHOD SHOW A MESSAGE INFORMING THE USER ABOUT HIM CHOICE 
    def opcao_escolhida(self, janela, valor):

        valor = int(valor)

        if valor == 1:
            
            file = open('informacoes.txt', 'w')
            file.write('1')
            file.close()

            messagebox.showinfo('Sucesso', 'Você selecionou a opção Curtidas em Sequência.')

        else:

            file = open('informacoes.txt', 'w')
            file.write('2')
            file.close()

            messagebox.showinfo('Sucesso', 'Você selecionou a opção Curtidas Aleatórias.')

    
    # THIS METHOD SHOW THE GRAPHICAL INTERFACE OF THE PROGRAM
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

        # VARIABLES
        valor_cb = IntVar()

        # ROOT ====================
        # FRAME ROOT PROGRAM
        f_raiz = Frame(janela, width=500, height=330)
        f_raiz.pack(side=TOP)

        # FRAME LOGO PROGRAM
        f_logo = Frame(f_raiz, width=500, height=100)
        f_logo.pack(side=TOP)

        logo_programa = PhotoImage(file='logo.png')

        # LABEL LOGO PROGRAM
        l_logo = Label(f_raiz, image=logo_programa)
        l_logo.place(x=0, y=0)


        # LIKE OPTIONS
        # FRAME LIKE OPTIONS
        f_opcoes_curtir = Frame(f_raiz, width=500, height=100, bg='floral white')
        f_opcoes_curtir.pack(side=TOP)

        rb_curtidas_sequencia = Radiobutton(f_opcoes_curtir, text='Curtidas em Sequência',
        font=('arial', 12, 'bold'), bg='floral white',
        variable=valor_cb, value=1)
        rb_curtidas_sequencia.place(x=20, y=20)

        rb_curtidas_aleatorias = Radiobutton(f_opcoes_curtir, text='Curtidas Aleatórias',
        font=('arial', 12, 'bold'), bg='floral white',
        variable=valor_cb, value=1)
        rb_curtidas_aleatorias.place(x=100, y=20)

        b_opcoes_curtidas = Button(f_opcoes_curtir, text='ENVIAR', font=('arial', 15, 'bold'),
        bg='dark salmon',
        activebackground='salmon', activeforeground='white',
        command=lambda: self.opcao_escolhida(janela, valor_cb.get()))
        b_opcoes_curtidas.place(x=150, y=50)

        # WINDOW CONFIGURATION
        janela.resizable(width=False, height=False)
        janela.title('AutoLike {} - Curtir Fotos De Perfil Específico - Banco de Dados'.format(app_version))
        janela.geometry(g)
        janela.mainloop()


    # CONSTRUCTOR METHOD
    def __init__(self):

        pass

a = CurtirFotosEscolhaBancoDeDadosMetodoCurtidas()
a.interface()