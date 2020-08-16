# TKINTER LIBRARY
from tkinter import *

# VIEW
from view.user_manipulation.select_users import SelectUsers
from view.user_manipulation.view_users import ViewUsers
from view.user_manipulation.delete_users import DeleteUsers
from view.user_manipulation.ManipulateUsersDatabaseFragments import ManipulateUsersDatabaseFragments

# CONTROLLER
from controller.file_manipulator import FileReader
from controller.file_manipulator import FileWriter

class UserManipulation:

    def __init__(self, window):

        " this class instances the 3 (three) buttons which manipulate the users "

        " INSTANCES THE WINDOW "
        self.__window = window
        window  = self.__window


    def readReturn(self, **kws):

        " this method just read the return of 'OptionTwoFragments.py' "

        file_directory = 'controller/communication_file/return_option_two.txt'

        file_reader = FileReader(file_directory=file_directory)
        file_content = file_reader.startFileReader()

        return file_content


    def startUserManipulation(self, **kws):

        " this method starts the class "

        n_profiles = kws.get('n_profiles')
        n_likes = kws.get('n_likes')
        error = kws.get('error')

        " INSTANCES THE WINDOW "
        window = self.__window

        " INSTANCES THE FRAGMENTS OF THE WINDOW "
        fragments = ManipulateUsersDatabaseFragments(window)

        file_directory = 'controller/system_files/option_two/n_selected_users.txt'

        file_reader = FileReader(file_directory=file_directory)
        file_content = file_reader.startFileReader()

        type_message = ''
        if file_content == 'Here will appear\nthe number of selected users':
            type_message = 'database_options-no_user'

        else:
            type_message = 'database_options'


        " CREATES THE INTERFACE WHICH WILL CONTROLL THE INSTAGRAM DATABASE "
        fragments.startMessage(type_message=type_message)
        fragments.startButtons()

        " CREATES THE SEPARATOR "
        fragments.startSeparator()

