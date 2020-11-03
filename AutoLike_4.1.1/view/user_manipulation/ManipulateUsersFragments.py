# TKINTER LIBRARY
from tkinter import *

# MODEL
from controller.ErrorHandling import ErrorHandlingEmail

# VIEW
from view.Widgets import Widgets
from view.Message import Message

# CONTROLLER
from controller.file_manipulator import FileReader
from controller.file_manipulator import FileWriter


class MasterWidgets:

    def __init__(self, window):

        """
        this class constructs the buttons responssibles to manipulates the database
        """
        
        " INSTANCES THE WINDOW "
        self.__window = window
        window = self.__window

        " INSTANCES THE WIDGETS "
        self.__widget = Widgets(window)
        widget = self.__widget

        " INSTANCES THE FRAME "
        self.__message_frame = widget.startFrame(500, 200, 'floral white', TOP)


    def startButtons(self):

        " this method creates the buttons which will manipulate the user database "

        " INSTANCES THE WINDOW "
        message_frame = self.__message_frame

        " INSTANCES THE WIDGET "
        widget = self.__widget

        " TEXT ABOUT ANY OPTION "
        text_button_01 = 'Select\nNew Users'
        text_button_02 = 'View\nSelected Users'
        text_button_03 = 'Delete\nSelected Users'

        " INSTANCES THE BUTTONS "
        " SELECT USERS BUTTON "
        widget.startButton(message_frame, text_button_01, 'arial-15-bold', 'dark salmon', 'salmon', 'white', 'button-select-users', 20, 65)

        " VIEW USERS BUTTON "
        widget.startButton(message_frame, text_button_02, 'arial-15-bold', 'dark salmon', 'salmon', 'white', 'button-view-users', 150, 65)

        " DELETE USERS BUTTON "
        widget.startButton(message_frame, text_button_03, 'arial-15-bold', 'dark salmon', 'salmon', 'white', 'button-delete-users', 320, 65)


    def startMessage(self, type_message):

        " this method write a message in the window "

        self.__message_frame.destroy()

        " INSTANCES THE WIDGET "
        widget = self.__widget
        
        if type_message == 'database_options-no_user':

            file_directory = 'controller/system_files/user_manipulation/n_selected_users.txt'

            file_reader = FileReader(file_directory=file_directory)
            file_content = file_reader.startFileReader()

            " INSTANCES THE MESSAGE "
            message_text = file_content

            " INSTANCES THE FRAME PROPORTIONS "
            width = 500
            height = 140

            " INSTANCES THE LOCATION OF THE MESSAGE "
            x = 110
            y = 5

        elif type_message == 'database_options':

            file_directory = 'controller/system_files/user_manipulation/n_selected_users.txt'

            file_reader = FileReader(file_directory=file_directory)
            file_content = file_reader.startFileReader()

            " INSTANCES THE MESSAGE "
            message_text = file_content

            " INSTANCES THE FRAME PROPORTIONS "
            width = 500
            height = 140

            " INSTANCES THE LOCATION OF THE MESSAGE "
            x = 170
            y = 17

        elif type_message == 'send':

            " INSTANCES THE MESSAGE "
            message_text = 'Inform the amount of photos\nwill be liked of each user'

            " INSTANCES THE FRAME PROPORTIONS "
            width = 500
            height = 150

            " INSTANCES THE LOCATION OF THE MESSAGE "
            x = 110
            y = 15


        " INSTANCES THE FRAME "
        self.__message_frame = widget.startFrame(width, height, 'floral white', TOP)
        message_frame = self.__message_frame

        self.__message_label = widget.startLabel(message_frame, message_text, 'arial-15-bold', 'floral white', x, y)


    def startSeparator(self):

        " this method creates a widget which separate others widgets "

        " INSTANCES THE WIDGET "
        widget = self.__widget

        " CREATE THE FRAME SEPARATOR "
        widget.startFrame(500, 10, 'dark salmon', TOP)


