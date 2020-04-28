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

    # ESSE MÉTODO ESCREVE EM UM .TXT O RESULTADO DO PROCESSO
    def escrever_resultado(self, perfis, fotos, erro):

        if erro < 1:

            file = open('informacoes.txt', 'w')
            file.write('1-{}-{}-{}'.format(perfis, fotos, erro))
            file.close()

        else:

            file = open('informacoes.txt', 'w')
            file.write('0-{}-{}-{}'.format(perfis, fotos, erro))
            file.close()


    # ESSA FUNÇÃO PAUSA O PROGRAMA EM 2 SEGUNDOS
    def tempo(self, driver):

        tempo = 2

        time.sleep(tempo)
        driver.implicitly_wait(10)


    def verificacao(self, conteudo):
        
        cont = 0
        valor_conteudo = len(conteudo)

        i = 0
        while(i < valor_conteudo):

            if conteudo[i] == '':

                cont += 1

            i += 1

        if cont == valor_conteudo:

            return 'True'

        else:

            return 'False'


    # ESSA FUNÇÃO REMOVE OS USUÁRIOS INFORMADOS DA LISTA
    def remover_usuario(self, conteudo, indice):

        if indice == -1:
            
            file = open('curtir_fotos_usuarios.txt', 'w')
            file.close()

        else:

            # REMOVING USERS WITH ALREADY LIKED PHOTOS FROM THE LIST
            conteudo[indice] = ''

            conteudo_string = ''
            i = 0
            while(i < len(conteudo)):
                        
                if i == 0:

                    conteudo_string = conteudo[i]
                        
                else:

                    conteudo_string += "-" + conteudo[i]

                i += 1

            if conteudo == []:

                file = open('curtir_fotos_usuarios.txt', 'w')
                file.close()

            else:
                
                file = open('curtir_fotos_usuarios.txt', 'w')
                file.write(conteudo_string)
                file.close()

            return conteudo


    # ESSA FUNÇÃO CURTE AS FOTOS DO USUÁRIO 'x'
    def curtir_fotos(self, driver, conteudo, quant_curtidas, perfis, fotos, cont):

        print('PERFIL SENDO ACESSADO: {}'.format(conteudo[cont]))
        i = 0
        while(i < quant_curtidas):

            coracao = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button')
            coracao.click()

            seta_direita = driver.find_elements(By.CLASS_NAME, '_65Bje.coreSpriteRightPaginationArrow')
            seta_direita[0].click()

            # PAUSE OF 2 SECONDS
            self.tempo(driver)

            i += 1
            fotos += 1

            print('{} FOTO(S) CURTIDA(S) DE {}'.format(i, conteudo[cont]))

        print('====================')

        self.remover_usuario(conteudo, cont)

        perfis += 1
        cont += 1

        lista = [cont, perfis, fotos]

        return lista


    # ESSA FUNÇÃO VERIFICA SE O USUÁRIO 'x' EXISTE
    def verificar_existencia_usuario(self, driver, conteudo, indice, cont):

        j = cont
        valor_conteudo = len(conteudo)
        while(j < valor_conteudo):
            
            # TENTA INSERIR O ITEM 'I' DA LISTA
            try:
        
                inp = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
                inp.clear()
                inp.send_keys(conteudo[j])

                # PAUSE OF 2 SECONDS
                self.tempo(driver)

                # CLICKING ON THE FIRST RETURN
                nome = driver.find_elements(By.CLASS_NAME, 'z556c')
                nome[0].click()

                # PAUSE OF 2 SECONDS
                self.tempo(driver)
                        
                break

            except:

                if j == valor_conteudo-1:
                    
                    print('{} NÃO ENCONTRADO. ENCERRANDO O PROGRAMA'.format(conteudo[j]))
                    self.remover_usuario(conteudo, -1)
                        
                    break
                
                print('{} NÃO ENCONTRADO, PARTINDO PARA PRÓXIMO USUÁRIO'.format(conteudo[j]))
                self.remover_usuario(conteudo, j)
                
                j += 1
                indice += 1

        lista = [j, indice]

        return lista


    # ESSA FUNÇÃO PEGA O EMAIIL E SENHA DO INSTAGRAM INFORMADO
    def pegar_email_senha_instagram(self):

        # CATCH MAIL AND PASSWORD OF INSTAGRAM
        file = open('email_senha_instagram.txt', 'r')
        content_file = file.read()
        file.close()

        content = content_file.split('-')

        email = content[0]
        senha = content[1]

        lista = [email, senha]

        return lista


    # ESSA FUNÇÃO INICIA A AUTOMATIZAÇÃO
    def abrir_navegador(self, janela, conteudo, quant_curtidas):

        # VARIABLES
        lista = self.pegar_email_senha_instagram()
        email = lista[0]
        senha = lista[1]

        valor_conteudo = len(conteudo)

        erro = 0
        perfis = 0
        fotos = 0


        # ACESSING INSTAGRAM
        options = Options()
        options.headless = False

        driver = webdriver.Chrome(executable_path='C:\chromedriver.exe', chrome_options=options)
        driver.get('https://www.instagram.com/')

        print('\n')
        
        # PAUSE OF 2 SECONDS
        self.tempo(driver)

        # WRITING THE MAIL AND PASSWORD ON THE BOXES
        driver.find_element(By.NAME, 'username').send_keys(email)
        driver.find_element(By.NAME, 'password').send_keys(senha)
        btn = driver.find_elements(By.TAG_NAME, 'button')
        btn[1].click()

        # PAUSE OF 2 SECONDS
        self.tempo(driver)

        # CLOSING THE BOX OF NOTIFICATIONS
        caixa_inicio = driver.find_elements(By.CLASS_NAME, 'aOOlW.HoLwm')
        caixa_inicio[0].click()
            
        # PAUSE OF 2 SECONDS
        self.tempo(driver)

        i = 0
        j = 0
        while(i < valor_conteudo):
            
            # VERIFICA SE O USUÁRIO NA POSIÇÃO 'i' EXISTE
            erro += 1
            lista_verificar = self.verificar_existencia_usuario(driver, conteudo, i, j)

            j = lista_verificar[0]
            i = lista_verificar[1]

            if i != valor_conteudo-1:

                # PAUSE OF 2 SECONDS
                self.tempo(driver)

                erro += 1
                # CLICKING ON THE FIRST PHOTO
                foto = driver.find_elements(By.CLASS_NAME, 'v1Nh3.kIKUG._bz0w')
                foto[0].click()

                # PAUSE OF 2 SECONDS
                self.tempo(driver) 

                erro += 1
                # LIKE PHOTOS PROCESS
                lista_curtir_fotos = self.curtir_fotos(driver, conteudo, quant_curtidas, perfis, fotos, j)

                j = lista_curtir_fotos[0]
                perfis = lista_curtir_fotos[1]
                quant_fotos_curtidas = lista_curtir_fotos[2]
                
                erro += 1
                # CLOSE THE WINDOW OF PHOTOS
                fechar = driver.find_element_by_xpath('/html/body/div[4]/div[3]/button')
                fechar.click()

                # PAUSE OF 2 SECONDS
                self.tempo(driver)

                erro += 1

            resp = self.verificacao(conteudo)

            # SE ESTIVER NO ÚLTIMO VALOR, A LISTA É ZERADA
            if resp == 'True':

                conteudo = self.remover_usuario(conteudo, -1)

                break

            else:
                
                conteudo = self.remover_usuario(conteudo, i)


            erro = 0
            i += 1


        driver.close()

        self.escrever_resultado(perfis, quant_fotos_curtidas, erro)


    # ESSE MÉTODO INICIA A CLASSE
    def __init__(self):

        pass
