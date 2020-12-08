# SELENIUM LIBRARY
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# MODEL
from model.clear_user_publications import ClearUserPublications

# CONTROLLER
from controller.verifications import VerifyUserDatabase
from controller.file_manipulator import FileReader
from controller.file_manipulator import FileWriter
from controller.file_manipulator import FileAppender

# EXTRA LIBRARY'S
from random import randrange
import time
import os

class GeneralOptions:

    def __init__(self, driver, user_instagram, password_instagram):

        " INSTANCES THE VARIABLES "
        user_instagram = user_instagram
        password_instagram = password_instagram

        first_return = False
        second_return = False
        third_return = False

        self.__driver = driver


        " ACCESS THE INSTAGRAM WEBSITE "
        first_return = self.__startAccessTheWebsite()

        time.sleep(2)

        " EACH ACTION JUST WILL CONTINUE IF THE PREVIOUS ACTION RETURNS TRUE "
        if first_return == True:

            " DOES LOGIN IN INSTAGRAM "
            second_return = self.__startLogin(user_instagram, password_instagram)


        time.sleep(2)

        if second_return == True:

            " CLOSES THE BORING DIALOG BOXES "
            third_return = self.__startCloseDialogBox()


        " IF ALL ACTION RETURNS TRUE, THE FINAL RETURN IS WRITTED - IF NOT, ALL THE RETURNS OF EACH ACTION WILL BE WRITTEN "
        if first_return == True and second_return == True and third_return == True:

            " WRITE THE RETURN OF FINAL RETURN "
            file_directory = 'controller/communication_file/return_bot.txt'
            file_content = 'True'

            file_writer = FileWriter(file_content, file_directory)
            file_writer.startFileWriter()

        else:

            returns = [
                first_return,
                second_return,
                third_return
            ]

            for each_return in returns:
                if each_return == True:
                    each_return = 'True'

                else:
                    each_return = 'False'


            " WRITE THE RETURN OF FINAL RETURN "
            file_directory = 'controller/communication_file/return_bot.txt'
            file_content = f'{first_return}-{second_return}-{third_return}'

            file_writer = FileWriter(file_content, file_directory)
            file_writer.startFileWriter()


    def __startCloseDialogBox(self):

        " this method just closes the dialog boxes that will appear during the bot's execution "

        try:

            " INSTANCES THE WEBDRIVER "
            driver = self.__driver

            box_one = driver.find_element(By.CLASS_NAME, 'sqdOP.yWX7d.y3zKF')
            box_one.click()

            time.sleep(3)

            box_two = driver.find_element(By.CLASS_NAME, 'aOOlW.HoLwm')
            box_two.click()

            return True

        except:

            return False


    def __startLogin(self, user_instagram, password_instagram):

        " this method login the user in the Instagram "

        try:

            " INSTANCES THE WEBDRIVER "
            driver = self.__driver
            delay = 3

            " INSTANCES THE VARIABLES "
            user_instagram = user_instagram
            password_instagram = password_instagram

            " WRITE THE USER EMAIL AND THE USER PASSWORD IN THE ENTRIES "
            try:
                myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.NAME, 'username')))
            
            except TimeoutException:
                return False

            driver.find_element(By.NAME, 'username').send_keys(user_instagram)
            driver.find_element(By.NAME, 'password').send_keys(password_instagram)

            time.sleep(2)

            " SEARCH AND CLICK IN THE LOGIN BUTTON "
            login_button = driver.find_elements(By.TAG_NAME, 'button')
            login_button[1].click()

            try:

                driver.find_element_by_id('slfErrorAlert')

                return False

            except:

                return True

        except:

            return False


    def __startAccessTheWebsite(self):

        " this method access the Instagram "

        try:

            " INSTANCES THE DRIVER "
            driver = self.__driver

            " ACCESS THE INSTAGRAM "
            driver.get('https://www.instagram.com/')

            return True

        except:

            return False


