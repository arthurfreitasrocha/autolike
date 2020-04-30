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


class CapturarInformacoes:

    # THIS METHOD WRITE IN A .TXT DOCUMENT THE RESULT OF THE PROCESS
    def escrever_resultado(self, erro):

        if erro < 1:

            file = open('informacoes.txt', 'w')
            file.write('1-{}'.format(erro))
            file.close()


            m = 0
            n = 0
            for 

            file = open('curtir_fotos_usuarios_aleatorio.txt', 'w')
            file.write()
            file.close()

        else:

            file = open('informacoes.txt', 'w')
            file.write('0-{}'.format(perfis, fotos, erro))
            file.close()

    # THIS METHOD PAUSE THE PROGRAM IN 2 SECONDS
    def tempo(self, driver):

        tempo = 2

        time.sleep(tempo)
        driver.implicitly_wait(10)


    # THIS METHOD REMOVE THE INFORMED USERS FROM THE LIST
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


    # THIS METHOD CHECKS IF THE USER 'x' HAS THE PREREQUISITES TO LIKE HIM PUBLICATIONS
    def verificacao_interna_usuario(self, driver, quant_curtidas):

        lista = ['', 0]

        temp = driver.find_elements_by_class_name('g47SY')
        quant_publicacoes_usuario = temp[0].text
        temp = ''

        i = 0
        for letra in quant_publicacoes_usuario:

            if quant_publicacoes_usuario[i] == '.':

                temp += quant_publicacoes_usuario[i]

            i += 1

        quant_publicacoes_usuario = int(temp)
        lista[0] = quant_publicacoes_usuario
  
        if quant_curtidas <= quant_publicacoes_usuario:

            lista[1] = 'True'

        else:

            lista[1] = 'False'


        return lista


    # THIS METHOD CHECKS IF THE USER 'x' EXIST
    def verificar_existencia_usuario(self, driver, conteudo, indice, cont):

        j = cont
        valor_conteudo = len(conteudo)
        while(j < valor_conteudo):
            
            # TRY TO INSERT THE 'i' ITEM IN THE LIST
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


    # THIS METHOD CATCH THE MAIL AND PASSWORD OF THE INFORMED INSTAGRAM
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

    
    # THIS METHOD START THE AUTOMATIZATION
    def abrir_navegador(self, janela, conteudo, quant_curtidas):

        # VARIABLES
        lista = self.pegar_email_senha_instagram()
        email = lista[0]
        senha = lista[1]

        valor_conteudo = len(conteudo)

        erro = 0
        perfis = 0
        quant_fotos_curtidas = 0
        self.conteudo2 = [[], []]


        # ACESSING INSTAGRAM
        options = Options()
        options.headless = True

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
            
            # CHECK IF THE USER 'x' EXIST
            erro += 1
            lista_verificar = self.verificar_existencia_usuario(driver, conteudo, i, j)

            j = lista_verificar[0]
            i = lista_verificar[1]

            # PAUSE OF 2 SECONDS
            self.tempo(driver)

            retorno_verificacao_interna_usuario = self.verificacao_interna_usuario(driver, quant_curtidas)
            rvi = retorno_verificacao_interna_usuario

            if rvi[1] == 'True':
                
                self.conteudo2[i][0] = conteudo[i]
                self.conteudo2[i][1] = rvi[0]

                j += 1

            # IF IS THE LAST VALUE, THE LIST IS CLEARED
            if conteudo == '':

                break


            erro = 0
            i += 1


        driver.close()

        self.escrever_resultado(erro)


    # CONSTRUCTOR METHOD
    def __init__(self):

        pass


