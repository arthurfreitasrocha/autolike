from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from time import sleep
from os import mkdir, getcwd


def loginInstagram(usuario, senha):

    # Acessando Instagram
    driver = webdriver.Edge(executable_path='C:\msedgedriver.exe')
    driver.get("http://www.instagram.com")
    sleep(3)


    # Realizando login
    delay = 3 # seconds
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.NAME, 'username')))
        driver.find_element(By.NAME, 'username').send_keys(usuario)

    except TimeoutException:
        print("AUTOLIKE: Falha ao carregar elemento 'username'.")


    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.NAME, 'password')))
        driver.find_element(By.NAME, 'password').send_keys(senha)

    except:
        print("AUTOLIKE: Falha ao carregar elemento 'passowrd'.")


    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'sqdOP.L3NKy.y3zKF')))
        driver.find_element(By.CLASS_NAME, 'sqdOP.L3NKy.y3zKF').click()

    except:
        print("AUTOLIKE: Falha ao carregar elemento 'sqdOP.L3NKy.y3zKF' (botão para logar).")


    # Verificando se o login foi efetuado
    try:
        myElem = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'slfErrorAlert')))
        driver.find_element(By.ID, 'slfErrorAlert')
        print("AUTOLIKE: Falha no login.")
        driver.close()
        exit(0)

    except:
        print("AUTOLIKE: Sucesso no login")

    sleep(5)

    return driver