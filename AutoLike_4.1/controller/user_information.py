# CONTROLLER
from controller.verifications import VerifyUser
from controller.file_manipulator import FileReader
from controller.file_manipulator import FileWriter

# OPERATIONAL SYSTEM LIBRARY
import os

class UserLogin:

    """
    this class login the user
    """

    def __init__(self, user_login):
        
        self.__user_login = user_login


    def startUserLogin(self):

        user_login = self.__user_login

        file_directory = 'controller/system_files/user_instagram.txt'
        file_content = f'{user_login}'

        file_writer = FileWriter(file_content=file_content, file_directory=file_directory)
        file_writer.startFileWriter()


class UserRegister:

    """
    this class register new users
    """

    def __init__(self, user_login, user_password):
        
        self.__user_login = user_login
        self.__user_password = user_password


    def startUserRegister(self):
        
        " INSTANCES THE USER LOGIN AND PASSWORD "
        user_login = self.__user_login
        user_password = self.__user_password

        " VERIFY IF THE USER WAS ALREADY REGISTERED"
        verify_user = VerifyUser(user_login)
        return_verify_user = verify_user.startVerifyUser()

        " IF THE USER DOESN'T EXISTS, A NEW FOLDER AND FILES ARE CREATED "
        if return_verify_user == False:
            
            " FOLDER DIRECTORY "
            dir_directory = f'controller/users/{user_login}'

            os.mkdir(dir_directory)

            " PERSONAL USER FILES "
            file_directory = f'{dir_directory}/{user_login}.txt'
            file_content = f'{user_login}-{user_password}'

            file_writer = FileWriter(file_directory=file_directory, file_content=file_content)
            file_writer.startFileWriter()

            " PERSONAL USER DATABASES "
            file_directory = f'{dir_directory}/database.txt'
            file_content = ''

            file_writer = FileWriter(file_directory=file_directory, file_content=file_content)
            file_writer.startFileWriter()

            file_directory = f'{dir_directory}/second_database.txt'
            file_content = ''

            file_writer = FileWriter(file_directory=file_directory, file_content=file_content)
            file_writer.startFileWriter()

            file_directory = f'{dir_directory}/temp_database.txt'
            file_content = ''

            file_writer = FileWriter(file_directory=file_directory, file_content=file_content)
            file_writer.startFileWriter()

            return True

        else:

            " FOLDER DIRECTORY "
            dir_directory = f'controller/users/{user_login}'

            " PERSONAL USER FILES "
            file_directory = f'{dir_directory}/{user_login}.txt'
            file_content = f'{user_login}-{user_password}'

            file_writer = FileWriter(file_directory=file_directory, file_content=file_content)
            file_writer.startFileWriter()

            return False