class CurtirFotosEscolhaBancoDeDadosAcessarInstagram:

    # THIS METHOD WRITE IN A .TXT DOCUMENT THE RESULT OF THE PROCESS
    def escrever_resultado(self, perfis, fotos, erro):

        if erro < 1:

            file = open('informacoes.txt', 'w')
            file.write('1-{}-{}-{}'.format(perfis, fotos, erro))
            file.close()

        else:

            file = open('informacoes.txt', 'w')
            file.write('0-{}-{}-{}'.format(perfis, fotos, erro))
            file.close()


    # THIS METHOD PAUSE THE PROGRAM IN 2 SECONDS
    def tempo(self, driver):

        tempo = 2

        time.sleep(tempo)
        driver.implicitly_wait(10)


    # THIS METHOD CHECK IF ALL THE USERS ALREADY LIKED
    def verificacao_conteudo(self, conteudo):
        
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


    # THIS METHOD REMOVE THE INFORMED USERS FROM THE LIST
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


    # THIS METHOD LIKE THE PHOTOS OF THE USER 'x'
    def curtir_fotos(self, driver, conteudo, quant_curtidas, perfis, fotos, cont):

        print('PERFIL SENDO ACESSADO: {}'.format(conteudo[cont]))
        i = 0
        while(i < quant_curtidas):

            if i == quant_curtidas-1:
                
                try:

                    coracao = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button')
                    coracao.click()

                except:

                    messagebox.showerror('Algo deu errado', 'Falha ao tentar curtir')

            else:
                
                try:

                    coracao = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button')
                    coracao.click()

                except:

                    messagebox.showerror('Algo deu errado', 'Falha ao tentar curtir')

                try:

                    seta_direita = driver.find_elements(By.CLASS_NAME, '_65Bje.coreSpriteRightPaginationArrow')
                    seta_direita[0].click()

                except:

                    messagebox.showerror('Algo deu errado', 'Falha ao tentar passar para próxima publicação')

            # PAUSE OF 2 SECONDS
            self.tempo(driver)

            i += 1
            fotos += 1

            print('{} FOTO(S) CURTIDA(S) DE {}'.format(i, conteudo[cont]))

        print('====================')

        # CHECKS IF THE ACTUAL VALUE IS THE LAST
        resp = self.verificacao_conteudo(conteudo)

        # IF IS THE LAST VALUE, THE LIST IS CLEARED
        if resp == 'True':

            conteudo = self.remover_usuario(conteudo, -1)

        else:
                    
            conteudo = self.remover_usuario(conteudo, i)


        perfis += 1
        cont += 1

        lista = [cont, perfis, fotos, conteudo]

        return lista

    
    # THIS METHOD CHECKS IF THE USER 'x' HAS THE PREREQUISITES TO LIKE HIM PUBLICATIONS
    def verificacao_interna_usuario(self, driver, quant_curtidas):

        lista = ['', '']

        # CHECKS IF THE USER ACCOUNT IS PRIVATE
        try:

            conta_privada = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/article/div[1]/div/h2').text
        
            if conta_privada == 'Esta conta é privada':
                
                lista[0] = 'True'
        
        except:

            lista[0] = 'False'


        temp = driver.find_elements_by_class_name('g47SY')
        quant_publicacoes_usuario = temp[0].text
        temp = ''

        i = 0
        for letra in quant_publicacoes_usuario:

            if quant_publicacoes_usuario[i] == '.':

                temp += quant_publicacoes_usuario[i]

            i += 1

        quant_publicacoes_usuario = int(temp)

  
        if quant_curtidas <= quant_publicacoes_usuario:

            lista[1] = 'True'

        else:

            lista[1] = 'False'


        return lista


    # THIS METHOD CHECKS IF THE USER 'x' EXIST
    def verificar_existencia_usuario(self, driver, conteudo, indice, cont):

        j = cont
        valor_conteudo = len(conteudo)
        while(j < valor_conteudo):
            
            # TRY TO INSERT THE 'i' ITEM IN THE LIST
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


    # THIS METHOD CATCH THE MAIL AND PASSWORD OF THE INFORMED INSTAGRAM
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


    # THIS METHOD START THE AUTOMATIZATION
    def abrir_navegador(self, janela, conteudo, quant_curtidas):

        # VARIABLES
        lista = self.pegar_email_senha_instagram()
        email = lista[0]
        senha = lista[1]

        valor_conteudo = len(conteudo)

        erro = 0
        perfis = 0
        quant_fotos_curtidas = 0


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
            
            # CHECK IF THE USER 'x' EXIST
            erro += 1
            lista_verificar = self.verificar_existencia_usuario(driver, conteudo, i, j)

            j = lista_verificar[0]
            i = lista_verificar[1]

            # PAUSE OF 2 SECONDS
            self.tempo(driver)

            retorno_verificacao_interna_usuario = self.verificacao_interna_usuario(driver, quant_curtidas)
            rvi = retorno_verificacao_interna_usuario

            if (rvi[0] == 'True' and rvi[1] == 'False') or (rvi[0] == 'True' and rvi[1] == 'True'):
                
                print('O USUÁRIO {} NÃO PASSOU NOS CRITÉRIOS DO TESTE DE VERIFICAÇÃO'.format(conteudo[i]))

                j += 1

            else:

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
                lista_curtir_fotos = self.curtir_fotos(driver, conteudo, quant_curtidas, perfis, quant_fotos_curtidas, j)

                j = lista_curtir_fotos[0]
                perfis = lista_curtir_fotos[1]
                quant_fotos_curtidas = lista_curtir_fotos[2]
                conteudo = lista_curtir_fotos[3]
                    
                erro += 1
                # CLOSE THE WINDOW OF PHOTOS
                fechar = driver.find_element_by_xpath('/html/body/div[4]/div[3]/button')
                fechar.click()

                # PAUSE OF 2 SECONDS
                self.tempo(driver)

                erro += 1


            # IF IS THE LAST VALUE, THE LIST IS CLEARED
            if conteudo == '':

                break


            erro = 0
            i += 1


        driver.close()

        self.escrever_resultado(perfis, quant_fotos_curtidas, erro)


    # THIS METHOD START THE CLASS
    def __init__(self):

        pass
