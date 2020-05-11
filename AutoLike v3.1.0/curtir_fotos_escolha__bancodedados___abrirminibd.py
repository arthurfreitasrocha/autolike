# TKINTER LIBRAY
from tkinter import *
from tkinter import messagebox

class CurtirFotosEscolhaBancoDeDadosAbrirMiniBD():

    def retorno(self):
        
        # THIS FUNCTION RETURNS THE INFORMATION STORED IN THE FILE BELOW
        file = open('informacoes.txt', 'r')
        conteudo_file = file.read()
        file.close()

        conteudo = conteudo_file.split('-')

        lista = []
        lista.append(conteudo[0])
        lista.append(conteudo[1])
        lista.append(conteudo[2])
        lista.append(conteudo[3])
        lista.append(conteudo[4])

        return lista

    
    def confirmacao(self, janela, top, valor, conteudo, email_curto, lbox, inter_inicial, inter_final, valor_intervalo):
            
        # THIS FUNCTION WRITE THE RETURN OF THE PROCESS IN THE FILE BELOW
        var_controle = 0
        if valor == 1:
                
            i = 0
            temp = []
            while(i < len(conteudo)):
 
                temp.append(i)
                n_usuarios = len(temp)-1

                i += 1

            var_controle = 1
            
        else:

            temp = lbox.curselection()
            n_usuarios = len(temp)


        i = 0
        while(i < len(temp)-var_controle):

            if i == 0:

                file = open('curtir_fotos_usuarios.txt', 'w')
                file.write(conteudo[temp[i]])
                file.close()

            else:

                file = open('curtir_fotos_usuarios.txt', 'a')
                file.write('-{}'.format(conteudo[temp[i]]))
                file.close()

            i += 1



        if valor_intervalo == 1:

            if inter_inicial.isnumeric() == False or inter_final.isnumeric() == False:

                messagebox.showwarning('Um ou mais valores inválidos', 'Os valores informados são inválidos.')

                top.destroy()

            else:

                inter_inicial = int(inter_inicial)
                inter_final = int(inter_final)

                if (inter_inicial < 0 or inter_final < 0) or (inter_final > len(conteudo)):

                    messagebox.showwarning('Um ou mais valores inválidos', 'Os valores informados são inválidos.')

                    top.destroy()

                else:

                    intervalo = [int(inter_inicial), int(inter_final)]

                    file = open('informacoes.txt', 'w')
                    file.write('{}-{}'.format(intervalo[0], intervalo[1]))
                    file.close()
                    
                    messagebox.showinfo('Sucesso', 'Intervalo selecionado com sucesso')

                    top.destroy()
                    janela.destroy()

                    a = CurtirFotosEscolhaBancoDeDadosAbrirMiniBD()
                    a.interface(email_curto)


        if valor_intervalo == 0:

            file = open('informacoes.txt', 'w')
            file.write('{}-{}-{}-{}-{}'.format(email_curto, 1, n_usuarios, 0, 0))
            file.close()

            messagebox.showinfo('Sucesso', 'Lista de usuários selecionados atualizada com sucesso!')
            janela.destroy()
            
            self.retorno()

    
    def intervalo_func(self, janela, checkvar, conteudo, email_curto, lbox_selecionar_usuarios, app_version):

        top = Toplevel()

        # WINDOW GEOMETRY
        lado = top.winfo_screenwidth()
        cima = top.winfo_screenheight()
        l = int(lado/3)
        c = int(cima/4)
        g = '{}x{}+{}+{}'.format(500, 340, l, c)

        # ROOT ====================
        # FRAME ROOT PROGRAM
        f_raiz = Frame(top, width=500, height=260)
        f_raiz.pack(side=TOP)

        # FRAME LOGO PROGRAM
        f_logo = Frame(f_raiz, width=500, height=100)
        f_logo.pack(side=TOP)

        logo_programa = PhotoImage(file='logo.png')

        # LABEL LOGO PROGRAM
        l_logo = Label(f_raiz, image=logo_programa)
        l_logo.place(x=0, y=0)

        # SELECT USERS
        # FRAME SELECT USERS INTERVAL 01
        f_selecionar_intervalo_usuarios_label = Frame(f_raiz, width=500, height=80, bg='floral white')
        f_selecionar_intervalo_usuarios_label.pack(side=TOP)

        # LABEL SELECT USERS INTERVAL 01
        l_selecionar_intervalo_usuarios = Label(f_selecionar_intervalo_usuarios_label, text='Selecione o intervalo que o programa\nirá usar para curtir as fotos',
        font=('arial', 15, 'bold'), bg='floral white')
        l_selecionar_intervalo_usuarios.place(x=60, y=15)

        # FRAME SELECT USERS 02
        f_selecionar_intervalo_usuarios = Frame(f_raiz, width=500, height=80, bg='floral white')
        f_selecionar_intervalo_usuarios.pack(side=TOP)

        e_intervalo_inicial = Entry(f_selecionar_intervalo_usuarios, font=('arial', 13), width=10)
        e_intervalo_inicial.place(x=100, y=30)

        l_intervalos = Label(f_selecionar_intervalo_usuarios, text='-----',
        font=('arial', 15, 'bold'), bg='floral white')
        l_intervalos.place(x=225, y=25)

        e_intervalo_final = Entry(f_selecionar_intervalo_usuarios, font=('arial', 13), width=10)
        e_intervalo_final.place(x=300, y=30)

        # FRAME SELECT USERS 03
        f_selecionar_usuarios_button = Frame(f_raiz, width=500, height=80, bg='floral white')
        f_selecionar_usuarios_button.pack(side=TOP)

        b_selecionar_usuarios = Button(f_selecionar_usuarios_button, text='ENVIAR', font=('arial', 15, 'bold'),
        bg='dark salmon',
        activebackground='salmon', activeforeground='white',
        command=lambda: self.confirmacao(janela, top, checkvar, conteudo, email_curto, lbox_selecionar_usuarios, e_intervalo_inicial.get(), e_intervalo_final.get(), 1))
        b_selecionar_usuarios.place(x=200, y=20)

        # WINDOW CONFIGURATION
        top.resizable(width=False, height=False)
        top.title('AutoLike {} - Curtir Fotos De Perfil Específico - Banco de Dados'.format(app_version))
        top.geometry(g)
        top.mainloop()



    # GRAPHICAL INTERFACE METHOD
    def interface(self, email_curto):

        def aviso(janela, valor):
            
            if valor == 1:

                messagebox.showinfo('Todos os usuários selecionados', 'Todos os usuários selecionados!')


        janela = Tk()
        
        # WINDOW GEOMETRY
        lado = janela.winfo_screenwidth()
        cima = janela.winfo_screenheight()
        l = int(lado/3)
        c = int(cima/7)
        g = '{}x{}+{}+{}'.format(500, 610, l, c)

        # VARIABLES
        checkvar = IntVar()

        # ADDITIONAL CONFIGURATION
        file = open('app_version.txt', 'r')
        app_version = file.read()
        file.close()

        txt = 'bd_{}.txt'.format(email_curto)

        file = open(txt, 'r')
        conteudo_file = file.read()
        file.close()

        conteudo = conteudo_file.split('\n')


        try:

            file = open('informacoes.txt', 'r')
            content_file = file.read()
            file.close()

            intervalo = content_file.split('-')

            if intervalo == '':

                intervalo = [0, 0]

        except:

            intervalo = [0, 0]


        #print(intervalo)

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
        f_selecionar_intervalo_usuarios = Frame(f_raiz, width=500, height=60, bg='floral white')
        f_selecionar_intervalo_usuarios.pack(side=TOP)

        if intervalo[1] == '0':
            
            l_selecionar_intervalo_usuarios = Label(f_selecionar_intervalo_usuarios, text='Intervalo Selecionado: N/A',
            font=('arial', 15, 'bold'), bg='floral white')
            l_selecionar_intervalo_usuarios.place(x=110, y=20)

        elif intervalo[1] != '0':

            l_selecionar_intervalo_usuarios = Label(f_selecionar_intervalo_usuarios, text='Intervalo Selecionado:     {} --- {}'.format(intervalo[0], intervalo[1]),
            font=('arial', 15, 'bold'), bg='floral white')
            l_selecionar_intervalo_usuarios.place(x=80, y=20)

        #

        # FRAME SELECT USERS 04
        f_selecionar_usuarios_button = Frame(f_raiz, width=500, height=110, bg='floral white')
        f_selecionar_usuarios_button.pack(side=TOP)

        # CHECKBUTTON SELECT USERS 04
        cbutton = Checkbutton(f_selecionar_usuarios_button, text='Selecionar todos', font=('arial', 12, 'bold'),
        bg='dark salmon',
        activebackground='salmon', activeforeground='white',
        variable=checkvar, onvalue=1, offvalue=0,
        command=lambda: aviso(janela, checkvar.get()))
        cbutton.place(x=20, y=25)

        # BUTTON SELECT USERS 04
        b_intervalo_usuarios = Button(f_selecionar_usuarios_button, text='SELECIONAR\nINTERVALO', font=('arial', 13, 'bold'),
        bg='dark salmon',
        activebackground='salmon', activeforeground='white',
        command=lambda: self.intervalo_func(janela, checkvar.get(), conteudo, email_curto, lbox_selecionar_usuarios, app_version))
        b_intervalo_usuarios.place(x=200, y=15)

        b_selecionar_usuarios = Button(f_selecionar_usuarios_button, text='ENVIAR', font=('arial', 15, 'bold'),
        bg='dark salmon',
        activebackground='salmon', activeforeground='white',
        command=lambda: self.confirmacao(janela, 0, checkvar.get(), conteudo, email_curto, lbox_selecionar_usuarios, 0, 0, 0))
        b_selecionar_usuarios.place(x=350, y=20)

        # WINDOW CONFIGURATION
        janela.resizable(width=False, height=False)
        janela.title('AutoLike {} - Curtir Fotos De Perfil Específico - Banco de Dados'.format(app_version))
        janela.geometry(g)
        janela.mainloop()

    
    # CONSTRUCTOR METHOD
    def __init__(self):

        pass


a = CurtirFotosEscolhaBancoDeDadosAbrirMiniBD()
a.interface('neisserfreitasadvocacia')