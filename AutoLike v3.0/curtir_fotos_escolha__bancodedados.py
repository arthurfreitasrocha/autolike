# TKINTER LIBRARY
from tkinter import *
from tkinter import messagebox

# CUSTOM LIBRARY
from curtir_fotos_escolha__bancodedados___abrirminibd import CurtirFotosEscolhaBancoDeDadosAbrirMiniBD
from curtir_fotos_escolha__bancodedados___verselecionados import CurtirFotosEscolhaBancoDeDadosVerSelecionados
from curtir_fotos_escolha__bancodedados___removerselecionados import CurtirFotosEscolhaBancoDeDadosRemoverSelecionados
from curtir_fotos_escolha__bancodedados___acessarinstagram import CurtirFotosEscolhaBancoDeDadosAcessarInstagram


class CurtirFotosEscolhaBancoDeDados():

    def curtir_fotos(self, janela, quant_curtidas_usuarios, email_curto, status, n_usuarios):

        if quant_curtidas_usuarios.isnumeric() == False:

            messagebox.showinfo('Digite apenas números', 'Por favor informe um valor válido')

        else:

            quant_curtidas_usuarios = int(quant_curtidas_usuarios)

            file = open('curtir_fotos_usuarios.txt', 'r')
            conteudo_file = file.read()
            file.close()

            conteudo = conteudo_file.split('-')

            a = CurtirFotosEscolhaBancoDeDadosAcessarInstagram(janela, conteudo, quant_curtidas_usuarios)
            janela.destroy()
            a = CurtirFotosEscolhaBancoDeDados(email_curto, status, n_usuarios)


    # THIS FUNCTION CAN REMOVE ANY USER YOU HAVE
    def remover_selecionados(self, janela, email_curto):

        file = open('curtir_fotos_usuarios.txt', 'r')
        conteudo_file = file.read()
        file.close()

        conteudo = conteudo_file.split('-')

        if conteudo == [] or conteudo == '' or conteudo == ['']:

            messagebox.showinfo('Você ainda não escolheu nenhum usuário', 'Por favor selecione pelo menos 1 usuário para continuar')

        else:

            janela.destroy()
            a = CurtirFotosEscolhaBancoDeDadosRemoverSelecionados(email_curto)
            resp = a.retorno()
            a = CurtirFotosEscolhaBancoDeDados(resp[0], resp[1], resp[2])
        

    # THIS FUNCTION SHOW THE USER YOU HAVE SELECTED
    def ver_selecionados(self, janela, email_curto, status, n_usuarios):

        file = open('curtir_fotos_usuarios.txt', 'r')
        conteudo_file = file.read()
        file.close()

        conteudo = conteudo_file.split('-')

        if conteudo == [] or conteudo == '' or conteudo == ['']:

            messagebox.showinfo('Você ainda não escolheu nenhum usuário', 'Por favor selecione pelo menos 1 usuário para continuar')

        else:

            janela.destroy() 
            a = CurtirFotosEscolhaBancoDeDadosVerSelecionados()
            a = CurtirFotosEscolhaBancoDeDados(email_curto, status, n_usuarios)


    # THIS FUNCTION SHOW THE LIST OF USERS IN THE DB
    def abrir_mini_bd(self, janela, email_curto):
        
        janela.destroy()
        a = CurtirFotosEscolhaBancoDeDadosAbrirMiniBD(email_curto)
        resp = a.retorno()
        a = CurtirFotosEscolhaBancoDeDados(resp[0], resp[1], resp[2])



    def __init__(self, email_curto, status, n_usuarios):

        try:

            file = open('curtir_fotos_usuarios.txt', 'r')
            conteudo = file.read()
            file.close()

            if conteudo == '':

                status = 0

        except:

            pass


        janela = Tk()

        # WINDOW GEOMETRY
        lado = janela.winfo_screenwidth()
        cima = janela.winfo_screenheight()
        l = int(lado/3)
        c = int(cima/5)
        g = '{}x{}+{}+{}'.format(500, 400, l, c)

        # VARIABLES
        n_usuarios = n_usuarios
        status = status

        # ADDITIONAL CONFIGURATION
        try:
            file = open('curtir_fotos_usuarios.txt', 'r')
            conteudo_file = file.read()
            file.close()

            conteudo = conteudo_file.split('-')

            if conteudo != [] and conteudo != '' and conteudo != ['']:

                n_usuarios = len(conteudo)
                status = 1

        except:
            
            pass
        

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

        # CHOICE ====================
        # FRAME CHOICE
        f_escolha = Frame(f_raiz, width=500, height=140, bg='floral white')
        f_escolha.pack(side=TOP)
        
        if status == 0:
            
            # LABEL CHOICE
            l_escolha = Label(f_escolha, text='Aqui aparecerão a quantidade de\nusuários selecionados',
            font=('arial', 15, 'bold'), bg='floral white')
            l_escolha.place(x=90, y=5)

        else:
            
            # LABEL CHOICE
            l_escolha = Label(f_escolha, text='Você selecionou {} usuário(s)'.format(n_usuarios),
            font=('arial', 15, 'bold'), bg='floral white')
            l_escolha.place(x=100, y=15)

        # BUTTON CHOICE
        b_escolha_remover_selecionado = Button(f_escolha, text='Remover\nSelecionados', font=('arial', 15, 'bold'),
        bg='dark salmon',
        activebackground='salmon', activeforeground='white',
        command=lambda: self.remover_selecionados(janela, email_curto))
        b_escolha_remover_selecionado.place(x=20, y=65)

        b_escolha_ver_selecionados = Button(f_escolha, text='Ver\nSelecionados', font=('arial', 15, 'bold'),
        bg='dark salmon',
        activebackground='salmon', activeforeground='white',
        command=lambda: self.ver_selecionados(janela, email_curto, status, n_usuarios))
        b_escolha_ver_selecionados.place(x=185, y=65)

        b_escolha = Button(f_escolha, text='Selecionar\nUsuários', font=('arial', 15, 'bold'),
        bg='dark salmon',
        activebackground='salmon', activeforeground='white',
        command=lambda: self.abrir_mini_bd(janela, email_curto))
        b_escolha.place(x=350, y=65)

        # SEPARATOR ====================
        # FRAME SEPARATOR
        f_separador = Frame(f_raiz, width=500, height=10, bg='dark salmon')
        f_separador.pack(side=TOP)

        # AMOUNT OF LIKES ====================
        # FRAME AMOUNT OF LIKES
        f_quant_curtidas = Frame(f_raiz, width=500, height=150, bg='floral white')
        f_quant_curtidas.pack(side=TOP)
        
        # LABEL AMOUNT OF LIKES
        l_quant_curtidas = Label(f_quant_curtidas, text='Informe a quantidade de fotos que\nserão curtidas de cada usuário', 
        font=('arial', 15, 'bold'), bg='floral white')
        l_quant_curtidas.place(x=90, y=15)

        # ENTRY AMOUNT OF LIKES
        e_quant_curtidas = Entry(f_quant_curtidas, font=('arial', 15), width=10)
        e_quant_curtidas.place(x=150, y=98)

        # BUTTON AMOUNT OF LIKES
        b_quant_curtidas = Button(f_quant_curtidas, text='ENVIAR', font=('arial', 15, 'bold'),
        bg='dark salmon',
        activebackground='salmon', activeforeground='white',
        command=lambda: self.curtir_fotos(janela, e_quant_curtidas.get(), email_curto, status, n_usuarios))
        b_quant_curtidas.place(x=280, y=90)
        

        # WINDOW CONFIGURATION
        janela.resizable(width=False, height=False)
        janela.title('AutoLike 3.0 - Curtir Fotos De Um Perfil Específico - Banco de Dados')
        janela.geometry(g)
        janela.mainloop()
 

#a = CurtirFotosEscolhaBancoDeDados('arthur.freitas2000', 0, 0)
