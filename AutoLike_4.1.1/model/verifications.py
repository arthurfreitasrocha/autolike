# CONTROLLER
from controller.file_manipulator import FileReader

# OPERATIONAL SYSTEM LIBRARY
import os

class VerifyUser:

    """
    this class verify if the user exists in the database
    """

    def __init__(self, user_instagram):
        
        self.__user_instagram = user_instagram


    def startVerifyUser(self):

        user_instagram = self.__user_instagram

        directory = f'controller/users/{user_instagram}'

        if os.path.isdir(directory):
            return True

        else:
            return False


class VerifyUserDatabase:

    def __init__(self, user_instagram, moment_user):

        """
        this class returns a boll telling if the 'moment_user' informed is already liked
        """

        self.__user_instagram = user_instagram
        self.__moment_user = moment_user


    def startVerifyUserDatabase(self):

        " this method returns a boll if the 'moment_user' informed is already liked "
        
        " INSTANCES THE VARIABLES "
        user_instagram = self.__user_instagram
        moment_user = self.__moment_user

        " CATCH THE PERSONAL DATABASE OF THE USER "
        file_directory = f'controller/users/{user_instagram}/database.txt'

        file_reader = FileReader(file_directory=file_directory)
        users_database = file_reader.startFileReader()

        users_database = users_database.split('-')
        
        " THIS VARIABLE IS RESPONSIBLE TO TELL IF THE MOMENT USER IS ALREADY LIKED "
        user_was_liked = False


        " VERIFY IF THE MOMENT USER IS ALREADY LIKED "
        for user_database in users_database:
            
            if user_database == moment_user:
                user_was_liked = True


        return user_was_liked
