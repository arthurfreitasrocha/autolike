# SELENIUM LIBRARY
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

# EXTRA LIBRARY'S
import time
import os

class VerifyInstagramUser:

    """
    this class verify if the Instagram credentials informed are valids
    """
    def __init__(self, user_login, user_password):
        
        self.__user_login = user_login
        self.__user_password = user_password


    def startVerifyInstagramUser(self):

        " this method verify if the instagram user account is valid "

        " VARIABLES "
        user_login = self.__user_login
        user_password = self.__user_password

        " CONFIGURATION "
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(executable_path='C:\chromedriver.exe', chrome_options=options)

        os.system('cls')
        print('===== PROGRESS =====\n')

        print('ACESSING INSTAGRAM\n')

        " ACCESS THE INSTAGRAM "
        driver.get('https://www.instagram.com/')

        time.sleep(2)

        print(f'TRYING TO LOGIN INTO [{user_login}] INSTAGRAM ACCOUNT')
        print('DESCRIPTION: THE LOGIN IS NECESSARY TO VERIFY YOUR INSTAGRAM ACCOUNT\n')

        " WRITE THE USER EMAIL AND THE USER PASSWORD IN THE ENTRIES "
        driver.find_element(By.NAME, 'username').send_keys(user_login)
        driver.find_element(By.NAME, 'password').send_keys(user_password)

        " SEARCH AND CLICK IN THE LOGIN BUTTON "
        login_button = driver.find_elements(By.TAG_NAME, 'button')
        login_button[1].click()

        time.sleep(5)

        try:
            
            " TRY TO FIND THE ERROR MESSAGE "
            invalid_account = driver.find_element_by_id('slfErrorAlert')
            print(f'FAILED TO LOGIN INTO [{user_login}] INSTAGRAM ACCOUNT')

            " CLOSES THE DRIVER "
            driver.close()
                
            " IF THE PROGRAM FIND THE ERROR MESSAGE, THE LOGIN FAILED "
            return False

        except:

            print(f'LOGGED INTO [{user_login}] INSTAGRAM ACCOUNT WITH SUCCESS')

            " CLOSES THE DRIVER "
            driver.close()

            " IF NOT, THE INSTAGRAM LOGIN WILL BE A SUCCESS "
            return True
