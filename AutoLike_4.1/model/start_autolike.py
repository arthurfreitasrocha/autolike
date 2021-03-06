# VIEW
from view.main_menu import MainMenu
from view.email import Email
from view.options import OptionOne
from view.options import OptionTwo
from view.options import OptionThree

from view.user_manipulation.start_user_manipulation import UserManipulation

from view.user_manipulation.ManipulateUsersInterface import SelectUsers
from view.user_manipulation.ManipulateUsersInterface import ViewUsers
from view.user_manipulation.ManipulateUsersInterface import DeleteUsers

# CONTROLLER
from controller.start_database import StartDatabase
from controller.clear_return import ClearReturn
from controller.file_manipulator import FileWriter
from controller.file_manipulator import FileReader
from controller.user_information import *

# BOT
from model.bots import VerifyInstagramUser
from model.bots import LikePhotosByHashtag
from model.bots import LikePhotosByUsers


class InternalClearReturn:

    def __init__(self):

        " CATCH THE CURRENT USER "
        file_directory = 'controller/system_files/user_instagram.txt'
        file_reader = FileReader(file_directory=file_directory)
        file_content = file_reader.startFileReader()

        user = file_content
        
        if user != 'Your Email will be shown here!':
            " INSTANCES THE LIST WITH THE NAME FILES"
            self.__names_file = [
                'controller/communication_file/return_bot.txt',
                'controller/communication_file/return_email.txt',
                'controller/communication_file/return_main_menu.txt',
                'controller/communication_file/return_option_one.txt',
                'controller/communication_file/return_option_two.txt',
                'controller/communication_file/return_option_three.txt',
                'controller/communication_file/return_text_window/return_text_window.txt',
                'controller/communication_file/return_user_manipulation/return_users_selected.txt',
                'controller/communication_file/return_user_manipulation/return_window_selected.txt',
                f'controller/users/{user}/second_database.txt',
                f'controller/users/{user}/temp_database.txt',
                f'controller/users/{user}/users_accessed.txt'
            ]

        else:
            " INSTANCES THE LIST WITH THE NAME FILES"
            self.__names_file = [
                'controller/communication_file/return_bot.txt',
                'controller/communication_file/return_email.txt',
                'controller/communication_file/return_main_menu.txt',
                'controller/communication_file/return_option_one.txt',
                'controller/communication_file/return_option_two.txt',
                'controller/communication_file/return_option_three.txt',
                'controller/communication_file/return_text_window/return_text_window.txt',
                'controller/communication_file/return_user_manipulation/return_users_selected.txt',
                'controller/communication_file/return_user_manipulation/return_window_selected.txt',
            ]


    def startInternalClearReturn(self):

        " RESTART THE STANDARD PHRASE "
        file_directory = 'controller/system_files/user_manipulation/n_selected_users.txt'
        file_content = 'Here will appear\nthe number of selected users'
        file_writer = FileWriter(file_content=file_content, file_directory=file_directory)
        file_writer.startFileWriter()


        " CLEAR THE FILES "
        names_file = self.__names_file

        for name_file in names_file:
            clear_return = ClearReturn(name_file)
            clear_return.startClearReturn()


