# TKINTER LIBRARY
from tkinter import *
from tkinter import messagebox

# CUSTOM LIBRARY'S
from curtir_fotos_escolha__bancodedados import CurtirFotosEscolhaBancoDeDados

class CurtirFotosEscolha():

    def retornar(self):

        return 1


    def mini_bd(self, janela):
        
        # TAKING THE NAME_USER OF THE BD
        file = open('email_senha_instagram.txt', 'r')
        conteudo_file = file.read()
        file.close()

        conteudo = conteudo_file.split('-')
        email = conteudo[0]

        i = 0
        email_curto = ''
        while(i < len(email)):
            if email[i] != '@':
                email_curto += email[i]
                                
            else:
                i = len(email)

            i += 1

        erro = 0

        try:
            
            txt = 'bd_{}.txt'.format(email_curto)

            file = open(txt, 'r')
            conteudo_file = file.read()
            file.close()

            if conteudo_file == '':

                erro = 1

        except:

            erro = 1


        if erro == 1:

            messagebox.showinfo('Banco de Dados não encontrado', 'Banco de Dados (BD) ainda não criado.\nPara dar inicio ao seu BD selecione a opção "Curtir Fotos usando uma Hashtag"')

            janela.destroy()
            self.retornar()

        else:

            janela.destroy()
            a = CurtirFotosEscolhaBancoDeDados(email_curto, 0, 0)
            a = CurtirFotosEscolha()


    def escolha(self, janela):

        messagebox.showinfo('Ainda em manutenção', 'Opção ainda não programada')

        janela.destroy()


    def __init__(self):

        janela = Tk()

        # WINDOW GEOMETRY
        lado = janela.winfo_screenwidth()
        cima = janela.winfo_screenheight()
        l = int(lado/3)
        c = int(cima/5)
        g = '{}x{}+{}+{}'.format(500, 280, l, c)

        # ROOT ====================
        # FRAME ROOT PROGRAM
        f_raiz = Frame(janela, width=500, height=330)
        f_raiz.pack(side=TOP)

        # FRAME LOGO PROGRAM
        f_logo = Frame(f_raiz, width=500, height=100)
        f_logo.pack(side=TOP)

        logo_programa = PhotoImage(file='logo.png')

        l_logo = Label(f_raiz, image=logo_programa)
        l_logo.place(x=0, y=0)


        # OPTIONS ====================
        # FRAME OPTIONS
        f_opcoes = Frame(f_raiz, width=500, height=230, bg='floral white')
        f_opcoes.pack(side=TOP)

        # BUTTONS OPTIONS
        b_escolher_usuario_bd = Button(f_opcoes,
        text='Escolher Usuário do Banco de Dados', font=('arial', 15,'bold'), bg='dark salmon',
        activebackground='salmon', activeforeground='white',
        command=lambda: self.mini_bd(janela))
        b_escolher_usuario_bd.place(x=65, y=100)

        b_informar_usuario = Button(f_opcoes,
        text='Informar Usuário', font=('arial', 15,'bold'), bg='dark salmon',
        activebackground='salmon', activeforeground='white',
        command=lambda: self.escolha(janela))
        b_informar_usuario.place(x=160, y=30)

        janela.resizable(width=False, height=False)
        janela.title('AutoLike 3.0 - Curtir Fotos De Um Perfil Específico')
        janela.geometry(g)
        janela.mainloop()

#a = CurtirFotosEscolha()
