# TKINTER LIBRARY
from tkinter import *
from tkinter import messagebox

# CUSTOM LIBRARY
from curtir_fotos_escolha__bancodedados___abrirminibd import CurtirFotosEscolhaBancoDeDadosAbrirMiniBD
from curtir_fotos_escolha__bancodedados___verselecionados import CurtirFotosEscolhaBancoDeDadosVerSelecionados
from curtir_fotos_escolha__bancodedados___removerselecionados import CurtirFotosEscolhaBancoDeDadosRemoverSelecionados
from curtir_fotos_escolha__bancodedados___acessarinstagram import *

class CurtirFotosEscolhaBancoDeDados:

    # THIS METHOD SHOW A MESSAGE IF THE USER CHOICE
    def escolha(self, valor):

        valor = int(valor)

        if valor == 1:

            messagebox.showinfo('Sucesso', 'Você selecionou a opção Curtidas em Sequência.')

        else:

            messagebox.showinfo('Sucesso', 'Você selecionou a opção Curtidas Aleatórias.')


    # THIS METHOD START THE LIKE PROCESS
    def curtir_fotos(self, janela, conteudo, quant_curtidas_usuarios, valor, email_curto, status, n_usuarios):
        
        valor = int(valor)
        var_controle = 0

        file = open('informacoes.txt', 'r')
        content_file = file.read()
        file.close()

        intervalo = content_file.split('-')

        if intervalo[0].isnumeric() == True or intervalo[1] == True:
            
            intervalo[0] = int(intervalo[0])
            intervalo[1] = int(intervalo[1])

            var_controle = 1


        if valor == 1:

            if quant_curtidas_usuarios.isnumeric() == False:

                messagebox.showinfo('Digite apenas números', 'Por favor informe um valor válido')

            else:

                if var_controle == 1:

                    i = 0
                    cont = intervalo[0]
                    novo_conteudo = []
                    while(i < len(conteudo)):

                        if cont == i:

                            novo_conteudo.append(cont)

                            cont += 1

                        i += 1


                    janela.destroy()
                    a = CurtirFotosPerfilSequencia()
                    a.abrir_navegador(janela, novo_conteudo, quant_curtidas_usuarios)
                    a = CurtirFotosEscolhaBancoDeDados(email_curto, 2, n_usuarios)

                else:

                    janela.destroy()
                    a = CurtirFotosPerfilSequencia()
                    a.abrir_navegador(janela, conteudo, quant_curtidas_usuarios)
                    a = CurtirFotosEscolhaBancoDeDados(email_curto, 2, n_usuarios)

        else:

            if quant_curtidas_usuarios.isnumeric() == False:

                messagebox.showinfo('Digite apenas números', 'Por favor informe um valor válido')

            else:

                if var_controle == 1:

                    i = 0
                    cont = intervalo[0]
                    novo_conteudo = []
                    while(i <= len(conteudo)):

                        if cont == i:

                            novo_conteudo.append(cont)

                            cont += 1

                        i += 1


                    janela.destroy()
                    a = CurtirFotosPerfilSequencia()
                    a.abrir_navegador(janela, novo_conteudo, quant_curtidas_usuarios)
                    a = CurtirFotosEscolhaBancoDeDados(email_curto, 2, n_usuarios)

                else:

                    janela.destroy()
                    a = CurtirFotosPerfilSequencia()
                    a.abrir_navegador(janela, conteudo, quant_curtidas_usuarios)
                    a = CurtirFotosEscolhaBancoDeDados(email_curto, 2, n_usuarios)



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

        valor_conteudo = len(conteudo)
        cont = 0
        i = 0
        while(i < valor_conteudo):

            if conteudo[i] == '':

                cont += 1

            i += 1

        if conteudo == [] or conteudo == '' or conteudo == [''] or cont == valor_conteudo:

            messagebox.showinfo('Você ainda não escolheu nenhum usuário', 'Por favor selecione pelo menos 1 usuário para continuar')

        else:

            janela.destroy() 
            a = CurtirFotosEscolhaBancoDeDadosVerSelecionados()
            a = CurtirFotosEscolhaBancoDeDados(email_curto, status, n_usuarios)


    # THIS FUNCTION SHOW THE LIST OF USERS IN THE DB
    def abrir_mini_bd(self, janela, email_curto):
        
        janela.destroy()
        a = CurtirFotosEscolhaBancoDeDadosAbrirMiniBD()
        a.interface(email_curto)

        try:
            
            resp = a.retorno()
            a = CurtirFotosEscolhaBancoDeDados(resp[0], resp[1], resp[2])

        except:

            a = CurtirFotosEscolhaBancoDeDados(email_curto, 0, 0)



    def __init__(self, email_curto, status, n_usuarios):

        try:

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

                else:

                    n_usuarios += 1

                i += 1

            conteudo = lista

        except:

            pass


        janela = Tk()

        # WINDOW GEOMETRY
        lado = janela.winfo_screenwidth()
        cima = janela.winfo_screenheight()
        l = int(lado/3)
        c = int(cima/7)
        g = '{}x{}+{}+{}'.format(500, 500, l, c)

        # ADDITIONAL CONFIGURATION
        file = open('app_version.txt', 'r')
        app_version = file.read()
        file.close()

        # VARIABLES
        n_usuarios = n_usuarios
        status = status
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

        # CHOICE ====================
        # FRAME CHOICE
        f_escolha = Frame(f_raiz, width=500, height=140, bg='floral white')
        f_escolha.pack(side=TOP)
        
        if status == 0 or status == 2:
            
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

        # LIKE METHOD ====================
        # FRAME LIKE METHOD
        f_metodo_curtir = Frame(f_raiz, width=500, height=90, bg='floral white')
        f_metodo_curtir.pack(side=TOP)

        l_metodo_curtir = Label(f_metodo_curtir, text='Método de Curtidas',
        font=('arial', 15, 'bold'), bg='floral white')
        l_metodo_curtir.place(x=150, y=10)

        rb_curtidas_sequencia = Radiobutton(f_metodo_curtir, text='Curtidas em Sequência',
        font=('arial', 12, 'bold'), bg='floral white',
        variable=valor_cb, value=1,
        command=lambda: self.escolha(valor_cb.get()))
        rb_curtidas_sequencia.place(x=50, y=50)

        rb_curtidas_aleatorias = Radiobutton(f_metodo_curtir, text='Curtidas Aleatórias',
        font=('arial', 12, 'bold'), bg='floral white',
        variable=valor_cb, value=2,
        command=lambda: self.escolha(valor_cb.get()))
        rb_curtidas_aleatorias.place(x=270, y=50)

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
        command=lambda: self.curtir_fotos(janela, conteudo, e_quant_curtidas.get(), valor_cb.get(), email_curto, status, n_usuarios))
        b_quant_curtidas.place(x=280, y=90)
        

        # WINDOW CONFIGURATION
        janela.resizable(width=False, height=False)
        janela.title('AutoLike {} - Curtir Fotos De Perfil Específico - Banco de Dados'.format(app_version))
        janela.geometry(g)


        # RETORNA AS INFORMAÇÕES DA AUTOMATIZAÇÃO
        if status == 2:

            file = open('informacoes.txt', 'r')
            resp_file = file.read()
            file.close()

            resp = resp_file.split('-')

            if resp[0] == '1':
                
                if resp[2] == '0':

                    messagebox.showinfo('Sucesso', 'Nenhuma publicação curtida')
                
                else:

                    messagebox.showinfo('Sucesso', 'Total de {} perfi(s) acessado(s) e {} foto(s) curtidas com sucesso!'.format(resp[1], resp[2]))

            else:

                messagebox.showinfo('Fracasso', 'Algo deu errado. ERRO: 00{}'.format(resp[3]))

            status = 0

        janela.mainloop()
 

#a = CurtirFotosEscolhaBancoDeDados('arthur.freitas2000', 0, 0, 0, 0)
