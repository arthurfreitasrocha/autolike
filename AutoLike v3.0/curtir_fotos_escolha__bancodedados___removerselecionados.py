# TKINTER LIBRARY
from tkinter import *
from tkinter import messagebox


class CurtirFotosEscolhaBancoDeDadosRemoverSelecionados:

    # THIS FUNCTION RETURNS THE INFORMATION STORED IN THE FILE BELOW
    def retorno(self):
        
        file = open('informacoes.txt', 'r')
        conteudo_file = file.read()
        file.close()

        conteudo = conteudo_file.split('-')

        lista = []
        lista.append(conteudo[0])
        lista.append(conteudo[1])
        lista.append(conteudo[2])

        return lista


    # THIS FUNCTION REMOVE THE SELECTED USER(S)
    def remover_selecionados(self, janela, lbox, email_curto):

        temp = lbox.curselection()
        
        file = open('curtir_fotos_usuarios.txt', 'r')
        conteudo_file = file.read()
        file.close()

        conteudo = conteudo_file.split('-')
        
        i = 0
        lista = []
        while(i < len(temp)):

            lista.append(conteudo[temp[i]])

            i += 1


        i = 0
        while(i < len(conteudo)):
            
            j = 0
            while(j < len(lista)):
                
                if lista[j] == conteudo[i]:
                    
                    conteudo.pop(i)

                j += 1

            i += 1



        i = 0
        n_usuarios = len(conteudo)
        conteudo_string = ''
        while(i < len(conteudo)):

            if i == 0:

                conteudo_string = conteudo[i]

            else:

                conteudo_string += '-' + conteudo[i]

            i += 1


        file = open('curtir_fotos_usuarios.txt', 'w')
        file.write(conteudo_string)
        file.close()

        file = open('informacoes.txt', 'w')
        file.write('{}-{}-{}'.format(email_curto, 1, n_usuarios))
        file.close()

        messagebox.showinfo('Sucesso', '{} usuário(s) removido(s) com sucesso!'.format(len(temp)))
        janela.destroy()

        self.retorno()



    def __init__(self, email_curto):

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
        file = open('curtir_fotos_usuarios.txt', 'r')
        conteudo_file = file.read()
        file.close()

        conteudo = conteudo_file.split('-')


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
        yscrollcommand=sb_selecionar_usuarios.set, selectmode=MULTIPLE)

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
        b_selecionar_usuarios_voltar = Button(f_selecionar_usuarios_button, text='<- Voltar', font=('arial', 15, 'bold'),
        bg='dark salmon',
        activebackground='salmon', activeforeground='white',
        command=voltar)
        b_selecionar_usuarios_voltar.place(x=120, y=20)

        b_selecionar_usuarios = Button(f_selecionar_usuarios_button, text='ENVIAR', font=('arial', 15, 'bold'),
        bg='dark salmon',
        activebackground='salmon', activeforeground='white',
        command=lambda: self.remover_selecionados(janela, lbox_selecionar_usuarios, email_curto))
        b_selecionar_usuarios.place(x=280, y=20)

        # WINDOW CONFIGURATION
        janela.resizable(width=False, height=False)
        janela.title('AutoLike 3.0 - Curtir Fotos De Um Perfil Específico - Banco de Dados')
        janela.geometry(g)
        janela.mainloop()

#a = CurtirFotosEscolhaBancoDeDadosRemoverSelecionados('arthur.freitas2000')