class GeneralOptionsInstagramUser:

    def __init__(self, driver, option, **kws):

        " INSTANCES THE VARIABLES "
        self.__driver = driver
        self.__option = option
        self.__user = kws.get('user')
        self.__n_photos = kws.get('n_photos')


    def __startIndividualUserValidation(self, current_user, n_photos):

        " this method verify if the 'current user' has the prerequisites to like him publications "

        " INSTANCES THE DRIVER "
        driver = self.__driver

        " VARIABLES "
        current_user = current_user # STORES THE CURRENT USER
        n_photos = int(n_photos) # STORES THE NUMBER OF PHOTOS
        validation = [True, True] # VERIFY THE USER CONDITIONS

        " CHECKS IF THE USER ACCOUNT IS PRIVATE "
        try:
            private_account = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/article/div[1]/div/h2').text
        
            if private_account == 'Esta conta é privada':
                validation[0] = False
        
        except:
            pass


        " VARIABLE WHICH CATCH THE NUMBER OF PUBLICATIONS WHICH THE 'current user' HAVES "
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


    def returnOption(self):

        " INSTANCES THE OPTION "
        option = self.__option

        if option == 1:

            " INSTANCES THE USER "
            user = self.__user

            " CALLS THE METHOD "
            return_option = self.__startVerifyUserExistence(user)
            return return_option

        elif option == 2:

            " INSTANCES THE USER "
            user = self.__user
            n_photos = self.__n_photos

            " CALLS THE METHOD "
            return_option = self.__startIndividualUserValidation(user, n_photos)
            return return_option


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

        time.sleep(2)

        " SEARCH AND CLICK IN THE LOGIN BUTTON "
        login_button = driver.find_elements(By.TAG_NAME, 'button')
        login_button[1].click()

        time.sleep(5)

        try:
            
            " TRY TO FIND THE ERROR MESSAGE "
            driver.find_element_by_id('slfErrorAlert')
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


