from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from time import sleep
from os import system
from random import randint


def __incrementarBD(usuario, profile_user):

    # Lendo diretório raiz
    with open('Bot\\diretorio_raiz.txt', 'r') as f:
        diretorio_raiz = f.read()

    # Adicionando profile_user ao Banco de Dados

    # # Verificando se o arquivo está vazio
    diretorio_usuario = f'{diretorio_raiz}\\Users\\{usuario}\\database.txt'
    with open(diretorio_usuario, 'r') as f:
        database = f.read()


    # # Se o arquivo estiver vazio o usuário é adicionado
    if database == '':
        with open(diretorio_usuario, 'a') as f:
            f.write(profile_user)

    # # # Verifica se o usuário já está no Banco de Dados, caso não esteja ele é adicionado.
    else:
        database_splitted = database.split('-')
        user_in_database = False

        for user_saved in database_splitted:
            if profile_user == user_saved:
                user_in_database = True
                print(f"AUTOLIKE: {profile_user} já armazenado no Banco de Dados")

        if user_in_database == False:
            print(f"AUTOLIKE: Adicionando {profile_user} ao Banco de Dados")
            conteudo = f'-{profile_user}'
            with open(diretorio_usuario, 'a') as f:
                f.write(conteudo)

        sleep(2)
        return user_in_database


def __acessarPagina(driver, link):

    # Acessa a página da Hashtag
    print(f"AUTOLIKE: Acessando página: {link}")
    driver.get(link)

    # Abrindo primeira publicação do Instagram
    sleep(2)
    delay = 3 # seconds
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'v1Nh3.kIKUG._bz0w')))
        publicacao = driver.find_elements(By.CLASS_NAME, 'v1Nh3.kIKUG._bz0w')
        publicacao[0].click()

    except TimeoutException:
        print("AUTOLIKE: Falha ao clicar no elemento 'v1Nh3.kIKUG._bz0w' (primeira publicação da hashtag).")


def iniciarProcesso(driver, usuario, hashtag, perfis, comentario):

    link = f'https://www.instagram.com/explore/tags/{hashtag}/'
    __acessarPagina(driver, link)

    sleep(2)
    delay = 3 # seconds
    usuarios_gerais = 0
    usuarios_acessados = 0
    while(usuarios_acessados < perfis):

        system("cls")
        print("===== PROGRESSO =====")
        print(f"{usuarios_acessados} de {perfis} perfis acessados\n")

        # Capturando e armazenando nome de usuário
        try:
            myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'sqdOP.yWX7d._8A5w5.ZIAjV')))
            profile_user = driver.find_element(By.CLASS_NAME, 'sqdOP.yWX7d._8A5w5.ZIAjV').text

        except TimeoutException:
            print("AUTOLIKE: Falha ao capturar o elemento 'sqdOP.yWX7d._8A5w5.ZIAjV' (nome de usuário).")

        user_in_database = __incrementarBD(usuario, profile_user)


        if user_in_database == True:
            # Clicando na seta para avançar
            print(f"AUTOLIKE: Indo para próximo usuário...")
            sleep(2)
            driver.find_element(By.CLASS_NAME, '_65Bje.coreSpriteRightPaginationArrow').click()
            usuarios_gerais += 1

        else:
            # Armazenando URL atual
            link = f'https://www.instagram.com/explore/tags/{hashtag}/'

            # Entrando no perfil do usuário
            driver.find_element(By.CLASS_NAME, 'sqdOP.yWX7d._8A5w5.ZIAjV').click()

            print(f"\nAUTOLIKE: Acessando perfil de {profile_user}...")
            sleep(2)
            curtirPublicacoes(driver, comentario)
            usuarios_acessados += 1
            usuarios_gerais += 1

            if usuarios_acessados < perfis:

                # Acessa a página da Hashtag
                __acessarPagina(driver, link)

                # Vai para a última publicação
                print("AUTOLIKE: Avançando para a última publicação")
                i = 0
                while(i < usuarios_gerais):
                    try:
                        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, '_65Bje.coreSpriteRightPaginationArrow')))
                        right_arrow = driver.find_element(By.CLASS_NAME, '_65Bje.coreSpriteRightPaginationArrow').click()

                    except TimeoutException:
                        print("AUTOLIKE: Falha ao clicar no elemento '_65Bje.coreSpriteRightPaginationArrow' (flecha apontando para a direita).")

                    sleep(2)
                    i += 1


