# TKINTER LIBRARY
from tkinter import *
from tkinter import messagebox

# CUSTOM LIBRARY'S
from curtir_fotos_hashtag import CurtirFotosHashtag
from curtir_fotos_escolha import CurtirFotosEscolha
from curtir_fotos_msg_direct import CurtirFotosMsgDirect
from mudar_email_instagram import MudarEmailInstagram

class Start():

    def __init__(self):

        def mudar_email_instagram():
            
            janela.destroy()
            a = MudarEmailInstagram()
            a = Start()


        def escolha(opcao):

            def curtir_fotos_hashtag():
            
                janela.destroy()
                a = CurtirFotosHashtag()
                a = Start()

            def curtir_fotos_escolha():
                
                janela.destroy()
                a = CurtirFotosEscolha() # CASO NAO HAJA BD PRONTO O 'curtir_fotos_escolha.py' DEVE RETORNAR 1
                resp = a.retornar()

                if resp == 1:
                    resp = Start()

            def curtir_fotos_msg_direct():
                
                messagebox.showinfo('Ainda em manutenção', 'Opção ainda não programada')
                #janela.destroy()
                #a = CurtirFotosMsgDirect()
                #a = Start()

            if opcao == 0:

                curtir_fotos_hashtag()

            elif opcao == 1:

                curtir_fotos_escolha()

            else:

                curtir_fotos_msg_direct()



        janela = Tk()

        # WINDOW GEOMETRY
        lado = janela.winfo_screenwidth()
        cima = janela.winfo_screenheight()
        l = int(lado/3)
        c = int(cima/13)
        g = '{}x{}+{}+{}'.format(500, 570, l, c)

        # ADDITIONAL INFORMATION
        conteudo = ''
        erro = 0

        try:

            file = open('email_senha_instagram.txt', 'r')
            conteudo_file = file.read()
            file.close()

            conteudo = conteudo_file.split('-')

            if conteudo[0] == '':
                conteudo[0] = 'Email ainda não cadastrado'
                erro = 1

        except:

            conteudo = ['Email ainda não cadastrado']
            erro = 1

        email = conteudo[0]

        # VARIABLES
        opcao = IntVar()


        # ROOT PROGRAM ====================
        # FRAME ROOT PROGRAM
        f_raiz = Frame(janela, width=500, height=330, bg='dark salmon')
        f_raiz.pack(side=TOP)

        # FRAME LOGO PROGRAM
        f_logo = Frame(f_raiz, width=500, height=100)
        f_logo.pack(side=TOP)

        logo_programa = PhotoImage(file='logo.png')

        l_logo = Label(f_raiz, image=logo_programa)
        l_logo.place(x=0, y=0)

        # USER INFORMATION ====================
        # FRAME USER INFORMATION
        f_info_usuario = Frame(f_raiz, width=500, height=150, bg='floral white')
        f_info_usuario.pack(side=TOP)

        if erro == 0:
            l_email = Label(f_info_usuario, text='Email: {}'.format(email),
            font=('arial', 15, 'bold'), bg='floral white')
            l_email.place(x=50, y=20)

            b_email = Button(f_info_usuario, text='Alterar Email Instagram',
            font=('arial', 15,'bold'), bg='dark salmon',
            activebackground='salmon', activeforeground='white',
            command=mudar_email_instagram)
            b_email.place(x=130, y=80)

        else:
            l_email = Label(f_info_usuario, text=email,
            font=('arial', 15, 'bold'), bg='floral white')
            l_email.place(x=110, y=20)

            b_email = Button(f_info_usuario, text='Cadastrar Email Instagram',
            font=('arial', 15,'bold'), bg='dark salmon',
            activebackground='salmon', activeforeground='white',
            command=mudar_email_instagram)
            b_email.place(x=110, y=80)

        # DIVIDER ====================
        # FRAME DIVIDER
        f_divider = Frame(f_raiz, width=500, height=10, bg='dark salmon')
        f_divider.pack(side=TOP)

        # OPTIONS ====================
        # FRAME OPTIONS
        f_opcoes = Frame(f_raiz, width=500, height=310, bg='floral white')
        f_opcoes.pack(side=TOP)

        # LABELFRAME OPTIONS
        l_opcoes = Label(f_opcoes, text='Opções do Usuário',
        font=('arial', 15,'bold'), bg='floral white')
        l_opcoes.place(x=150, y=20)

        # RADIOBUTTONS OPTIONS
        r_curtir_fotos_hashtag = Radiobutton(f_opcoes,
        text='Curtir Fotos usando uma Hashtag', font=('arial', 15,'bold'), bg='dark salmon',
        activebackground='salmon', activeforeground='white',
        variable=opcao, value=0)
        r_curtir_fotos_hashtag.place(x=80, y=80)

        r_curtir_fotos_escolha = Radiobutton(f_opcoes,
        text='Curtir Fotos de um perfil Específico', font=('arial', 15,'bold'), bg='dark salmon',
        activebackground='salmon', activeforeground='white',
        variable=opcao, value=1)
        r_curtir_fotos_escolha.place(x=70, y=130)

        r_curtir_fotos_msg_direct = Radiobutton(f_opcoes,
        text='Curtir Fotos e Enviar Mensagem no Direct', font=('arial', 15,'bold'), bg='dark salmon',
        activebackground='salmon', activeforeground='white',
        variable=opcao, value=2)
        r_curtir_fotos_msg_direct.place(x=40, y=180)

        # BUTTON OPTIONS
        b_options = Button(f_opcoes, text='SELECIONAR', font=('arial', 15, 'bold'), bg='dark salmon',
        activebackground='salmon', activeforeground='white',
        command=lambda: escolha(opcao.get()))
        b_options.place(x=180, y=250)

        janela.resizable(width=False, height=False)
        janela.title('AutoLike 3.0')
        janela.geometry(g)
        janela.mainloop()

a = Start()