class LikePhotosByHashtag:

    def __init__(self, hashtag, n_likes):

        """
        this class like N photos based in the hashtag passed by the user
        """

        " NECESSARY FUNCTIONS "
        def webDriverConfiguration():

            """
            this function is responsible to configures and returns the webdriver
            """

            " CONFIGURATION "
            options = Options()
            options.headless = False

            " INSTANCES THE WEBDRIVER "
            driver = webdriver.Chrome(executable_path='C:\chromedriver.exe', chrome_options=options)

            return driver

        def userInformation():

            """
            this function is responsible to catch the user and password Instagram of the current AutoLike's user
            """
            
            " CATCHING THE USER "
            file_directory = 'controller/system_files/user_instagram.txt'

            file_reader = FileReader(file_directory=file_directory)
            user_instagram = file_reader.startFileReader()

            " CATCHING THE PASSWORD "
            file_directory = f'controller/users/{user_instagram}/{user_instagram}.txt'

            file_reader = FileReader(file_directory=file_directory)
            return_file_reader = file_reader.startFileReader()

            password_instagram = return_file_reader.split('-')
            password_instagram = password_instagram[1]


            user_information = [user_instagram, password_instagram]

            return user_information


        " INSTANCES THE VARIABLES "
        self.__driver = webDriverConfiguration()
        user_information = userInformation()

        self.__user_instagram = user_information[0]
        self.__password_instagram = user_information[1]
        self.__hashtag = hashtag
        self.__n_likes = n_likes


    def __startLikePhotos(self):

        """
        this method verify if the 'moment user' is already liked
        if the moment user not is in the database, the same is appended at the database
        """

        " NECESSARY FUNCTIONS "
        def printProgress(type_progress, liked_photos, n_likes, **kws):

            os.system('cls')

            " INSTANCES THE VARIABLES "
            type_progress = type_progress
            liked_photos = liked_photos
            n_likes = n_likes

            print('\n===== PROGRESS =====')
            print(f'{liked_photos} OF {n_likes} PHOTOS LIKED\n')


            if type_progress == 'user_skipped':

                print('USER SKIPPED')

            elif type_progress == 'user_liked':

                moment_user = kws.get('moment_user')

                print(f'PUBLICATION OF {moment_user} LIKED')

        def registerMomentUser(moment_user):

            " INSTANCES THE VARIABLE "
            moment_user = moment_user

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


        " INSTANCES THE DRIVER "
        driver = self.__driver

        " INSTANCES VARIABLES "
        n_likes = int(self.__n_likes)
        user_instagram = self.__user_instagram

        try:

            liked_photos = 0
            n_photos = 0
            while(liked_photos < n_likes):

                printProgress(type_progress='all_progress', liked_photos=n_photos, n_likes=n_likes)

                " CATCH THE 'MOMENT USER' "
                moment_user = driver.find_element(By.CLASS_NAME, 'sqdOP.yWX7d._8A5w5.ZIAjV').text

                " CHECK THE 'MOMENT USER' "
                verify_user_database = VerifyUserDatabase(user_instagram=user_instagram, moment_user=moment_user)
                return_verify_user_database = verify_user_database.startVerifyUserDatabase()

                " IF THE USER IS ALREADY IN THE DATABASE, THE BOT SWITCH TO THE NEXT PHOTO "
                if return_verify_user_database == True:

                    printProgress(type_progress='user_skipped', liked_photos=n_photos, n_likes=n_likes)

                    right_arrow = driver.find_element(By.CLASS_NAME, '_65Bje.coreSpriteRightPaginationArrow')
                    right_arrow.click()

                    liked_photos -= 1

                else:

                    n_photos += 1

                    printProgress(type_progress='user_liked', liked_photos=n_photos, n_likes=n_likes, moment_user=moment_user)

                    " LIKES THE CURRENT PHOTO AND SWITCH TO THE NEXT PHOTO "
                    heart = driver.find_elements(By.CLASS_NAME, 'wpO6b')
                    heart[1].click()

                    registerMomentUser(moment_user=moment_user)

                    right_arrow = driver.find_element(By.CLASS_NAME, '_65Bje.coreSpriteRightPaginationArrow')
                    right_arrow.click()


                time.sleep(3)

                " INCREMENT THE 'LIKED PHOTO' VAR TO SIGNAL THE NUMBER OF PHOTOS IS ALREADY LIKED "
                liked_photos += 1

        except:

            driver.close()
            return False

        return True


    def __startPutTheHashtagAndSelectTheFirstPhoto(self):

        """
        this method put the hashtag informed by the user in the Instagram 'search input'.

        after find a corresponding hashtag to the hashtag reported
        the bot clicks at the first photo which he can see
        """

        " INSTANCES THE DRIVER "
        driver = self.__driver

        try:

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

        except:

            driver.close()
            return False

        return True


    def startLikePhotosByHashtag(self):

        " this method like N photos based in the hashtag passed by the user "

        " VARIABLES "
        driver = self.__driver
        user_instagram = self.__user_instagram
        password_instagram = self.__password_instagram
        error = ''


        " BOT - START "

        GeneralOptions(driver, user_instagram, password_instagram)

        file_directory = 'controller/communication_file/return_bot.txt'

        file_reader = FileReader(file_directory)
        file_content = file_reader.startFileReader()

        " VERIFY IF THE INITIAL ACTION ENDED WELL "
        if file_content != 'True':

            " SPLITS THE FILE CONTENT TO FILTER THE RETURNS "
            file_content = file_content.split('-')

            " INSTANCES THE RETURNS "
            first_return = file_content[0]
            second_return = file_content[1]
            third_return = file_content[2]

            " CATCHES THE ERROR BASED IN THE RETURNS "
            if first_return == False:

                error = 'general_options-first_return'
                return_list = [False, error]
                return error

            else:

                " IF 'first_return == True' "
                if second_return == False:

                    error = 'general_options-second_return'
                    return_list = [False, error]
                    return error

                else:

                    " IF 'first_return == True' AND 'second_return == True' "
                    if third_return == False:

                        error = 'general_options-third_return'
                        return_list = [False, error]
                        return error


        time.sleep(2)

        " PUT THE HASHTAG AND CLICK AT THE FIRST PHOTO "
        return_first_photo = self.__startPutTheHashtagAndSelectTheFirstPhoto()

        if return_first_photo == False:

            error = 'first_photo'
            return_list = [False, error]
            return return_list

        time.sleep(2)


        " START THE 'LIKE PHOTO' PROCESS "
        return_like_photos_process = self.__startLikePhotos()

        if return_like_photos_process == False:

            error = 'like_photo_process'
            return_list = [False, error]
            return return_list


        " BOT - END "

        driver.close()

        return True


