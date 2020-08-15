# SELENIUM LIBRARY
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

# MODEL
from model.bot_general_options import GeneralOptions
from model.clear_user_publications import ClearUserPublications

# CONTROLLER
from controller.verify_user_database import VerifyUserDatabase
from controller.file_reader import FileReader
from controller.file_writer import FileWriter

# EXTRA LIBRARY'S
from random import *
import time
import os

class LikePhotosByUsers:

    def __init__(self, users_selected, kind_likes, n_photos):
        
        """
        this class one by one Instagram profile and likes a X number of photos
        """

        self.__users_selected = users_selected
        self.__kind_likes = kind_likes
        self.__n_photos = n_photos


    def __startUpdateSecondDatabase(self, current_user):

        " INSTANCES THE CURRENT INSTAGRAM USER "
        current_user = current_user

        " CATCH THE CURRENT PROGRAM USER "
        file_directory = 'controller/system_files/user_instagram.txt'

        file_reader = FileReader(file_directory=file_directory)
        file_content = file_reader.startFileReader()

        user = file_content


        " UPDATES THE SECOND DATABASE - START "

        " READ THE SECOND DATABASE"
        file_directory = f'controller/users/{user}/second_database.txt'

        file_reader = FileReader(file_directory=file_directory)
        file_content = file_reader.startFileReader()

        second_database = file_content.split('-')

        " REMOVE THE CURRENT INSTAGRAM USER FROM THE SECOND DATABASE "
        second_database.remove(current_user)

        " CREATES THE SECOND DATABASE STRING WHICH WILL BE WRITTED IN THE SECOND DATABASE FILE "
        second_database_text = ''
        count_user = 0
        for instagram_user in second_database:

            instagram_user_text = f'-{instagram_user}'

            if count_user == 0:
                second_database_text += instagram_user

            else:
                second_database_text += instagram_user_text

            count_user += 1

        " WRITE THE NEW SECOND DATABASE FILE "
        file_directory = file_directory = f'controller/users/{user}/second_database.txt'
        file_content = second_database_text

        file_writer = FileWriter(file_content=file_content, file_directory=file_directory)
        file_writer.startFileWriter()

        " UPDATES THE SECOND DATABASE - END "


        " UPDATES THE USERS SELECTED - START "
        
        " VARIABLE WHICH CATCH THE REMAINING NUMBER OF USERS "
        n_second_database = len(second_database)
        
        if n_second_database > 0:
            file_content = f'{n_second_database} users selected'
        
        else:
            file_content = 'Here will appear\nthe number of selected users'

        file_directory = 'controller/system_files/option_two/n_selected_users.txt'

        file_writer = FileWriter(file_content=file_content, file_directory=file_directory)
        file_writer.startFileWriter()

        " UPDATES THE USERS SELECTED - END "


    def __startLikesRandomUserPublications(self, photos_randomized):

        " this method likes random users photos "

        " INSTANCES THE DRIVER "
        driver = self.__driver
        
        " INSTANCES VARIABLES "
        photos_randomized = photos_randomized # STORES THE LIST OF PHOTOS WHICH WILL BE LIKED

        " OPEN THE FIRS PUBLICATION "
        first_publication = driver.find_elements(By.CLASS_NAME, 'v1Nh3.kIKUG._bz0w')
        first_publication[0].click()

        current_position = 0
        photos_liked = 0
        " LOOP WHICH LIKES THE INSTAGRAM USER PUBLICATIONS"
        for current_photo in photos_randomized:

            " GOES TO THE SELECTED PUBLICATION - START "

            count_position = 0 # CONTROLS THE LIKES FLOW
            if current_position != current_photo:

                while(True):

                    if current_position == current_photo:
                        break

                    if current_position > current_photo:
                        current_position -= 1
                        count_position -= 1

                    else:
                        current_position += 1
                        count_position += 1


            if count_position != 0:

                while(True):

                    if count_position == 0:
                        break

                    elif count_position > 0:
                        right_arrow = driver.find_elements(By.CLASS_NAME, '_65Bje.coreSpriteRightPaginationArrow')
                        right_arrow[0].click()

                        count_position -= 1

                    elif count_position < 0:
                        left_arrow = driver.find_elements(By.CLASS_NAME, 'ITLxV.coreSpriteLeftPaginationArrow')
                        left_arrow[0].click()

                        count_position += 1

                    time.sleep(1)

            " GOES TO THE SELECTED PUBLICATION - END "

            time.sleep(1)

            heart = driver.find_elements(By.CLASS_NAME, 'wpO6b')
            heart[2].click()

            photos_liked += 1

            print(f'PHOTOS LIKED: {photos_liked}')

        print('')

        close_window = driver.find_element_by_xpath('/html/body/div[4]/div[3]/button')
        close_window.click()


    def __startRandomizePublications(self, n_user_publications, n_photos):

        " this method randomize the photos will be liked "

        " VARIABLES "
        n_user_publications = int(n_user_publications) # STORES THE NUMBER OF PUBLICATIONS WHAT THE CURRENT INSTAGRAM USER HAS
        n_photos = int(n_photos) # STORES THE NUMBER OF PHOTOS WILL BE LIKED OF EACH INSTAGRAM USER
        random_publications = [] # STORES THE INDEX OF THE PUBLICATIONS WHICH WILL BE LIKED

        if n_user_publications > 10:
            n_user_publications = 10


        " PUT THE RANDOM VALUES IN THE 'random_publications' LIST "
        i = 0
        while(i < n_photos):

            " CATCH A RANDOM VALUE"
            random_value = randrange(0, n_user_publications)


            " VERIFY IF EXISTS A REPEATED VALUE IN THE LIST - START "
            verify_repeated_value = 0
            if i > 0:

                for value in random_publications:

                    if value == random_value:
                        verify_repeated_value = 1
                        break

            " VERIFY IF EXISTS A REPEATED VALUE IN THE LIST - END "


            " IF THE VAR 'verify_repeated_value' IS SETTED TO '1' "
            " IT MEANS THE RANDOM VALUE IS ALREADY IN THE LIST "
            " THEN THE INCREMENTOR IS DECREMENTED AND THE LOOP IS REPEATED "
            if verify_repeated_value == 1:
                i -= 1

            else:
                " IF NOT, THE RANDOM VALUE IS APPENDED IN THE 'random_publications' LIST "
                random_publications.append(random_value)

            i += 1

        return random_publications


    def __startIndividualUserValidation(self, current_user):

        " this method verify if the 'current user' has the prerequisites to like him publications "

        " INSTANCES THE DRIVER "
        driver = self.__driver

        " VARIABLES "
        current_user = current_user # STORES THE CURRENT USER
        n_photos = int(self.__n_photos) # STORES THE NUMBER OF PHOTOS
        validation = [True, True] # VERIFY THE USER CONDITIONS

        " CHECKS IF THE USER ACCOUNT IS PRIVATE "
        try:
            private_account = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/article/div[1]/div/h2').text
        
            if private_account == 'Esta conta é privada':
                validation[0] = False
        
        except:
            pass


        " VARIABLE WHICH CATCH THE NUMBER OF PUBLICATIONS WHICH THE 'current user' HAVES"
        current_user_publications = driver.find_elements_by_class_name('g47SY')
        current_user_publications = current_user_publications[0].text


        " CLEAR THE STRING WHICH HAVE THE NUMBER OF PUBLICATIONS WHAT THE INSTAGRAM USER HAS "
        clear_user_publications = ClearUserPublications(n_user_publications=current_user_publications)
        n_user_publications = clear_user_publications.startClearUserPublications()


        " VERIFY IF THE NUMBER OF PHOTOS PASSED BY THE PROGRAM USER "
        " IS LESS OR EQUAL THE NUMBER OF PUBLICATIONS WHAT THE INSTAGRAM USER HAS "
        if not n_photos <= n_user_publications:
            validation[1] = False


        " IF ALL CONDITIONS ARE SATISFIED, THE 'n_user_publications' IS RETURNED "
        if validation[0] == True and validation[1] == True:
            return n_user_publications

        else:
            return False


    def __startVerifyUserExistence(self, current_user):

        " this method verify if the 'current user' already exists "

        " INSTANCES THE DRIVER "
        driver = self.__driver

        " VARIABLE WHICH WILL STORESS THE CURRENT USER "
        current_user = current_user

        " TRY TO FIND IN INSTAGRAM THE CURRENT USER "
        try:

            " PUT THE CURRENT USER IN THE INSTAGRAM INPUT "
            search_input = driver.find_element(By.CLASS_NAME, 'XTCLo.x3qfX')
            search_input.clear()
            search_input.send_keys(current_user)

            time.sleep(2)

            " CLICK ON THE CORRESPONDING RESULT "
            search_result = driver.find_element(By.CLASS_NAME, 'Ap253')
            search_result.click()

        except:

            return False

        return True


    def startLikesPhotosByUsers(self):

        " this method likes N photos in N instagram users selecteds by the program user "

        " VARIABLE "
        users_selected = self.__users_selected # STORES THE USERS WHO WILL HAVE THEIR PHOTOS LIKED
        n_photos = self.__n_photos # STORES THE NUMBER OF PHOTOS

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

            time.sleep(2)

            try:
                " CLOSE THE DIALOG BOXES "
                general_options.startCloseDialogBox()

            except:
                error = 'dialog_boxes'

                driver.close()
                return_list = [False, error]
                return return_list

            time.sleep(2)

            profiles = 0
            for user in users_selected:

                os.system('cls')

                print('\n===== PROGRESS =====')
                print(f'{profiles} OF {len(users_selected)} PROFILES ACCESSED\n')

                print(f'CURRENT INSTAGRAM PROFILE: {user}')

                try:
                    " VERIFY IF THE 'user' EXISTS "
                    return_verify_user = self.__startVerifyUserExistence(current_user=user)

                except:
                    continue

                time.sleep(2)

                try:
                    " IF THE 'user' EXISTS, THE PROGRAM VERIFY SOME CONDITIONS "
                    return_individual_user_validation = ''
                    if return_verify_user == True:
                        return_individual_user_validation = self.__startIndividualUserValidation(current_user=user)

                except:
                    continue

                try:
                    " IF THE 'return_individual_user_validation' RETURNS THE NUMBER OF "
                    " PUBLICATIONS OF THE USER, THE PROGRAM CATCH THIS NUMBER AND USE IT "
                    " TO RANDOMIZE THE PUBLICATIONS WHICH WILL BE LIKED "
                    photos_randomized = ''
                    if return_individual_user_validation != False and return_individual_user_validation != '':
                        n_user_publications = return_individual_user_validation # CONTAINS THE NUMBER OF PUBLICATIONS
                                                                                # WHAT THE INSTAGRAM USER HAS
                        photos_randomized = self.__startRandomizePublications(n_photos=n_photos, n_user_publications=n_user_publications)
                
                except:
                    error = 'individual_user_validation'

                    driver.close()
                    return_list = [False, error]
                    return return_list

                time.sleep(2)

                if photos_randomized != '':
                    try:
                        " LIKES THE PHOTOS IN EACH INSTAGRAM USER PROFILE "
                        self.__startLikesRandomUserPublications(photos_randomized=photos_randomized)

                    except:
                        error = 'likes_random_publications'

                        driver.close()
                        return_list = [False, error]
                        return return_list

                    try:
                        " UPDATES THE SECOND DATABASE "
                        " REMOVING THE USERS IS ALREADY LIKED "
                        self.__startUpdateSecondDatabase(current_user=user)
                    
                    except:
                        error = 'update_second_database'

                        driver.close()
                        return_list = [False, error]
                        return return_list

                profiles += 1

                time.sleep(2)

            " THE BOT - END "
        except:
            error = 'unknown'

            driver.close()
            return_list = [False, error]
            return return_list

        time.sleep(2)

        driver.close()

        return True

