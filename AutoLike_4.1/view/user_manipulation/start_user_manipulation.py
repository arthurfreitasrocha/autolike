# TKINTER LIBRARY
from tkinter import *

# VIEW
from view.user_manipulation.ManipulateUsersFragments import MasterWidgets

# CONTROLLER
from controller.file_manipulator import FileReader
from controller.file_manipulator import FileWriter

class UserManipulation:

    def __init__(self, window):

        """
        the objective of this class is to facilitate the instances of the windows which will manipulate the user database
        """

        " INSTANCES THE WINDOW "
        self.__window = window
        window  = self.__window


    def readReturn(self, **kws):

        " this method just read the return of 'OptionTwoFragments.py' "

        file_directory = 'controller/communication_file/return_user_manipulation/return_selected_window.txt'

        file_reader = FileReader(file_directory=file_directory)
        file_content = file_reader.startFileReader()

        return file_content


    def startUserManipulation(self, **kws):

        " this method starts the class "

        " INSTANCES THE WINDOW "
        window = self.__window

        file_directory = 'controller/system_files/option_two/n_selected_users.txt'

        file_reader = FileReader(file_directory=file_directory)
        file_content = file_reader.startFileReader()

        type_message = ''
        if file_content == 'Here will appear\nthe number of selected users':
            type_message = 'database_options-no_user'

        else:
            type_message = 'database_options'


        " INSTANCES THE FRAGMENTS OF THE WINDOW "
        fragments = MasterWidgets(window)

        " CREATES THE INTERFACE WHICH WILL CONTROLL THE INSTAGRAM DATABASE "
        fragments.startMessage(type_message=type_message)
        fragments.startButtons()

        " CREATES THE SEPARATOR "
        fragments.startSeparator()

