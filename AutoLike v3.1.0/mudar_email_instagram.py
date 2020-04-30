# TKINTER LIBRARY
from tkinter import *
from tkinter import messagebox

# SELENIUM LIBRARY
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

class MudarEmailInstagram:

    def mostrar_senha(self):

        senha = self.e_senha.get()

        if self.estado_senha == 0:
            
            self.e_senha.destroy()
            self.b_mostrar_senha.destroy()
            
            self.e_senha = Entry(self.f_login_senha, font=('arial', 15, 'bold'), width=16)
            self.e_senha.place(x=120, y=143)

            self.b_mostrar_senha = Button(self.f_login_senha, text='OCULTAR SENHA', font=('arial', 11, 'bold'), bg='dark salmon',
                        activebackground='salmon', activeforeground='white', command=self.mostrar_senha)
            self.b_mostrar_senha.place(x=310, y=141)

            self.e_senha.insert(0, senha)

            self.estado_senha = 1

        else:
            
            self.e_senha.destroy()
            self.b_mostrar_senha.destroy()
            
            self.e_senha = Entry(self.f_login_senha, font=('arial', 15, 'bold'), width=17, show='*')
            self.e_senha.place(x=120, y=143)

            self.b_mostrar_senha = Button(self.f_login_senha, text='EXIBIR SENHA', font=('arial', 13, 'bold'), bg='dark salmon',
                        activebackground='salmon', activeforeground='white', command=self.mostrar_senha)
            self.b_mostrar_senha.place(x=320, y=141)

            self.e_senha.insert(0, senha)

            self.estado_senha = 0



    def __init__(self):

        def alterar():

            email = self.e_login.get()
            senha = self.e_senha.get()

            if email == '' or senha == '':

                messagebox.showwarning('ERRO: Campos vazios', 'Um ou mais campos vazios.\nPor favor, forneça um email e senha válidos')

            else:

                messagebox.showinfo('Aguarde', 'Por favor aguarde, estamos validando sua conta')

                # ACESSING INSTAGRAM
                options = Options()
                options.headless = True

                driver = webdriver.Chrome(executable_path='C:\chromedriver.exe', chrome_options=options)
                driver.get('https://www.instagram.com/')

                driver.implicitly_wait(10)
                    
                driver.find_element(By.NAME, 'username').send_keys(email)
                driver.find_element(By.NAME, 'password').send_keys(senha)
                btn = driver.find_elements(By.TAG_NAME, 'button')
                btn[1].click()

                erro = 0
                try:

                    conta_invalida = driver.find_element_by_id('slfErrorAlert')
                    msg_conta_invalida = conta_invalida.text

                    print(msg_conta_invalida)

                    erro = 1

                except:

                    pass
                
                if erro == 0:

                    file = open('email_senha_instagram.txt', 'w')
                    file.write('{}-{}-1'.format(email, senha))
                    file.close()

                    messagebox.showinfo('Sucesso', 'Email e senha do Instagram alterados')

                else:

                    messagebox.showinfo('Falha', 'Nós não conseguimos validar sua conta.\nTem certeza de que você escreveu seus dados corretamente?')

                self.window.destroy()


        self.window = Tk()

        # WINDOW GEOMETRY
        self.lado = self.window.winfo_screenwidth()
        self.cima = self.window.winfo_screenheight()
        self.l = int(self.lado/3)
        self.c = int(self.cima/5)
        self.g = '{}x{}+{}+{}'.format(500, 370, self.l, self.c)

        # ADDITIONAL CONFIGURATION
        file = open('app_version.txt', 'r')
        app_version = file.read()
        file.close()

        # VARIABLES
        self.estado_senha = 0 # 0 == INVISIBLE, 1 == VISIBLE


        # FRAME LOGO
        self.f_logo = Frame(self.window, width=500, height=100, bg='dark salmon')
        self.f_logo.pack(side=TOP)

        self.logo = PhotoImage(file='logo.png')

        self.l_logo = Label(self.f_logo, image=self.logo)
        self.l_logo.place(x=0, y=0)

        # FRAME LOGIN, PASSWORD
        self.f_login_senha = Frame(self.window, width=500, height=300, bg='floral white')
        self.f_login_senha.pack(side=TOP)

        self.l_mensagem = Label(self.f_login_senha, text='Por favor, informe seu\nlogin e senha do Instagram', font=('arial', 15, 'bold'), bg='floral white')
        self.l_mensagem.place(x=130, y=17)
        
        self.l_login = Label(self.f_login_senha, text='Login', font=('arial', 20, 'bold'), bg='floral white')
        self.l_login.place(x=20, y=90)

        self.e_login = Entry(self.f_login_senha, font=('arial', 15, 'bold'), width=30)
        self.e_login.place(x=120, y=93)

        self.l_senha = Label(self.f_login_senha, text='Senha', font=('arial', 20, 'bold'), bg='floral white')
        self.l_senha.place(x=20, y=140)

        self.e_senha = Entry(self.f_login_senha, font=('arial', 15, 'bold'), width=17, show='*')
        self.e_senha.place(x=120, y=143)
    
        self.b_mostrar_senha = Button(self.f_login_senha, text='EXIBIR SENHA', font=('arial', 13, 'bold'), bg='dark salmon',
                        activebackground='salmon', activeforeground='white', command=self.mostrar_senha)
        self.b_mostrar_senha.place(x=320, y=141)

        self.b_enviar = Button(self.f_login_senha, text='ENVIAR', font=('arial', 15, 'bold'), bg='dark salmon',
                        activebackground='salmon', activeforeground='white', command=alterar)
        self.b_enviar.place(x=200, y=205)

        self.window.title('Auto Like {} - Mudar Email Instagram'.format(app_version))
        self.window.geometry(self.g)
        self.window.resizable(width=False, height=False)
        self.window.mainloop()

#a = MudarEmailInstagram()
