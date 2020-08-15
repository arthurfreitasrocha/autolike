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

