# TKINTER LIBRARY
from tkinter import *

# MODEL
from model.start_error_handling import ErrorHandling

# VIEW
from view.Message import Message

# CONTROLLER
from controller.file_writer import FileWriter

class OptionThreeFragments:

    """
    this class returns the option three window fragments
    """

    def __init__(self, window):
        
        " INSTANCES THE WINDOW "
        self.__window = window

        " INSTANCES THE FRAME "
        self.__message_frame = Frame(window, width=500, height=300, bg='floral white')
        self.__message_frame.pack(side=TOP)



    def startButton(self):

        " this method show the button which will return the information writted in the entries "

        " INSTANCES THE MESSAGE "
        start_message = 'Start'

        " INSTANCES THE WIDGETS "
        start_frame = self.__message_frame

        start_button = Button(start_frame, text=start_message, font=('arial', 15, 'bold'), 
        bg='dark salmon', activebackground='salmon', activeforeground='white',
        command=self.__startErrorHandling)
        start_button.place(x=240, y=140)


    def startSeparator(self):

        " this method creates a widget which can separate others widgets "

        " INSTANCES THE FRAME "
        message_frame = self.__message_frame

        " CREATE THE FRAME SEPARATOR "
        separator_frame = Frame(message_frame, width=500, height=10, bg='dark salmon')
        separator_frame.pack(side=TOP)


    def startText(self):

        " this method shows the text widget "

        " INSTANCES THE FRAME "
        message_frame = self.__message_frame

        self.__message_text = Text(message_frame, font=('arial', 15, 'bold'), width=41, height=5)
        self.__message_text.place(x=20, y=60)


    def startLabels(self):

        " this method shows the labels "

        " INSTANCES THE FRAME "
        message_frame = self.__message_frame

        " INSTANCES THE TEXT VARIABLE "
        text = 'Write the message which will be sended'

        " INSTANCES THE WIDGET "
        message_label = Label(message_frame, text=text, font=('arial', 15, 'bold'), bg='floral white')
        message_label.place(x=40, y=20)


    def __returnOption(self, type_return, **kws):
        
        " this method returns the input of the user "

        " INSTANCES THE WINDOW "
        window = self.__window

        if type_return == 'send':

            " VARIABLES WHICH WILL USED "
            users_selected = kws.get('users_selected') # STR
            kind_likes = kws.get('kind_likes') # INT
            n_photos = kws.get('n_photos') # INT

            if kind_likes == 1:
                kind_likes = 'sequence'

            elif kind_likes == 2:
                kind_likes = 'random'

            n_photos = n_photos
            
            " WRITE THE OPTION TWO RETURN " 
            file_directory = 'controller/communication_file/return_option_two.txt'
            file_content = f'send-{kind_likes}-{n_photos}'

            file_writer = FileWriter(file_content=file_content, file_directory=file_directory)
            file_writer.startFileWriter()

            " WRITE THE SELECTED USERS "
            file_directory = 'controller/communication_file/return_option_two/return_selected_users.txt'
            file_content = users_selected

            file_writer = FileWriter(file_content=file_content, file_directory=file_directory)
            file_writer.startFileWriter()

            " SHOWS A MESSAGE "
            type_message = 'info'
            title_message = 'Logging into Instagram'
            text_message = 'We are logging into Instagram\nYou can close this window'

            message = Message(type_message=type_message, title_message=title_message, text_message=text_message)
            message.startMessage()

            window.destroy()


        elif type_return == 'manipulate_database':

            button = kws.get('button')

            file_directory = f'controller/system_files/user_instagram.txt'

            file_reader = FileReader(file_directory=file_directory)
            file_content = file_reader.startFileReader()

            user = file_content

            file_directory = f'controller/users/{user}/second_database.txt'

            file_reader = FileReader(file_directory=file_directory)
            file_content = file_reader.startFileReader()

            if file_content == '':

                " INFORMS WHAT THE 'second_database.txt' IS EMPTY " 
                file_directory = 'controller/communication_file/return_option_two.txt'

                if button == 'select_users':
                    file_content = button
                    window.destroy()
                
                else:
                    " SHOW A MESSAGE "
                    type_message = 'error'
                    title_message = 'No users selected'
                    text_message = f'Please, select at least one user before viewing or deleting him'

                    message = Message(type_message, title_message, text_message)
                    message.startMessage()

                file_writer = FileWriter(file_content=file_content, file_directory=file_directory)
                file_writer.startFileWriter()

            else:

                " CATCH THE DIRECTORY WHICH HAS THE 'return_option_one.txt' FILE " 
                file_directory = 'controller/communication_file/return_option_two.txt'
                file_content = f'{button}'

                file_writer = FileWriter(file_content=file_content, file_directory=file_directory)
                file_writer.startFileWriter()

                window.destroy()


    def __startErrorHandling(self, send_entry):

        " this method verify if the typed information is valid "

        " INSTANCES THE VARIABLES WHICH WILL GET THE LOGIN AND PASSWORD OF THE USER "
        kind_likes = 2
        send_entry = send_entry

        " CATCH THE CURRENT USER "
        file_directory = 'controller/system_files/user_instagram.txt'

        file_reader = FileReader(file_directory=file_directory)
        file_content = file_reader.startFileReader()

        user = file_content

        " CATCH THE SELECTED INSTAGRAM USERS "
        file_directory = f'controller/users/{user}/second_database.txt'
        
        file_reader = FileReader(file_directory=file_directory)
        file_content = file_reader.startFileReader()

        users_selected = file_content

        " INSTANCES THE ERROR HANDLING "
        error_handling = ErrorHandling(users_selected=users_selected, send_entry=send_entry, kind_likes=kind_likes)
        return_EH = error_handling.startOptionTwoErrorHandling() # ERROR HANLING = EH

        users_selected_EH = return_EH[0]
        kind_likes_EH = return_EH[1]
        send_entry_EH = return_EH[2]

        if users_selected_EH == True and send_entry_EH == True and kind_likes_EH == True:

            " CALL THE METHOD WHICH WILL WRITE THE INFORMATION "
            self.__returnOption(type_return='send', users_selected=users_selected, kind_likes=kind_likes, n_photos=send_entry)

        else:

            if users_selected_EH == False and send_entry_EH == False and kind_likes_EH == False:
                
                " SHOWS A MESSAGE "
                type_message = 'warning'
                title_message = 'Warning'
                text_message = 'Please, selected at least one Instagram User to likes\nNumber of photos will be liked invalid\nPlease, selected at least one Kind of Likes'

                message = Message(type_message=type_message, title_message=title_message, text_message=text_message)
                message.startMessage()

            elif users_selected_EH == False:

                " SHOWS A MESSAGE "
                type_message = 'warning'
                title_message = 'Warning'
                text_message = 'Please, selected at least one Instagram User to likes'

                message = Message(type_message=type_message, title_message=title_message, text_message=text_message)
                message.startMessage()

            elif kind_likes_EH == False:

                " SHOWS A MESSAGE "
                type_message = 'warning'
                title_message = 'Warning'
                text_message = 'Please, selected at least one Kind of Likes'

                message = Message(type_message=type_message, title_message=title_message, text_message=text_message)
                message.startMessage()

            elif send_entry_EH == False:

                " SHOWS A MESSAGE "
                type_message = 'warning'
                title_message = 'Warning'
                text_message = 'Number of photos will be liked invalid'

                message = Message(type_message=type_message, title_message=title_message, text_message=text_message)
                message.startMessage()


    def startSeparator(self):

        " this method creates a widget which can separate others widgets "

        " INSTANCES THE WINDOW "
        window = self.__window

        " CREATE THE FRAME SEPARATOR "
        separator_frame = Frame(window, width=500, height=10, bg='dark salmon')
        separator_frame.pack(side=TOP)


    def startButtons(self, type_button):

        " this method creates the buttons which will manipulate the user database "

        type_button = type_button

        if type_button == 'database_options':

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

        elif type_button == 'send':

            " INSTANCES THE WINDOW "
            window = self.__window

            " INSTANCES THE FRAME "
            button_send_frame = self.__message_frame

            " TEXT ABOUT ANY OPTION "
            text_button = 'Send'

            button_send = Button(button_send_frame, text=text_button, font=('arial', 15, 'bold'), 
            bg='dark salmon', activebackground='salmon', activeforeground='white',
            command=lambda:self.__startErrorHandling(send_entry=self.__send_entry.get()))
            button_send.place(x=280, y=90)


    def startMessageLabel(self, type_message):

        " this method write a message in the window "

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