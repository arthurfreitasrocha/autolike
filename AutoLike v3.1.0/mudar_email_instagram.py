from tkinter import *
from tkinter import messagebox

class MudarEmailInstagram:

    def __init__(self):

        def alterar():

            email = e_login.get()
            senha = e_senha.get()

            if email == '' or senha == '':

                messagebox.showwarning('ERRO: Campos vazios', 'Um ou mais campos vazios.\nPor favor, forneça um email e senha válidos')

            else:

                file = open('email_senha_instagram.txt', 'w')
                file.write('{}-{}'.format(email, senha))
                file.close()

                messagebox.showinfo('Sucesso', 'Email e senha do Instagram alterados')

                window.destroy()


        window = Tk()

        # WINDOW GEOMETRY
        lado = window.winfo_screenwidth()
        cima = window.winfo_screenheight()
        l = int(lado/3)
        c = int(cima/5)
        g = '{}x{}+{}+{}'.format(500, 370, l, c)

        # ADDITIONAL CONFIGURATION
        file = open('app_version.txt', 'r')
        app_version = file.read()
        file.close()

        # FRAME LOGO
        f_logo = Frame(window, width=500, height=100, bg='dark salmon')
        f_logo.pack(side=TOP)

        logo = PhotoImage(file='logo.png')

        l_logo = Label(f_logo, image=logo)
        l_logo.place(x=0, y=0)

        # FRAME LOGIN, PASSWORD
        f_login_senha = Frame(window, width=500, height=300, bg='floral white')
        f_login_senha.pack(side=TOP)

        l_mensagem = Label(f_login_senha, text='Por favor informe seu login e senha do Instagram', font=('arial', 15, 'bold'), bg='floral white')
        l_mensagem.place(x=10, y=20)
        
        l_login = Label(f_login_senha, text='Login', font=('arial', 20, 'bold'), bg='floral white')
        l_login.place(x=20, y=90)

        e_login = Entry(f_login_senha, font=('arial', 15, 'bold'), width=30)
        e_login.place(x=120, y=93)

        l_senha = Label(f_login_senha, text='Senha', font=('arial', 20, 'bold'), bg='floral white')
        l_senha.place(x=20, y=140)

        e_senha = Entry(f_login_senha, font=('arial', 15, 'bold'), width=30, show='*')
        e_senha.place(x=120, y=143)

        b_enviar = Button(f_login_senha, text='ENVIAR', font=('arial', 15, 'bold'), bg='dark salmon',
                        activebackground='salmon', activeforeground='white', command=alterar)
        b_enviar.place(x=200, y=205)

        window.title('Auto Like {} - Mudar Email Instagram'.format(app_version))
        window.geometry(g)
        window.resizable(width=False, height=False)
        window.mainloop()

#a = MudarEmailInstagram()
