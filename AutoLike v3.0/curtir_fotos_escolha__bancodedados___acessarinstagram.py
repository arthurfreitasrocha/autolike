# SELENIUM LIBRARY
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

# TKINTER LIBRAY
from tkinter import *
from tkinter import messagebox

# ADDITIONAL LIBRARY
import time
import os

class CurtirFotosEscolhaBancoDeDadosAcessarInstagram:

    def __init__(self, janela, conteudo, quant_curtidas):

        print(len(conteudo))

        # VARIABLES
        tempo = 2
        
        # CATCH MAIL AND PASSWORD OF INSTAGRAM
        file = open('email_senha_instagram.txt', 'r')
        content_file = file.read()
        file.close()

        content = content_file.split('-')

        email = content[0]
        senha = content[1]


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

        caixa_inicio = driver.find_elements(By.CLASS_NAME, 'aOOlW.HoLwm')
        caixa_inicio[0].click()
        time.sleep(tempo)

        i = 0
        erro = 0
        perfis = 0
        fotos = 0
        while(i < len(conteudo)):

            try:

                time.sleep(tempo)

                print(conteudo[i])

                erro += 1

                # ENTERING THE USERNAME IN THE INSTAGRAM TEXT BOX
                inp = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
                inp.send_keys(conteudo[i])

                erro += 1

                # CLICKING ON THE FIRST RETURN
                nome = driver.find_elements(By.CLASS_NAME, 'z556c')
                nome[0].click()

                erro += 1

                time.sleep(tempo)

                # CLICKING ON THE FIRST PHOTO
                foto = driver.find_elements(By.CLASS_NAME, 'v1Nh3.kIKUG._bz0w')
                foto[0].click()

                erro += 1

                time.sleep(tempo)

                # LIKE PHOTOS PROCESS
                j = 0
                while(j < quant_curtidas):

                    coracao = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button')
                    coracao.click()   

                    seta_direita = driver.find_elements(By.CLASS_NAME, '_65Bje.coreSpriteRightPaginationArrow')
                    seta_direita[0].click()

                    time.sleep(tempo)

                    j += 1
                    fotos += 1

                erro += 1

                time.sleep(tempo)

                # CLOSE THE WINDOW OF PHOTOS
                fechar = driver.find_element_by_xpath('/html/body/div[4]/div[3]/button')
                fechar.click()

                erro += 1

                perfis += 1

                conteudo.pop(i)


            except:
                
                # REMOVING USERS WITH ALREADY LIKED PHOTOS FROM THE LIST
                conteudo_string = ''
                k = 0
                while(i < len(conteudo)):
                    
                    if k == 0:

                        conteudo_string = conteudo[k]
                    
                    else:

                        conteudo_string = "-" + conteudo[k]

                    k += 1

                
                if conteudo == []:

                    file = open('curtir_fotos_usuarios.txt', 'w')
                    file.close()

                else:

                    file = open('curtir_fotos_usuarios.txt', 'w')
                    file.write(conteudo_string)
                    file.close()

                # IF ANY ERROR HAS OCURRED, A MESSAGE WILL BE SHOWN
                messagebox.showinfo('Erro', 'Algo deu errado e não foi possível concluir esta ação.\nTotal de {} perfis acessados e {} fotos curtidas. ERRO: 00{}'.format(perfis, fotos, erro))

                erro = 1

            i += 1

        if erro < 1:
            
            # REMOVING USERS WITH ALREADY LIKED PHOTOS FROM THE LIST
            conteudo_string = ''
            k = 0
            while(i < len(conteudo)):
                    
                if k == 0:

                    conteudo_string = conteudo[k]
                    
                else:

                    conteudo_string = "-" + conteudo[k]

                k += 1

            if conteudo == []:

                file = open('curtir_fotos_usuarios.txt', 'w')
                file.close()

            else:

                file = open('curtir_fotos_usuarios.txt', 'w')
                file.write(conteudo_string)
                file.close()

            # IF ALL GOES WELL A SUCCESS MESSAGE WILL BE SHOWN
            messagebox.showinfo('Sucesso', 'Total de {} perfis acessados e {} fotos curtidas com sucesso!'.format(perfis, fotos))

        driver.close()

#a = CurtirFotosEscolhaBancoDeDadosAcessarInstagram(['arthur2k_'], 3)