class LikePhotosByUsers:

    def __init__(self, users_selected, kind_likes, n_photos, **kws):
        
        """
        this class one by one Instagram profile and likes a X number of photos
        """

        " NECESSARY FUNCTIONS "
        def webDriverConfiguration():

            """
            this function is responsible to configures and returns the webdriver
            """

            " CONFIGURATION "
            options = Options()
            options.headless = False

            " INSTANCES THE WEBDRIVER "
            driver = webdriver.Chrome(executable_path='C:\chromedriver.exe', chrome_options=options)

            return driver

        def userInformation():

            """
            this function is responsible to catch the user and password Instagram of the current AutoLike's user
            """
            
            " CATCHING THE USER "
            file_directory = 'controller/system_files/user_instagram.txt'

            file_reader = FileReader(file_directory=file_directory)
            user_instagram = file_reader.startFileReader()

            " CATCHING THE PASSWORD "
            file_directory = f'controller/users/{user_instagram}/{user_instagram}.txt'

            file_reader = FileReader(file_directory=file_directory)
            return_file_reader = file_reader.startFileReader()

            password_instagram = return_file_reader.split('-')
            password_instagram = password_instagram[1]


            user_information = [user_instagram, password_instagram]

            return user_information


        " INSTANCES THE VARIABLES "
        self.__driver = webDriverConfiguration()
        user_information = userInformation()

        self.__user_instagram = user_information[0]
        self.__password_instagram = user_information[1]
        self.__users_selected = users_selected
        self.__kind_likes = kind_likes
        self.__n_photos = n_photos
        self.__checkbutton_value = kws.get('checkbutton_value')


    def __startUpdateSecondDatabase(self, current_user):

        " INSTANCES THE CURRENT INSTAGRAM USER "
        current_user = current_user

        try:

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

            file_directory = 'controller/system_files/user_manipulation/n_selected_users.txt'

            file_writer = FileWriter(file_content=file_content, file_directory=file_directory)
            file_writer.startFileWriter()

            " UPDATES THE USERS SELECTED - END "

        except:

            return False

        return True


    def __startLikesRandomUserPublications(self, photos_randomized, **kws):

        " this method likes random users photos "

        " INSTANCES THE DRIVER "
        driver = self.__driver
        
        " INSTANCES VARIABLES "
        photos_randomized = photos_randomized # STORES THE LIST OF PHOTOS WHICH WILL BE LIKED
        checkbutton_value = kws.get('checkbutton_value')

        try:

            " OPEN THE FIRS PUBLICATION "
            first_publication = driver.find_elements(By.CLASS_NAME, 'v1Nh3.kIKUG._bz0w')
            first_publication[0].click()

            current_position = 0
            photos_liked = 0
            sended_messages = 0
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

                        time.sleep(2)

                " GOES TO THE SELECTED PUBLICATION - END "

                time.sleep(1)


                if checkbutton_value == 1 and sended_messages == 0:

                    " INSTANCES THE WRITTED TEXT "
                    writted_text = kws.get('writted_text')

                    comment_box_click = driver.find_element(By.CLASS_NAME, 'Ypffh')
                    comment_box_click.click()

                    time.sleep(1)

                    comment_box_write = driver.find_element(By.CLASS_NAME, 'Ypffh.focus-visible')
                    comment_box_write.send_keys(writted_text)

                    time.sleep(3)

                    button_send = driver.find_element(By.CLASS_NAME, 'sqdOP.yWX7d.y3zKF')
                    button_send.click()

                    time.sleep(3)

                    sended_messages = 1

                #os.system('pause')

                heart = driver.find_elements(By.CLASS_NAME, 'wpO6b')
                heart[2].click()

                photos_liked += 1

                print(f'PHOTOS LIKED: {photos_liked}')

            print('')

            close_window = driver.find_element_by_xpath('/html/body/div[4]/div[3]/button')
            close_window.click()

        except:

            return False

        return True


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


    def __startPrintProgress(self, user, profiles, users_selected):

        " INSTANCES THE VARIABLES "
        user = user
        profiles = profiles
        users_selected = users_selected

        os.system('cls')

        print('\n===== PROGRESS =====')
        print(f'{profiles} OF {len(users_selected)} PROFILES ACCESSED\n')

        print(f'CURRENT INSTAGRAM PROFILE: {user}')


    def startLikesPhotosByUsers(self, **kws):

        " this method likes N photos in N instagram users selecteds by the program user "

        " VARIABLES "
        driver = self.__driver
        users_selected = self.__users_selected # STORES THE USERS WHO WILL HAVE THEIR PUBLICATIONS LIKED
        n_photos = self.__n_photos # STORES THE NUMBER OF PHOTOS
        user_instagram = self.__user_instagram
        password_instagram = self.__password_instagram


        " BOT - START "

        GeneralOptions(driver, user_instagram, password_instagram)

        file_directory = 'controller/communication_file/return_bot.txt'

        file_reader = FileReader(file_directory)
        file_content = file_reader.startFileReader()

        " VERIFY IF THE INITIAL ACTION ENDED WELL "
        if file_content != 'True':

            " SPLITS THE FILE CONTENT TO FILTER THE RETURNS "
            file_content = file_content.split('-')

            " INSTANCES THE RETURNS "
            first_return = file_content[0]
            second_return = file_content[1]
            third_return = file_content[2]

            " CATCHES THE ERROR BASED IN THE RETURNS "
            if first_return == False:

                error = 'general_options-first_return'
                return_list = [False, error]
                return error

            else:

                " IF 'first_return == True' "
                if second_return == False:

                    error = 'general_options-second_return'
                    return_list = [False, error]
                    return error

                else:

                    " IF 'first_return == True' AND 'second_return == True' "
                    if third_return == False:

                        error = 'general_options-third_return'
                        return_list = [False, error]
                        return error


        time.sleep(3)

        profiles = 1
        for user in users_selected:

            " PRINT THE LIKES PROGRESS "
            self.__startPrintProgress(user, profiles, users_selected)

            " INSTAGRAM USER VERIFICATION "
            general_options_one = GeneralOptionsInstagramUser(driver, 1, user=user)
            return_general_options_one = general_options_one.returnOption()

            if return_general_options_one == False:
                continue

            time.sleep(3)

            photos_randomized = ''
            return_general_options_two = ''
            if return_general_options_one == True:
                general_options_two = GeneralOptionsInstagramUser(driver, 2, user=user, n_photos=n_photos)
                return_general_options_two = general_options_two.returnOption()

                if return_general_options_two != '':

                    " RANDOMIZE PHOTOS PROCESS "
                    n_user_publications = return_general_options_two
                    photos_randomized = self.__startRandomizePublications(n_user_publications, n_photos)

            else:
                continue    


            time.sleep(2)

            if photos_randomized != '':

                " INSTANCES THE CHECKBUTTON "
                checkbutton_value = self.__checkbutton_value


                if checkbutton_value == 0:

                    " LIKES THE PHOTOS IN EACH INSTAGRAM USER PROFILE "
                    return_random_user_publication = self.__startLikesRandomUserPublications(photos_randomized=photos_randomized)

                    if return_random_user_publication == False:

                        error = 'likes_random_publications'
                        return_list = [False, error]
                        return return_list

                elif checkbutton_value == 1:

                    " INSTANCES THE WRITTED TEXT "
                    writted_text = kws.get('writted_text')

                    " LIKES THE PHOTOS IN EACH INSTAGRAM USER PROFILE AND WRITE A COMMENT "
                    return_random_user_publication = self.__startLikesRandomUserPublications(photos_randomized=photos_randomized, checkbutton_value=1, writted_text=writted_text)

                    if return_random_user_publication == False:

                        error = 'likes_random_publications'
                        return_list = [False, error]
                        return return_list


                " UPDATES THE SECOND DATABASE "
                " REMOVING THE USERS IS ALREADY LIKED "
                return_update_second_database = self.__startUpdateSecondDatabase(current_user=user)
                
                if return_update_second_database == False:

                    error = 'update_second_database'
                    return_list = [False, error]
                    return return_list


            profiles += 1

            time.sleep(2)

            " THE BOT - END "

        driver.close()

        return True