def curtirPublicacoes(driver, comentario):

    # Capturando quant. de publicações do usuário
    sleep(5)
    delay = 3 # seconds
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'g47SY')))
        user_publications = driver.find_element(By.CLASS_NAME, 'g47SY').text

    except TimeoutException:
        print("AUTOLIKE: Falha ao capturar o elemento 'g47SY' (quant. publicações usuário).")


    # Tratamento de erro caso o número possua caracteres inválidos
    numero = ''

    for caracter in user_publications:
        if caracter != '.':
            numero += caracter

    user_publications = int(numero)


    # Verifica se o usuário possui pelo menos 10 publicações
    if user_publications < 10:
        print("AUTOLIKE: O usuário atual não possui a quantidade mínima de publicações.")

    else:
        # Clica na primeira publicação do usuário
        try:
            myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'eLAPa')))
            user_publications = driver.find_element(By.CLASS_NAME, 'eLAPa').click()

        except TimeoutException:
            print("AUTOLIKE: Falha ao clicar no elemento 'eLAPa' (primeira publicação do usuário).")


        # Verifica se o perfil é bloqueado para publicações, se sim, ele ignora o perfil, se não, ele curte as fotos e comenta
        try:
            myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, '_7UhW9.xLCgt.MMzan.mDXrS.uL8Hv.l4b0S')))
            print("AUTOLIKE: Este perfil está bloqueado para escrever comentários. Pulando ele.")

        except TimeoutException:

            # Armazena numa lista as fotos que serão curtidas
            sleep(3)
            posicao = 0
            random_publications = []
            i = 0
            while(i < 3):

                valor_aleatorio = randint(0,9)
                if i == 0:
                    random_publications.append(valor_aleatorio)
                    i += 1

                else:
                    if valor_aleatorio in random_publications:
                        continue
                    else:
                        random_publications.append(valor_aleatorio)
                        i += 1


            # Loop para avançar ou regredir nas publicações
            for item in random_publications:

                while(posicao != item):

                    if item > posicao:
                        try:
                            myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, '_65Bje.coreSpriteRightPaginationArrow')))
                            right_arrow = driver.find_element(By.CLASS_NAME, '_65Bje.coreSpriteRightPaginationArrow').click()

                        except TimeoutException:
                            print("AUTOLIKE: Falha ao clicar no elemento '_65Bje.coreSpriteRightPaginationArrow' (flecha apontando para a direita).")

                        posicao += 1
                    else:
                        try:
                            myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'ITLxV.coreSpriteLeftPaginationArrow')))
                            right_arrow = driver.find_element(By.CLASS_NAME, 'ITLxV.coreSpriteLeftPaginationArrow').click()

                        except TimeoutException:
                            print("AUTOLIKE: Falha ao clicar no elemento 'ITLxV.coreSpriteLeftPaginationArrow' (flecha apontando para a esquerda).")

                        posicao -= 1

                    sleep(2)


                # Curte a publicação
                sleep(3)
                try:
                    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'wpO6b')))
                    heart = driver.find_element(By.CLASS_NAME, 'fr66n').find_element(By.CLASS_NAME, 'wpO6b')
                    heart.click()

                except TimeoutException:
                    print("AUTOLIKE: Falha ao clicar no elemento 'wpO6b' (coração).")


                # Caso seja a última publicação, será feito um comentário
                sleep(3)
                if item == random_publications[-1]:
                    driver.find_element(By.CLASS_NAME, 'Ypffh').click()
                    sleep(2)

                    for caracter in comentario:
                        sleep(randint(0, 1))
                        driver.find_element(By.CLASS_NAME, 'Ypffh').send_keys(caracter)

                    sleep(2)
                    #driver.find_element(By.CLASS_NAME, 'sqdOP.yWX7d.y3zKF').click()


            print("AUTOLIKE: 3 (três) publicações curtidas e 1 (um) comentário realizado com sucesso!")