class MinimumWidgets:

    def __init__(self, window):

        """
        this class manipules the database
        """
        
        " INSTANCES THE WINDOW "
        self.__window = window
        window = self.__window

        " INSTANCES THE WIDGETS "
        self.__widget = Widgets(window)


    def __catchUsers(self, type_catch):

        " this method catch the users database "

        " INSTANCES THE TYPE CATCH VARIABLE "
        type_catch = type_catch


        " CATCH THE CURRENT USER "
        file_directory = 'controller/system_files/user_instagram.txt'

        file_reader = FileReader(file_directory=file_directory)
        file_content = file_reader.startFileReader()

        user = file_content

        " READ THE SECOND DATABASE "
        file_directory = f'controller/users/{user}/second_database.txt'

        file_reader = FileReader(file_directory=file_directory)
        file_content = file_reader.startFileReader()

        second_database = file_content


        if type_catch == 'select_users':
            
            " VARIABLES "
            instagram_users = ''
            refactored_instagram_users = ''

            " OPEN THE DATABASE OF THE CURRENT USER "
            file_directory = f'controller/users/{user}/database.txt'

            file_reader = FileReader(file_directory=file_directory)
            file_content = file_reader.startFileReader()

            database = file_content

            " READ THE TEMP DATABASE (A ESPECIAL DATABASE USED JUST TO SHOW THE USERS) "
            file_directory = f'controller/users/{user}/temp_database.txt'

            file_reader = FileReader(file_directory=file_directory)
            file_content = file_reader.startFileReader()

            temp_database = file_content

            if temp_database == '':

                " UPDATES THE SECOND DATABASE USING THE FIRST DATABASE CONTENT "
                file_directory = f'controller/users/{user}/temp_database.txt'

                file_writer = FileWriter(file_content=database, file_directory=file_directory)
                file_writer.startFileWriter()

                " REFACTOR THE INSTAGRAM USERS, SEPARATING ONE BY ONE "
                instagram_users = database.split('-')

                refactored_instagram_users = []
                for instagram_user in instagram_users:

                    refactor_string = instagram_user
                    refactored_instagram_users.append(refactor_string)

            else:

                " UPDATES THE INSTAGRAM USER VARIABLE "
                file_directory = f'controller/users/{user}/temp_database.txt'

                file_reader = FileReader(file_directory=file_directory)
                file_content = file_reader.startFileReader()

                instagram_users = file_content.split('-')

                refactored_instagram_users = []
                for instagram_user in instagram_users:

                    refactor_string = instagram_user
                    refactored_instagram_users.append(refactor_string)

            " RETURN THE INSTAGRAM USERS NAMES "
            return refactored_instagram_users


        elif type_catch == 'view_users' or type_catch == 'delete_users':


            " UPDATES THE SECOND DATABASE VARIABLE"
            file_directory = f'controller/users/{user}/second_database.txt'

            file_reader = FileReader(file_directory=file_directory)
            file_content = file_reader.startFileReader()

            second_database = file_content

            " REFACTOR THE INSTAGRAM USERS, SEPARATING ONE BY ONE "
            instagram_users = second_database.split('-')

            refactored_instagram_users = []
            for instagram_user in instagram_users:

                refactored_string = instagram_user
                refactored_instagram_users.append(refactored_string)

            " RETURN THE INSTAGRAM USERS NAMES SAVED IN THE SECOND DATABASE "
            return refactored_instagram_users


    def startButton(self, type_button):

        " this method creates the buttons which will send or back the windows "

        " INSTANCES THE TYPE BUTTON "
        type_button = type_button

        " INSTANCES THE WIDGETS "
        widget = self.__widget


        if type_button == 'back':

            " TEXT ABOUT ANY OPTION "
            text_button = 'Back'

            " INSTANCES THE FRAME "
            button_frame = widget.startFrame(500, 100, 'floral white', TOP)

            " INSTANCES THE BUTTON "
            widget.startButton(button_frame, text_button, 'arial-15-bold', 'dark salmon', 'salmon', 'white', 'button-back', 225, 20)

        elif type_button == 'select_users' or type_button == 'delete_users':

            " TEXT ABOUT ANY OPTION "
            text_button = 'Send'

            " INSTANCES THE FRAME "
            button_frame = self.__check_frame

            if type_button == 'select_users':
                command = 'select-users'

            else:
                command = 'delete-users'

            widget.startButton(button_frame, text_button, 'arial-15-bold', 'dark salmon', 'salmon', 'white', command, 350, 20, listbox_users=self.__listbox_users, checkbutton_value=self.__checkbutton_value)


    def startCheckButton(self):

        " this method creates the checkbutton which can select all the users "

        " INSTANCES THE WIDGET "
        widget = self.__widget

        " INSTANCES THE FRAME "
        self.__check_frame = widget.startFrame(500, 110, 'floral white', TOP)
        check_frame = self.__check_frame

        " VARIABLE "
        self.__checkbutton_value = IntVar()
        checkbutton_value = self.__checkbutton_value

        " CHECKBUTTON TEXT "
        checkbutton_text = 'Select All'

        " INSTANCES THE CHECK BUTTON "
        widget.startCheckButton(check_frame, checkbutton_text, 'arial-12-bold', 'dark salmon', 'salmon', 'white', checkbutton_value, 'select-all-users', 50, 25)


    def startListBox(self, type_catch):

        " this method creates the listbox with the instagram users "

        " INSTANCES THE WINDOW "
        window = self.__window

        " INSTANCES THE TYPE CATCH VARIABLE "
        type_catch = type_catch

        " INSTANCES THE FRAME "
        frame = Frame(window, width=500, height=300, bg='floral white')
        frame.pack(side=TOP)

        " CATCH THE INSTAGRAM USERS "
        instagram_users = self.__catchUsers(type_catch=type_catch)

        scrollbar = Scrollbar(frame, width=20)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.__listbox_users = Listbox(frame, font=('arial', 15, 'bold'),
        width=50, yscrollcommand=scrollbar.set, selectmode=MULTIPLE)

        i = 0
        for instagram_user in instagram_users:
            self.__listbox_users.insert(i, f'{i+1} - {instagram_user}')

            i += 1

        self.__listbox_users.pack(side=LEFT)
        scrollbar.config(command=self.__listbox_users.yview)


    def startMessageLabel(self, message_text):

        " this method write a message in the window "

        " INSTANCES THE WINDOW "
        window = self.__window

        " INSTANCES THE FRAME "
        message_frame = Frame(window, width=500, height=80, bg='floral white')
        message_frame.pack(side=TOP)

        " INSTANCES THE MESSAGE "
        message_text = message_text

        message_label = Label(message_frame, text=message_text, font=('arial', 15, 'bold'), bg='floral white')
        message_label.place(x=175, y=25)
