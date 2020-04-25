# TKINTER LIBRAY
from tkinter import *


class CurtirFotosEscolhaBancoDeDadosAbrirMiniBD():

    def retorno(self):
        
        # THIS FUNCTION RETURNS THE INFORMATION STORED IN THE FILE BELOW
        file = open('informacoes.txt', 'r')
        conteudo_file = file.read()
        file.close()

        conteudo = conteudo_file.split('-')

        lista = []
        lista.append(conteudo[0], conteudo[1], conteudo[2])

        return lista

    
    def __init__(self, email_curto):

        def confirmacao(janela, valor, conteudo, email_curto, lbox):
            
            # THIS FUNCTION WRITE THE RETURN OF THE PROCESS IN THE FILE BELOW
            temp = lbox.curselection()
            n_usuarios = len(temp)

            i = 0
            cont = 0
            while(i < len(temp)):

                if i == 0:

                    file = open('curtir_fotos_usuarios.txt', 'w')
                    file.write(conteudo[temp[i]])
                    file.close()

                    cont += 1

                else:

                    file = open('curtir_fotos_usuarios.txt', 'a')
                    file.write('-{}'.format(conteudo[temp[i]]))
                    file.close()

                    cont += 1

                i += 1

            janela.destroy()
            self.retorno()

            file = open('informacoes.txt', 'w')
            file.write('{}-{}-{}'.format(email_curto, 1, n_usuarios))
            file.close()



        janela = Toplevel()
        
        # WINDOW GEOMETRY
        lado = janela.winfo_screenwidth()
        cima = janela.winfo_screenheight()
        l = int(lado/3)
        c = int(cima/5)
        g = '{}x{}+{}+{}'.format(500, 510, l, c)

        # VARIABLES
        checkvar = IntVar()

        # ADDITIONAL CONFIGURATION
        txt = 'bd_{}.txt'.format(email_curto)

        file = open(txt, 'r')
        conteudo_file = file.read()
        file.close()

        conteudo = conteudo_file.split('\n')


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
        f_selecionar_usuarios_label = Frame(f_raiz, width=500, height=80, bg='floral white')
        f_selecionar_usuarios_label.pack(side=TOP)

        # LABEL SELECT USERS 01
        l_selecionar_usuarios = Label(f_selecionar_usuarios_label, text='Selecione os usuários que o\nprograma irá curtir as fotos',
        font=('arial', 15, 'bold'), bg='floral white')
        l_selecionar_usuarios.place(x=110, y=15)

        # FRAME SELECT USERS 02
        f_selecionar_usuarios = Frame(f_raiz, width=500, height=300, bg='floral white')
        f_selecionar_usuarios.pack(side=TOP)

        # SCROLLBAR SELECT USERS 02
        sb_selecionar_usuarios = Scrollbar(f_selecionar_usuarios, width=20)
        sb_selecionar_usuarios.pack(side=RIGHT, fill=Y)

        # LISTBOX SELECT USERS 02
        lbox_selecionar_usuarios = Listbox(f_selecionar_usuarios, font=('arial', 15, 'bold'),
        width=50, yscrollcommand=sb_selecionar_usuarios.set,
        selectmode=MULTIPLE)

        i = 0
        while(i < len(conteudo)-1):
            
            lbox_selecionar_usuarios.insert(i, '{} - {}'.format(i+1, conteudo[i]))

            i += 1

        lbox_selecionar_usuarios.pack(side=LEFT)
        sb_selecionar_usuarios.config(command=lbox_selecionar_usuarios.yview)

        # FRAME SELECT USERS 03
        f_selecionar_usuarios_button = Frame(f_raiz, width=500, height=110, bg='floral white')
        f_selecionar_usuarios_button.pack(side=TOP)

        # CHECKBUTTON SELECT USERS 03
        cbutton = Checkbutton(f_selecionar_usuarios_button, text='Selecionar todos', font=('arial', 15, 'bold'),
        bg='dark salmon',
        activebackground='salmon', activeforeground='white',
        variable=checkvar, onvalue=1, offvalue=0)
        cbutton.place(x=80, y=25)

        # BUTTON SELECT USERS 03
        b_selecionar_usuarios = Button(f_selecionar_usuarios_button, text='ENVIAR', font=('arial', 15, 'bold'),
        bg='dark salmon',
        activebackground='salmon', activeforeground='white',
        command=lambda: confirmacao(janela, checkvar.get(), conteudo, email_curto, lbox_selecionar_usuarios))
        b_selecionar_usuarios.place(x=300, y=20)

        # WINDOW CONFIGURATION
        janela.resizable(width=False, height=False)
        janela.title('AutoLike 3.0 - Curtir Fotos De Um Perfil Específico - Banco de Dados')
        janela.geometry(g)
        janela.mainloop()