class UserOption:

    def __init__(self, app_version, user_option):

        clear_return = InternalClearReturn()
        clear_return.startInternalClearReturn()
        
        self.__app_version = app_version
        user_option = user_option

        if user_option == '1':
            self.startOptionOne()

        elif user_option == '2':
            self.startOptionTwo()

        elif user_option == '3':
            self.startOptionThree()

        else:
            start_main_menu = StartMainMenu(app_version, flag='no_option')
            start_main_menu.startMainMenu()


    def startOptionOne(self):
        
        app_version = self.__app_version

        start_option_one = OptionOne(app_version=app_version)
        start_option_one.startInterface()

        return_option_one = start_option_one.readReturn()
        return_option_one = return_option_one.split('-')

        return_option = return_option_one[0]


        if return_option == 'window_closed':

            clear_return = InternalClearReturn()
            clear_return.startInternalClearReturn()

            start_main_menu = StartMainMenu(app_version)
            start_main_menu.startMainMenu()

        else:

            if return_option_one[0] == 'True':

                n_likes = return_option_one[1]

                start_option_one = OptionOne(app_version)
                start_option_one.startInterface(flag='success', n_likes=n_likes)

            else:

                error = return_option_one[1]

                start_option_one = OptionOne(app_version)
                start_option_one.startInterface(flag='failed', error=error)


            start_main_menu = StartMainMenu(app_version)
            start_main_menu.startMainMenu()


    def startOptionTwo(self):

        while(True):

            app_version = self.__app_version

            start_option_two = OptionTwo(app_version=app_version)
            start_option_two.startInterface()

            user_manipulation = UserManipulation(window='')
            return_user_manipulation = user_manipulation.readReturn()

            if return_user_manipulation == 'window-select-users':

                select_users = SelectUsers(app_version=app_version)
                select_users.startInterface()

            elif return_user_manipulation == 'window-view-users':

                select_users = ViewUsers(app_version=app_version)
                select_users.startInterface()

            elif return_user_manipulation == 'window-delete-users':

                select_users = DeleteUsers(app_version=app_version)
                select_users.startInterface()

            else:

                return_option_two = start_option_two.readReturn()

                if return_option_two == 'window_closed':
                    break

                else:

                    return_option_two_splitted = return_option_two.split('-')

                    if return_option_two_splitted[0] == 'send':
                        break

                    elif return_option_two_splitted[0] == 'send2':
                        break


        if return_option_two == 'window_closed':

            clear_return = InternalClearReturn()
            clear_return.startInternalClearReturn()

        else:

            return_option_two_splitted = return_option_two.split('-')

            if return_option_two_splitted[0] == 'send':

                " CATCH THE USERS SELECTED "
                file_directory = 'controller/communication_file/return_user_manipulation/return_users_selected.txt'

                file_reader = FileReader(file_directory=file_directory)
                file_content = file_reader.startFileReader()

                users_selected = file_content.split('-')

                " CATCH THE RETURN OF OPTION TWO "
                kind_likes = return_option_two_splitted[1]
                n_photos = return_option_two_splitted[2]

                like_photos_by_users = LikePhotosByUsers(users_selected=users_selected, kind_likes=kind_likes, n_photos=n_photos, checkbutton_value=0)
                return_like_photos_by_users = like_photos_by_users.startLikesPhotosByUsers()

                if return_like_photos_by_users == True:

                    start_option_two = OptionTwo(app_version)
                    start_option_two.startInterface(flag='success', n_profiles=len(users_selected), n_likes=n_photos)

                else:

                    error = return_like_photos_by_users[1]

                    start_option_two = OptionTwo(app_version)
                    start_option_two.startInterface(flag='failed', error=error)

            elif return_option_two_splitted[0] == 'send2':

                " CATCH THE USERS SELECTED "
                file_directory = 'controller/communication_file/return_user_manipulation/return_users_selected.txt'

                file_reader = FileReader(file_directory=file_directory)
                file_content = file_reader.startFileReader()

                users_selected = file_content.split('-')

                " CATCH THE RETURN OF OPTION TWO "
                kind_likes = return_option_two_splitted[1]
                n_photos = return_option_two_splitted[2]
                writted_text = return_option_two_splitted[3]

                print(writted_text)


                like_photos_by_users = LikePhotosByUsers(users_selected=users_selected, kind_likes=kind_likes, n_photos=n_photos, checkbutton_value=1)
                return_like_photos_by_users = like_photos_by_users.startLikesPhotosByUsers(writted_text=writted_text)

                if return_like_photos_by_users == True:

                    start_option_two = OptionTwo(app_version)
                    start_option_two.startInterface(flag='success', n_profiles=len(users_selected), n_likes=n_photos)

                else:

                    error = return_like_photos_by_users[1]

                    start_option_two = OptionTwo(app_version)
                    start_option_two.startInterface(flag='failed', error=error)


        start_main_menu = StartMainMenu(app_version)
        start_main_menu.startMainMenu()


    def startOptionThree(self):

        while(True):

            app_version = self.__app_version

            start_option_three = OptionThree(app_version=app_version)
            start_option_three.startInterface()

            user_manipulation = UserManipulation(window='')
            return_user_manipulation = user_manipulation.readReturn()

            if return_user_manipulation == 'window-select-users':

                select_users = SelectUsers(app_version=app_version)
                select_users.startInterface()

            elif return_user_manipulation == 'window-view-users':

                select_users = ViewUsers(app_version=app_version)
                select_users.startInterface()

            elif return_user_manipulation == 'window-delete-users':

                select_users = DeleteUsers(app_version=app_version)
                select_users.startInterface()

            else:

                return_option_three = start_option_three.readReturn()

                if return_option_three == 'window_closed':
                    break

                else:

                    return_option_three_splitted = return_option_three.split('-')

                    if return_option_three_splitted[0] == 'send':
                        break


        if return_option_three == 'window_closed':
        
            clear_return = InternalClearReturn()
            clear_return.startInternalClearReturn()

        else:

            return_option_three_splitted = return_option_three.split('-')

            if return_option_three_splitted[0] == 'send':

                " CATCH THE USERS SELECTED "
                file_directory = 'controller/communication_file/return_user_manipulation/return_users_selected.txt'

                file_reader = FileReader(file_directory=file_directory)
                file_content = file_reader.startFileReader()

                users_selected = file_content.split('-')

                " CATCH THE RETURN OF OPTION TWO "
                writted_text = return_option_three[1]

                #like_photos_by_users = LikePhotosByUsers(users_selected=users_selected, writted_text=writted_text, n_photos=n_photos)
                #return_like_photos_by_users = like_photos_by_users.startLikesPhotosByUsers()

                #if return_like_photos_by_users == True:

                    #start_option_two = OptionTwo(app_version)
                    #start_option_two.startInterface(flag='success', n_profiles=len(users_selected), n_likes=n_photos)

                #else:

                    #error = return_like_photos_by_users[1]

                    #start_option_two = OptionTwo(app_version)
                    #start_option_two.startInterface(flag='failed', error=error)



            start_main_menu = StartMainMenu(app_version)
            start_main_menu.startMainMenu()

        start_main_menu = StartMainMenu(app_version)
        start_main_menu.startMainMenu()


