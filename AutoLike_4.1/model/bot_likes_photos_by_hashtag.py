# SELENIUM LIBRARY
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

# MODEL
from model.bot_general_options import GeneralOptions

# CONTROLLER
from controller.verify_user_database import VerifyUserDatabase
from controller.file_reader import FileReader
from controller.file_appender import FileAppender

# EXTRA LIBRARY'S
import time
import os

class LikePhotosByHashtag:

    """
    this class like N photos based in the hashtag passed by the user
    """
    def __init__(self, hashtag, n_likes):
        
        self.__hashtag = hashtag
        self.__n_likes = n_likes


    def __startLikePhotos(self):

        " this method verify if the 'moment user' is already liked "
        " if the moment user not is in the database, the same is appended at the database "

        " INSTANCES THE DRIVER "
        driver = self.__driver

        " INSTANCES VARIABLES "
        n_likes = int(self.__n_likes)
        user_instagram = self.__user_instagram

        liked_photos = 0
        while(liked_photos <= n_likes):

            os.system('cls')

            print('\n===== PROGRESS =====')
            print(f'{liked_photos} OF {n_likes} PHOTOS LIKED\n')
            
            " CATCH THE 'MOMENT USER' "
            moment_user = driver.find_element(By.CLASS_NAME, 'sqdOP.yWX7d._8A5w5.ZIAjV').text
            
            " CHECK THE 'MOMENT USER' "
            verify_user_database = VerifyUserDatabase(user_instagram=user_instagram, moment_user=moment_user)
            return_verify_user_database = verify_user_database.startVerifyUserDatabase()

            " IF THE USER IS ALREADY IN THE DATABASE, THE BOT SWITCH TO THE NEXT PHOTO "
            if return_verify_user_database == True:

                print('SKIPPED')

                right_arrow = driver.find_element(By.CLASS_NAME, '_65Bje.coreSpriteRightPaginationArrow')
                right_arrow.click()

                liked_photos -= 1

            else:

                " LIKES THE CURRENT PHOTO AND SWITCH TO THE NEXT PHOTO "
                heart = driver.find_elements(By.CLASS_NAME, 'wpO6b')
                heart[1].click()

                print(f'CURRENT INSTAGRAM PROFILE: {moment_user}')
                print(f'PHOTOS LIKED: {liked_photos}')


                " IF NOT, THE 'MOMENT USER' IS REGISTERED IN THE DATABASE - START "

                " READ THE DATABASE "
                file_directory = f'controller/users/{user_instagram}/database.txt'

                file_reader = FileReader(file_directory=file_directory)
                file_content = file_reader.startFileReader()

                " IF THE DATABASE IS EMPTY, THE 'MOMENT USER' IS INSERTED WITHOUT THE HYPPEN "
                if file_content == '':
                    file_content = moment_user

                else:
                    file_content = f'-{moment_user}'

                file_appender = FileAppender(file_content=file_content, file_directory=file_directory)
                file_appender.startFileAppender()

                " IF NOT, THE 'MOMENT USER' IS REGISTERED IN THE DATABASE - END "


                right_arrow = driver.find_element(By.CLASS_NAME, '_65Bje.coreSpriteRightPaginationArrow')
                right_arrow.click()


            time.sleep(3)

            " INCREMENT THE 'LIKED PHOTO' VAR TO SIGNAL THE NUMBER OF PHOTOS IS ALREADY LIKED "
            liked_photos += 1


    def __startPutTheHashtagAndSelectTheFirstPhoto(self):

        " this method put the hashtag informed by the user in the Instagram 'search input' "
        " after find a corresponding hashtag to the hashtag reported "
        " the bot clicks at the first photo which he can see "

        " INSTANCES THE DRIVER "
        driver = self.__driver

        " INSTANCES THE HASHTAG "
        hashtag = self.__hashtag

        " PUT THE HASHTAG INTO THE SEARCH INPUT "
        search_input = driver.find_elements(By.TAG_NAME, 'input')
        search_input[2].send_keys(hashtag)

        time.sleep(2)

        " CLICK ON THE CORRESPONDING RESULT "
        search_result = driver.find_element(By.CLASS_NAME, 'Ap253')
        search_result.click()

        time.sleep(5)

        first_photo = driver.find_element(By.CLASS_NAME, 'v1Nh3.kIKUG._bz0w')
        first_photo.click()


    def startLikePhotosByHashtag(self):

        " this method like N photos based in the hashtag passed by the user "

        " VARIABLES "
        hashtag = self.__hashtag
        n_likes = self.__n_likes
        error = ''


        " CATCHING THE CURRENT INSTAGRAM USER INFORMATION - START "
        
        " CATCHING THE USER"
        file_directory = 'controller/system_files/user_instagram.txt'

        file_reader = FileReader(file_directory=file_directory)
        self.__user_instagram = file_reader.startFileReader()

        " USER INSTAGRAM "
        user_instagram = self.__user_instagram

        " CATCHING THE PASSWORD "
        file_directory = f'controller/users/{user_instagram}/{user_instagram}.txt'

        file_reader = FileReader(file_directory=file_directory)
        return_file_reader = file_reader.startFileReader()

        password_instagram = return_file_reader.split('-')
        self.__password_instagram = password_instagram[1]

        " PASSWORD INSTAGRAM "
        password_instagram = self.__password_instagram

        " CATCHING THE CURRENT INSTAGRAM USER INFORMATION - END "


        " THE BOT - START "
        general_options = GeneralOptions()

        try:
            " CONFIGURATION "
            driver = general_options.startConfigurationAndAccessTheWebsite()

        except:
            error = 'configuration'

            driver.close()
            return_list = [False, error]
            return return_list

        self.__driver = driver
        driver = self.__driver


        try:

            time.sleep(2)

            try:
                " LOGIN "
                general_options.startLogin(user_instagram=user_instagram, password_instagram=password_instagram)

            except:
                error = 'login'

                driver.close()
                return_list = [False, error]
                return return_list

            time.sleep(3)

            try:
                driver.find_element_by_id('slfErrorAlert')

                error = 'instagram_block'

                driver.close()
                return_list = [False, error]
                return return_list

            except:
                pass

            try:
                " CLOSE THE DIALOG BOXES "
                general_options.startCloseDialogBox()

            except:
                error = 'dialog_boxes'

                driver.close()
                return_list = [False, error]
                return return_list

            time.sleep(2)

            try:
                " PUT THE HASHTAG AND CLICK AT THE FIRST PHOTO "
                self.__startPutTheHashtagAndSelectTheFirstPhoto()

            except:
                error = 'first_photo'

                driver.close()
                return_list = [False, error]
                return return_list

            time.sleep(2)

            self.__startLikePhotos()

            " THE BOT - END "
        except:
            error = 'unknown'

            driver.close()
            return_list = [False, error]
            return return_list

        time.sleep(2)

        driver.close()

        return True