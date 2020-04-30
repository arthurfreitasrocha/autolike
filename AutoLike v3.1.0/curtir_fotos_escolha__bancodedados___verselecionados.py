from tkinter import *

class CurtirFotosEscolhaBancoDeDadosVerSelecionados:

    def __init__(self):

        def voltar():
            
            janela.destroy()


        janela = Tk()
        
        # WINDOW GEOMETRY
        lado = janela.winfo_screenwidth()
        cima = janela.winfo_screenheight()
        l = int(lado/3)
        c = int(cima/4)
        g = '{}x{}+{}+{}'.format(500, 320, l, c)

        # ADDITIONAL CONFIGURATION
        file = open('app_version.txt', 'r')
        app_version = file.read()
        file.close()

        file = open('curtir_fotos_usuarios.txt', 'r')
        conteudo_file = file.read()
        file.close()

        conteudo = conteudo_file.split('-')

        lista = conteudo
        valor_conteudo = len(conteudo)
        i = 0
        while(i < valor_conteudo):

            if conteudo[i] == '':

                lista.pop(i)

            i += 1

        conteudo = lista


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

        # SELECT USERS
        # FRAME SELECT USERS 01
        f_selecionar_usuarios = Frame(f_raiz, width=500, height=150, bg='floral white')
        f_selecionar_usuarios.pack(side=TOP)

        # SCROLLBAR SELECT USERS 01
        sb_selecionar_usuarios = Scrollbar(f_selecionar_usuarios, width=20)
        sb_selecionar_usuarios.pack(side=RIGHT, fill=Y)

        # LISTBOX SELECT USERS 01
        lbox_selecionar_usuarios = Listbox(f_selecionar_usuarios, font=('arial', 15, 'bold'),
        width=50, height=5,
        yscrollcommand=sb_selecionar_usuarios.set, selectmode=SINGLE)

        i = 0
        while(i < len(conteudo)):
            
            lbox_selecionar_usuarios.insert(i, '{} - {}'.format(i+1, conteudo[i]))

            i += 1

        lbox_selecionar_usuarios.pack(side=LEFT)
        sb_selecionar_usuarios.config(command=lbox_selecionar_usuarios.yview)

        # FRAME SELECT USERS 02
        f_selecionar_usuarios_button = Frame(f_raiz, width=500, height=90, bg='floral white')
        f_selecionar_usuarios_button.pack(side=TOP)

        # BUTTON SELECT USERS 02
        b_selecionar_usuarios = Button(f_selecionar_usuarios_button, text='<- Voltar', font=('arial', 15, 'bold'),
        bg='dark salmon',
        activebackground='salmon', activeforeground='white',
        command=voltar)
        b_selecionar_usuarios.place(x=200, y=20)

        # WINDOW CONFIGURATION
        janela.resizable(width=False, height=False)
        janela.title('AutoLike {} - Curtir Fotos De Perfil Específico - Banco de Dados'.format(app_version))
        janela.geometry(g)
        janela.mainloop()