class StartEmail:

    def __init__(self, app_version, password_status, password, login):

        clear_return = InternalClearReturn()
        clear_return.startInternalClearReturn()
        
        self.__app_version = app_version
        self.__password_status = password_status
        self.__password = password
        self.__login = login


    def startEmail(self):

        app_version = self.__app_version
        password_status = self.__password_status
        password = self.__password
        login = self.__login
        
        email_window = Email(app_version)
        email_window.startInterface(password_status='invisible', password=password, login=login)

        return_email = email_window.readReturn()

        if return_email == 'window_closed':

            start_main_menu = StartMainMenu(app_version)
            start_main_menu.startMainMenu()

        else:

            return_email = return_email.split('-')
            return_email_text = return_email[0]

            if return_email_text == 'send_instagram_login':

                login = return_email[1]
                password = return_email[2]

                user_verification = VerifyInstagramUser(login, password)
                return_user_verification = user_verification.startVerifyInstagramUser()

                if return_user_verification == True:

                    file_content = 'show_password--'
                    file_directory = 'controller/communication_file/return_email.txt'

                    file_writer = FileWriter(file_content=file_content, file_directory=file_directory)
                    file_writer.startFileWriter()

                    user_register = UserRegister(user_login=login, user_password=password)
                    return_user_register = user_register.startUserRegister()

                    user_login = UserLogin(user_login=login)
                    user_login.startUserLogin()

                    start_main_menu = StartMainMenu(app_version, flag='success')
                    start_main_menu.startMainMenu()

                else:

                    email_window.startInterface(password_status=password_status, password=password, login=login, flag='failed')

                    start_main_menu = StartMainMenu(app_version)
                    start_main_menu.startMainMenu()


class StartMainMenu:

    def __init__(self, app_version, **kws):

        clear_return = InternalClearReturn()
        clear_return.startInternalClearReturn()
        
        self.__app_version = app_version
        self.__flag = kws.get('flag')


    def startMainMenu(self):

        app_version = self.__app_version
        flag = self.__flag

        file_directory = 'controller/system_files/user_instagram.txt'

        file_reader = FileReader(file_directory)
        user_instagram = file_reader.startFileReader()

        main_menu_window = MainMenu(user_instagram, app_version)
        main_menu_window.startInterface(flag=flag)

        return_main_menu = main_menu_window.readReturn()
        return_main_menu = return_main_menu.split('-')

        return_option = return_main_menu[0]
        

        if not return_option == 'window_closed':
            
            if return_option == 'email_option':
                
                file_directory = 'controller/communication_file/return_email.txt'
                file_content = 'show_password--'

                file_writer = FileWriter(file_content=file_content, file_directory=file_directory)
                file_writer.startFileWriter()

                start_email = StartEmail(app_version=app_version, password_status='invisible', password='', login='')
                start_email.startEmail()

            elif return_option == 'user_option':

                user_option = return_main_menu[1]
                
                user_option = UserOption(app_version=app_version, user_option=user_option)


class StartAutoLike:

    """
    this class starts AutoLike
    """
    def __init__(self):

        clear_return = InternalClearReturn()
        clear_return.startInternalClearReturn()

        variables = StartDatabase()
        variables = variables.readDatabase()

        self.__app_version = variables['app_version']
        self.__user_instagram = variables['user_instagram']


    def startInterface(self):

        files = [
            'controller/communication_file/return_main_menu.txt',
            'controller/communication_file/return_email.txt'
            ]

        for the_file in files:
            clear_return = ClearReturn(name_file=the_file)
            clear_return.startClearReturn()

        variables = StartDatabase()
        variables = variables.readDatabase()

        app_version = self.__app_version
        user_instagram = self.__user_instagram

        start_main_menu = StartMainMenu(app_version)
        start_main_menu.startMainMenu()
