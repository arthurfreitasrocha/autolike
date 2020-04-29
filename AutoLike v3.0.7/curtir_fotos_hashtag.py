# TKINTER LIBRARY
from tkinter import *
from tkinter import messagebox

# SELENIUM LIBRARY
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

# IMPORTANT LIBRARY'S
import os
import time

class CurtirFotosHashtag():

    def __init__(self):

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


                # PHOTO LIKE PROCESS
                picture = driver.find_elements(By.CLASS_NAME, 'v1Nh3.kIKUG._bz0w')
                picture[0].click()

                i = 0
                img_curtidas = 0

                while(i < var):
                    time.sleep(5)

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


            tempo = 2

            htg = e_hashtag.get()
            var = e_curtidas.get()

            if htg == '' or var == '':

                messagebox.showinfo('Erro', 'Por favor, preencha todos os campos')

            else:

                var = int(var)
                
                file = open('email_senha_instagram.txt', 'r')
                conteudo_file = file.read()
                file.close()

                conteudo = conteudo_file.split('-')

                email = conteudo[0]
                senha = conteudo[1]

                # ACESSING INSTAGRAM
                options = Options()
                options.headless = False

                driver = webdriver.Chrome(executable_path='C:\chromedriver.exe', chrome_options=options)
                driver.get('https://www.instagram.com/')

                driver.implicitly_wait(10)
                    
                driver.find_element(By.NAME, 'username').send_keys(email)
                driver.find_element(By.NAME, 'password').send_keys(senha)
                btn = driver.find_elements(By.TAG_NAME, 'button')
                btn[1].click()
                time.sleep(tempo)

                curtir()

        
        janela = Tk()

        # WINDOW GEOMETRY
        lado = janela.winfo_screenwidth()
        cima = janela.winfo_screenheight()
        l = int(lado/3)
        c = int(cima/5)
        g = '{}x{}+{}+{}'.format(500, 320, l, c)


        # FRAME ROOT PROGRAM
        f_logo = Frame(janela, width=500, height=100, bg='dark salmon')
        f_logo.pack(side=TOP)

        logo = PhotoImage(file='logo.png')

        l_logo = Label(f_logo, image=logo)
        l_logo.place(x=0, y=0)

        # FRAME HASHTAG, LIKES, CHANGE INSTAGRAM, SEND
        f_hashtag_curtidas = Frame(janela, width=500, height=300, bg='floral white')
        f_hashtag_curtidas.pack(side=TOP)

        l_hashtag = Label(f_hashtag_curtidas, text='Hashtag', font=('arial', 20, 'bold'), bg='floral white')
        l_hashtag.place(x=20, y=30)

        e_hashtag = Entry(f_hashtag_curtidas, font=('arial', 20, 'bold'))
        e_hashtag.place(x=150, y=30)

        l_curtidas = Label(f_hashtag_curtidas, text='Curtidas', font=('arial', 20, 'bold'), bg='floral white')
        l_curtidas.place(x=20, y=80)

        e_curtidas = Entry(f_hashtag_curtidas, font=('arial', 20, 'bold'))
        e_curtidas.place(x=150, y=80)

        b_enviar = Button(f_hashtag_curtidas, text='Realizar login no Instagram', font=('arial', 15, 'bold'), bg='dark salmon',
                        activebackground='salmon', activeforeground='white', command=info)
        b_enviar.place(x=165, y=150)

        janela.title('Auto Like 3.0 - Curtir Fotos Usando A Hashtag')
        janela.resizable(width=False, height=False)
        janela.geometry(g)
        janela.mainloop()

#a = CurtirFotosHashtag()
