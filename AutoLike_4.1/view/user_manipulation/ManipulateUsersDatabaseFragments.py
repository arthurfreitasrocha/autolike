# TKINTER LIBRARY
from tkinter import *

# MODEL
from model.ErrorHandling import ErrorHandlingEmail

# VIEW
from view.Message import Message

# CONTROLLER
from controller.file_manipulator import FileReader
from controller.file_manipulator import FileWriter

# EXTRA LIBRARY
from random import shuffle

class ManipulateUsersDatabaseFragments:

    def __init__(self, window):

        """
        this class manipules the database
        """
        
        " INSTANCES THE WINDOW "
        self.__window = window

        self.__message_frame = Frame(window, width=500, height=200, bg='floral white')
        self.__message_frame.pack(side=TOP)


    def __returnOption(self, type_return, **kws):
        
        " this method returns the input of the user "

        " INSTANCES THE WINDOW "
        window = self.__window

        " CATCH THE CURRENT USER "
        file_directory = 'controller/system_files/user_instagram.txt'

        file_reader = FileReader(file_directory=file_directory)
        file_content = file_reader.startFileReader()

        user = file_content


        if type_return == 'back':
            window.destroy()

        elif type_return == 'select_all_users':

            checkbutton_value = self.__checkbutton_value.get()

            if checkbutton_value == 1:

                " SHOWS A MESSAGE "
                type_message = 'info'
                title_message = 'All users selecteds'
                text_message = 'Success! All users selecteds'

                message = Message(type_message=type_message, title_message=title_message, text_message=text_message)
                message.startMessage()

        elif type_return == 'select_users':

            " CATCH THE USERS OF THE MAIN DATABASE "
            file_directory = f'controller/users/{user}/database.txt'

            file_reader = FileReader(file_directory=file_directory)
            file_content = file_reader.startFileReader()

            second_database = file_content.split('-')


            " INSTAGRAM USERS SELECTED BY THE USER "
            users_selected = kws.get('users_selected')
            shuffle(users_selected)

            checkbutton_value = self.__checkbutton_value.get()

            if checkbutton_value == 1:

                users_selected = []

                i = 0
                for user_second_database in second_database:
                    users_selected.append(i)

                    i += 1

                shuffle(users_selected)


            " CATCH THE NAME OF THE SELECTED USERS "
            users_selected_text = ''
            i = 0
            while(i < len(users_selected)):

                current_user = users_selected[i]

                if i == 0:
                    users_selected_text += second_database[current_user]

                else:
                    users_selected_text += f'-{second_database[current_user]}'

                i += 1


            " WRITE THE USERS SELECTEDS IN THE SECOND DATABASE, WHICH WILL USED LATER "
            file_directory = f'controller/users/{user}/second_database.txt'
            file_content = users_selected_text

            file_writer = FileWriter(file_content=file_content, file_directory=file_directory)
            file_writer.startFileWriter()

            " UPDATE THE NUMBER OF USERS IN THE SECOND DATABASE "
            file_directory = f'controller/system_files/option_two/n_selected_users.txt'
            file_content = f'{len(users_selected)} users selected'

            file_writer = FileWriter(file_content=file_content, file_directory=file_directory)
            file_writer.startFileWriter()

            " SHOWS A MESSAGE "
            type_message = 'info'
            title_message = 'Success'
            text_message = f'Success! {len(users_selected)} users added to the database'

            message = Message(type_message=type_message, title_message=title_message, text_message=text_message)
            message.startMessage()

            file_directory = 'controller/communication_file/return_option_two.txt'
            file_content = 'window_closed'

            file_writer = FileWriter(file_content=file_content, file_directory=file_directory)
            file_writer.startFileWriter()

            window.destroy()

        elif type_return == 'delete_users':

            " CATCH THE USERS OF THE SECOND DATABASE "
            file_directory = f'controller/users/{user}/second_database.txt'

            file_reader = FileReader(file_directory=file_directory)
            file_content = file_reader.startFileReader()

            second_database = file_content.split('-')


            " INSTAGRAM USERS SELECTED BY THE USER "
            users_selected = kws.get('users_selected')

            checkbutton_value = self.__checkbutton_value.get()

            if checkbutton_value == 1:

                users_selected = []

                i = 0
                for user_second_database in second_database:
                    users_selected.append(i)

                    i += 1


            " CATCH THE NAME OF THE USERS WILL BE REMOVED "
            users_will_removed = []
            for user_second_database in second_database:
                user_second_database_index = second_database.index(user_second_database)

                for user_selected in users_selected:

                    if user_second_database_index == user_selected:
                        users_will_removed.append(user_second_database)

            " REMOVE FROM THE SECOND DATABASE THE SELECTED USERS "
            for user_removed in users_will_removed:
                second_database.remove(user_removed)

            " CATCH THE NAME OF THE SELECTED USERS "
            users_selected_text = ''
            users_count = 0
            for user_second_database in second_database:
                if users_count == 0:
                    users_selected_text += user_second_database

                else:
                    users_selected_text += f'-{user_second_database}'

                users_count += 1


            " UPDATE THE SECOND USER DATABASE "
            file_directory = f'controller/users/{user}/second_database.txt'
            file_content = users_selected_text

            file_writer = FileWriter(file_content=file_content, file_directory=file_directory)
            file_writer.startFileWriter()

            " UPDATE THE NUMBER OF USERS IN THE SECOND DATABASE "
            file_directory = f'controller/system_files/option_two/n_selected_users.txt'
            if len(second_database) != 0:
                file_content = f'{len(second_database)} users selected'
            
            else:
                file_content = 'Here will appear\nthe number of selected users'

            file_writer = FileWriter(file_content=file_content, file_directory=file_directory)
            file_writer.startFileWriter()

            " SHOWS A MESSAGE "
            type_message = 'info'
            title_message = 'Success'
            text_message = f'Success! {len(users_selected)} users removed from the database'

            message = Message(type_message=type_message, title_message=title_message, text_message=text_message)
            message.startMessage()

            window.destroy()


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

        type_button = type_button

        " INSTANCES THE WINDOW "
        window = self.__window

        if type_button == 'back':

            " TEXT ABOUT ANY OPTION "
            text_button = 'Back'

            " INSTANCES THE FRAME "
            button_frame = Frame(window, width=500, height=110, bg='floral white')
            button_frame.pack(side=TOP)

            button_back = Button(button_frame, text=text_button, font=('arial', 15, 'bold'), 
            bg='dark salmon', activebackground='salmon', activeforeground='white',
            command=lambda:self.__returnOption(type_return='back'))
            button_back.place(x=225, y=20)
            
        elif type_button == 'select_users':

            " TEXT ABOUT ANY OPTION "
            text_button = 'Send'

            " INSTANCES THE FRAME "
            button_frame = self.__check_frame

            button_send = Button(button_frame, text=text_button, font=('arial', 15, 'bold'), 
            bg='dark salmon', activebackground='salmon', activeforeground='white',
            command=lambda:self.__returnOption(type_return='select_users', users_selected=self.__listbox_users.curselection()))
            button_send.place(x=350, y=20)

        elif type_button == 'delete_users':

            " TEXT ABOUT ANY OPTION "
            text_button = 'Send'

            " INSTANCES THE FRAME "
            button_frame = self.__check_frame

            button_send = Button(button_frame, text=text_button, font=('arial', 15, 'bold'), 
            bg='dark salmon', activebackground='salmon', activeforeground='white',
            command=lambda:self.__returnOption(type_return='delete_users', users_selected=self.__listbox_users.curselection()))
            button_send.place(x=350, y=20)


    def startCheckButton(self):

        " this method creates the checkbutton which can select all the users "

        " INSTANCES THE WINDOW "
        window = self.__window

        " INSTANCES THE FRAME "
        self.__check_frame = Frame(window, width=500, height=110, bg='floral white')
        self.__check_frame.pack(side=TOP)

        check_frame = self.__check_frame

        " VARIABLE "
        self.__checkbutton_value = IntVar()
        checkbutton_value = self.__checkbutton_value

        " CHECKBUTTON TEXT "
        checkbutton_text = 'Select All'

        checkbutton = Checkbutton(check_frame, text=checkbutton_text, font=('arial', 12, 'bold'),
        bg='dark salmon', activebackground='salmon', activeforeground='white',
        variable=checkbutton_value, onvalue=1, offvalue=0,
        command=lambda:self.__returnOption('select_all_users'))
        checkbutton.place(x=50, y=25)


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


    def startSeparator(self):

        " this method creates a widget which can separate others widgets "

        " INSTANCES THE WINDOW "
        window = self.__window

        " CREATE THE FRAME SEPARATOR "
        separator_frame = Frame(window, width=500, height=10, bg='dark salmon')
        separator_frame.pack(side=TOP)


    def startButtons(self):

        " this method creates the buttons which will manipulate the user database "

        " INSTANCES THE WINDOW "
        message_frame = self.__message_frame

        " TEXT ABOUT ANY OPTION "
        text_button_01 = 'Delete\nSelected Users'
        text_button_02 = 'View\nSelected Users'
        text_button_03 = 'Select\nNew Users'

        button_01 = Button(message_frame, text=text_button_01, font=('arial', 15, 'bold'),
        bg='dark salmon', activebackground='salmon', activeforeground='white',
        command=lambda:self.__returnOption(type_return='manipulate_database', button='delete_users'))
        button_01.place(x=20, y=65)

        button_02 = Button(message_frame, text=text_button_02, font=('arial', 15, 'bold'),
        bg='dark salmon', activebackground='salmon', activeforeground='white',
        command=lambda:self.__returnOption(type_return='manipulate_database', button='view_users'))
        button_02.place(x=185, y=65)

        button_03 = Button(message_frame, text=text_button_03, font=('arial', 15, 'bold'),
        bg='dark salmon', activebackground='salmon', activeforeground='white',
        command=lambda:self.__returnOption(type_return='manipulate_database', button='select_users'))
        button_03.place(x=350, y=65)


    def startMessage(self, type_message):

        " this method write a message in the window "

        self.__message_frame.destroy()

        " INSTANCES THE WINDOW "
        window = self.__window
        
        if type_message == 'database_options-no_user':

            file_directory = 'controller/system_files/option_two/n_selected_users.txt'

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

            file_directory = 'controller/system_files/option_two/n_selected_users.txt'

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

        elif type_message == 'user_options':

            " INSTANCES THE MESSAGE "
            message_text = 'Kind of likes'

            " INSTANCES THE FRAME PROPORTIONS "
            width = 500
            height = 90

            " INSTANCES THE LOCATION OF THE MESSAGE "
            x = 200
            y = 10

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
        self.__message_frame = Frame(window, width=width, height=height, bg='floral white')
        self.__message_frame.pack(side=TOP)
        message_frame = self.__message_frame

        self.__message_label = Label(message_frame, text=message_text, font=('arial', 15, 'bold'), bg='floral white')
        self.__message_label.place(x=x, y=y)