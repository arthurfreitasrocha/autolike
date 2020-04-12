from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from tkinter import *
from tkinter import messagebox
import time
import os

def menu():

    def mudar_email():

        def alterar():

            email = e_login.get()
            senha = e_senha.get()

            file = open('email_senha_instagram.txt', 'w')
            file.write('{}\n{}'.format(email, senha))
            file.close()

            messagebox.showinfo('Sucesso', 'Email e senha do Instagram alterados. Reinicie o programa')

            top.destroy()
            janela.destroy()

        top = Toplevel()

        lado, cima = (top.winfo_screenwidth()), (top.winfo_screenheight())

        f_logo = Frame(top, width=500, height=100, bg='dark salmon')
        f_logo.pack(side=TOP)

        logo = PhotoImage(file='teste2.png')

        l_logo = Label(f_logo, image=logo)
        l_logo.place(x=0, y=0)

        f_login_senha = Frame(top, width=500, height=300, bg='floral white')
        f_login_senha.pack(side=TOP)

        l_mensagem = Label(f_login_senha, text='Por favor informe seu login e senha do Instagram', font=('arial', 15, 'bold'), bg='floral white')
        l_mensagem.place(x=10, y=20)
        
        l_login = Label(f_login_senha, text='Login', font=('arial', 20, 'bold'), bg='floral white')
        l_login.place(x=20, y=90)

        e_login = Entry(f_login_senha, font=('arial', 20, 'bold'))
        e_login.place(x=120, y=90)

        l_senha = Label(f_login_senha, text='Senha', font=('arial', 20, 'bold'), bg='floral white')
        l_senha.place(x=20, y=140)

        e_senha = Entry(f_login_senha, font=('arial', 20, 'bold'), show='*')
        e_senha.place(x=120, y=140)

        b_enviar = Button(f_login_senha, text='ENVIAR', font=('arial', 15, 'bold'), bg='dark salmon',
                          activebackground='salmon', activeforeground='white', command=alterar)
        b_enviar.place(x=200, y=205)

        top.title('Auto Like Instagram')
        top.geometry('{}x{}+400+200'.format(lado-870, cima-400))
        top.resizable(width=False, height=False)
        top.mainloop()

    def info():

        def curtir():

            cls = driver.find_elements(By.CLASS_NAME, 'aOOlW.HoLwm')
            cls[0].click()
            time.sleep(tempo)

            inp = driver.find_elements(By.TAG_NAME, 'input')
            inp[2].send_keys(htg)

            cls = driver.find_elements(By.CLASS_NAME, 'Ap253')
            cls[0].click()
            time.sleep(tempo)


            # PROCESSO DE CURTIDA DAS FOTOS
            picture = driver.find_elements(By.CLASS_NAME, 'v1Nh3.kIKUG._bz0w')
            picture[0].click()

            i = 0
            img_curtidas = 0

            while(i < var):
                time.sleep(5)

                # INÍCIO DA MAGICA
                try:
                    name = driver.find_element(By.CLASS_NAME, 'sqdOP.yWX7d._8A5w5.ZIAjV').text
                    kokoro = driver.find_elements(By.CLASS_NAME, 'wpO6b')
                    arrow = driver.find_elements(By.CLASS_NAME, '_65Bje.coreSpriteRightPaginationArrow')
      
                except:
                    messagebox.showinfo('Erro', 'Algo deu errado, por favor reinicie o programa.\nTotal de {} publicações curtidas'.format(i))
                    janela.destroy()
                
                j = 0
                email_curto = ''
                while(j < len(email)):
                    if email[j] != '@':
                        email_curto += email[j]
                        
                    else:
                        j = len(email)

                    j += 1

                try:
                    txt = 'bd_{}.txt'.format(email_curto)
                    
                    file = open(txt, 'r')
                    conteudo_file = file.read()
                    file.close()

                    users = conteudo_file.split('\n')

                except:
                    txt = 'bd_{}.txt'.format(email_curto)
                    
                    file = open(txt, 'w')
                    file.write('{}\n'.format(name))
                    file.close()

                file = open(txt, 'r')
                conteudo_file = file.read()
                file.close()

                users = conteudo_file.split('\n')

                j = 0
                cont = 0
                while(j < len(users)):
                    try:
                        if name != users[j]:
                            cont += 1
                    except:
                        pass

                    j += 1

                if cont == len(users):

                    k = 0
                    contador = 0
                    while(k < len(users)):
                        try:
                            if name != users[k]:
                                contador += 1
                        except:
                            pass

                        k += 1

                    if contador == len(users):
                        txt = 'bd_{}.txt'.format(email_curto)
                        
                        file = open(txt, 'a')
                        file.write('{}\n'.format(name))
                        file.close()
                        
                    else:
                        pass
                    
                    try:
                        kokoro[0].click()
                        arrow[0].click()
                        img_curtidas += 1
                        
                    except:
                        messagebox.showinfo('Erro', 'Algo deu errado, por favor reinicie o programa.\nTotal de {} publicações curtidas'.format(i))
                        janela.destroy()
                        driver.close()
                        exit(0)

                else:
                    i += -1
                    arrow[0].click()

                i += 1
                print('IMAGENS CURTIDAS: {}'.format(img_curtidas))
            
            messagebox.showinfo('Sucesso', 'TOTAL DE {} PUBLICAÇÕES CURTIDAS COM SUCESSO'.format(var))

            driver.close()
            janela.destroy()
            exit(0)


        cont = 0
        tempo = 2

        htg = e_hashtag.get()
        var = e_curtidas.get()

        if htg == '' or var == '':

            messagebox.showinfo('Erro', 'Por favor, preencha todos os campos')

        else:

            var = int(var)
            
            file = open('email_senha_instagram.txt', 'r')
            conteudo = file.readlines()
            email = conteudo[0]
            senha = conteudo[1]
            file.close()

            # ACESSANDO INSTAGRAM
            options = Options()
            options.headless = False

            driver = webdriver.Chrome(executable_path='C:\chromedriver.exe', chrome_options=options)
            driver.get('https://www.instagram.com/')

            #driver.implicitly_wait(10)
            #driver.find_element_by_link_text('Conecte-se').click()
            #time.sleep(tempo)

            #try:

            driver.implicitly_wait(10)
                
            driver.find_element(By.NAME, 'username').send_keys(email)
            driver.find_element(By.NAME, 'password').send_keys(senha)
            btn = driver.find_elements(By.TAG_NAME, 'button')
            btn[1].click()
            time.sleep(tempo)

            cont = 1

            #except:
                
                #messagebox.showinfo('Erro', 'Login ou senha incorretos')
                #janela.destroy()
                #driver.close()

                #cont = 0
                
            #if cont == 1:

            curtir()

    try:

        file = open('email_senha_instagram.txt', 'r')
        conteudo = file.readlines()
        file.close()

        email = conteudo[0]

    except:

        file = open('email_senha_instagram.txt', 'w')
        file.close()
        
        email = 'Nenhuma conta registrada ainda'
    
    janela = Tk()

    lado, cima = (janela.winfo_screenwidth()), (janela.winfo_screenheight())

    f_logo = Frame(janela, width=500, height=100, bg='dark salmon')
    f_logo.pack(side=TOP)

    logo = PhotoImage(file='teste2.png')

    l_logo = Label(f_logo, image=logo)
    l_logo.place(x=0, y=0)

    f_hashtag_curtidas = Frame(janela, width=500, height=300, bg='floral white')
    f_hashtag_curtidas.pack(side=TOP)

    l_mensagem = Label(f_hashtag_curtidas, text='{}'.format(email), font=('arial', 15, 'bold'), bg='floral white')
    l_mensagem.place(x=19, y=20)

    l_hashtag = Label(f_hashtag_curtidas, text='Hashtag', font=('arial', 20, 'bold'), bg='floral white')
    l_hashtag.place(x=20, y=70)

    e_hashtag = Entry(f_hashtag_curtidas, font=('arial', 20, 'bold'))
    e_hashtag.place(x=150, y=70)

    l_curtidas = Label(f_hashtag_curtidas, text='Curtidas', font=('arial', 20, 'bold'), bg='floral white')
    l_curtidas.place(x=20, y=120)

    e_curtidas = Entry(f_hashtag_curtidas, font=('arial', 20, 'bold'))
    e_curtidas.place(x=150, y=120)

    b_mudar_email = Button(f_hashtag_curtidas, text='Mudar\nInstagram', font=('arial', 15, 'bold'), bg='dark salmon',
                      activebackground='salmon', activeforeground='white', command=mudar_email)
    b_mudar_email.place(x=10, y=190)

    b_enviar = Button(f_hashtag_curtidas, text='Realizar login no Instagram', font=('arial', 15, 'bold'), bg='dark salmon',
                      activebackground='salmon', activeforeground='white', command=info)
    b_enviar.place(x=165, y=190)

    janela.title('Auto Like Instagram')
    janela.geometry('{}x{}+400+200'.format(lado-870, cima-400))
    janela.resizable(width=False, height=False)
    janela.mainloop()

menu()
