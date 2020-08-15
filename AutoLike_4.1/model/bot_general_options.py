# SELENIUM LIBRARY
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# EXTRA LIBRARY
import time

class GeneralOptions:

    def __init__(self):

        pass


    def startCloseDialogBox(self):

        " this method just closes the dialog boxes that will appear during the bot's execution "

        " INSTANCES THE DRIVER "
        driver = self.__driver

        box_one = driver.find_element(By.CLASS_NAME, 'sqdOP.yWX7d.y3zKF')
        box_one.click()

        time.sleep(3)

        box_two = driver.find_element(By.CLASS_NAME, 'aOOlW.HoLwm')
        box_two.click()


    def startLogin(self, user_instagram, password_instagram):

        " this method login the user in the Instagram "

        " INSTANCES THE DRIVER "
        driver = self.__driver

        " INSTANCES THE VARIABLES "
        user_instagram = user_instagram
        password_instagram = password_instagram

        " WRITE THE USER EMAIL AND THE USER PASSWORD IN THE ENTRIES "
        driver.find_element(By.NAME, 'username').send_keys(user_instagram)
        driver.find_element(By.NAME, 'password').send_keys(password_instagram)

        " SEARCH AND CLICK IN THE LOGIN BUTTON "
        login_button = driver.find_elements(By.TAG_NAME, 'button')
        login_button[1].click()


    def startConfigurationAndAccessTheWebsite(self):

        " this method configures the Selenium and access the Instagram "

        " CONFIGURATION "
        options = Options()
        options.headless = False
        self.__driver = webdriver.Chrome(executable_path='C:\chromedriver.exe', chrome_options=options)
        driver = self.__driver

        " ACCESS THE INSTAGRAM "
        driver.get('https://www.instagram.com/')

        return driver