class SendDirectMessage:

    def __init__(self, users_selected, writted_text):
        
        """
        this class one by one Instagram profile and likes a X number of photos
        """

        " NECESSARY FUNCTIONS "
        def webDriverConfiguration():

            """
            this function is responsible to configures and returns the webdriver
            """

            " CONFIGURATION "
            options = Options()
            options.headless = False

            " INSTANCES THE WEBDRIVER "
            driver = webdriver.Chrome(executable_path='C:\chromedriver.exe', chrome_options=options)

            return driver

        def userInformation():

            """
            this function is responsible to catch the user and password Instagram of the current AutoLike's user
            """
            
            " CATCHING THE USER "
            file_directory = 'controller/system_files/user_instagram.txt'

            file_reader = FileReader(file_directory=file_directory)
            user_instagram = file_reader.startFileReader()

            " CATCHING THE PASSWORD "
            file_directory = f'controller/users/{user_instagram}/{user_instagram}.txt'

            file_reader = FileReader(file_directory=file_directory)
            return_file_reader = file_reader.startFileReader()

            password_instagram = return_file_reader.split('-')
            password_instagram = password_instagram[1]


            user_information = [user_instagram, password_instagram]

            return user_information


        " INSTANCES THE VARIABLES "
        self.__driver = webDriverConfiguration()
        user_information = userInformation()

        self.__user_instagram = user_information[0]
        self.__password_instagram = user_information[1]
        self.__users_selected = users_selected
        self.__writted_text = writted_text


    def __startUpdateSecondDatabase(self, current_user):

        " INSTANCES THE CURRENT INSTAGRAM USER "
        current_user = current_user

        try:

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

            file_directory = 'controller/system_files/user_manipulation/n_selected_users.txt'

            file_writer = FileWriter(file_content=file_content, file_directory=file_directory)
            file_writer.startFileWriter()

            " UPDATES THE USERS SELECTED - END "

        except:

            return False

        return True


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


        " VARIABLE WHICH CATCH THE NUMBER OF PUBLICATIONS WHICH THE 'current user' HAVES "
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


    def __startPrintProgress(self, user, profiles, users_selected):

        " INSTANCES THE VARIABLES "
        user = user
        profiles = profiles
        users_selected = users_selected

        os.system('cls')

        print('\n===== PROGRESS =====')
        print(f'{profiles} OF {len(users_selected)} PROFILES ACCESSED\n')

        print(f'CURRENT INSTAGRAM PROFILE: {user}')


    def startSendDirectMessage(self):

        " this method sends a direct message to N instagram users selecteds by the program user "

        " VARIABLES "
        driver = self.__driver
        users_selected = self.__users_selected # STORES THE USERS WHO WILL HAVE THEIR PUBLICATIONS LIKED
        writted_text = self.__writted_text
        user_instagram = self.__user_instagram
        password_instagram = self.__password_instagram

        " BOT - START "

        GeneralOptions(driver, user_instagram, password_instagram)

        file_directory = 'controller/communication_file/return_bot.txt'

        file_reader = FileReader(file_directory)
        file_content = file_reader.startFileReader()

        " VERIFY IF THE INITIAL ACTION ENDED WELL "
        if file_content != 'True':

            " SPLITS THE FILE CONTENT TO FILTER THE RETURNS "
            file_content = file_content.split('-')

            " INSTANCES THE RETURNS "
            first_return = file_content[0]
            second_return = file_content[1]
            third_return = file_content[2]

            " CATCHES THE ERROR BASED IN THE RETURNS "
            if first_return == False:

                error = 'general_options-first_return'
                return_list = [False, error]
                return error

            else:

                " IF 'first_return == True' "
                if second_return == False:

                    error = 'general_options-second_return'
                    return_list = [False, error]
                    return error

                else:

                    " IF 'first_return == True' AND 'second_return == True' "
                    if third_return == False:

                        error = 'general_options-third_return'
                        return_list = [False, error]
                        return error


        time.sleep(3)


        profiles = 1
        for user in users_selected:

            " PRINT THE LIKES PROGRESS "
            self.__startPrintProgress(user, profiles, users_selected)

            " VERIFY IF THE 'user' EXISTS "
            return_verify_user = self.__startVerifyUserExistence(current_user=user)

            if return_verify_user == False:
                continue


            time.sleep(2)


            " IF THE 'user' EXISTS, THE PROGRAM VERIFY SOME CONDITIONS "
            return_individual_user_validation = ''
            if return_verify_user == True:
                return_individual_user_validation = self.__startIndividualUserValidation(current_user=user)

            if return_individual_user_validation == False:
                continue

            else:

                " IF THE 'return_individual_user_validation' RETURNS THE NUMBER OF "
                " PUBLICATIONS OF THE USER, THE PROGRAM CATCH THIS NUMBER AND USE IT "
                " TO RANDOMIZE THE PUBLICATIONS WHICH WILL BE LIKED "
                photos_randomized = ''
                if return_individual_user_validation != '':

                    n_user_publications = return_individual_user_validation # CONTAINS THE NUMBER OF PUBLICATIONS
                                                                            # WHAT THE INSTAGRAM USER HAS
                    photos_randomized = self.__startRandomizePublications(n_photos=n_photos, n_user_publications=n_user_publications)


            time.sleep(2)

            if photos_randomized != '':

                " LIKES THE PHOTOS IN EACH INSTAGRAM USER PROFILE "
                return_random_user_publication = self.__startLikesRandomUserPublications(photos_randomized=photos_randomized)

                if return_random_user_publication == False:

                    error = 'likes_random_publications'
                    return_list = [False, error]
                    return return_list


                " UPDATES THE SECOND DATABASE "
                " REMOVING THE USERS IS ALREADY LIKED "
                return_update_second_database = self.__startUpdateSecondDatabase(current_user=user)
                
                if return_update_second_database == False:

                    error = 'update_second_database'
                    return_list = [False, error]
                    return return_list


            profiles += 1

            time.sleep(2)

            " THE BOT - END "

        driver.close()

        return True