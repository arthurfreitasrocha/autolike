# TKINTER LIBRARY'S
from tkinter import *

# IMAGE LIBRARY
from PIL import ImageTk, Image

# MODEL
from model.start_error_handling import ErrorHandling

# VIEW
from view.Message import Message

# CONTROLLER
from controller.file_reader import FileReader
from controller.file_writer import FileWriter

class EmailFragments:

    def __init__(self, window, open_eye_image, closed_eye_image):

        """
        this class returns the email window fragments
        """

        " INSTANCES THE WINDOW "
        self.__window = window

        " INSTANCES THE FRAME "
        self.__email_frame = Frame(window, width=500, height=300, bg='floral white')
        self.__email_frame.pack(side=TOP)

        " INSTANCES THE IMAGES "
        self.__open_eye_image = open_eye_image
        self.__closed_eye_image = closed_eye_image

        " INSTANCES THE PASSWORD STATUS "
        self.__password_status = 'hide_password'

        " INSTANCES THE LOGIN AND PASSWORD VARIABLES "
        self.__login = ''
        self.__password = ''


    def __shows_hide_password(self, type_password):

        " INSTANCES THE 'type_password' "
        type_password = type_password

        " INSTANCES THE VARIABLES WHICH WILL GET THE PASSWORD OF THE USER "
        password_entry = self.__password_entry.get()

        " INSTANCES THE FRAMES "
        password_frame = self.__email_frame
        login_password_frame = self.__email_frame

        " STORES THE CURRENT PASSWORD "
        self.__password = password_entry
        password = self.__password

        " DESTROY THE PASSWORD ENTRY AND THE IMAGE BUTTON "
        self.__password_entry.destroy()
        self.__show_hide_password_button.destroy()


        if type_password == 'show_password':

            " INSTANCES THE TYPE RETURN "
            self.__password_status = 'hide_password'
            type_return = self.__password_status

            " CATCH THE 'show_password' IMAGE "
            password_eye = self.__open_eye_image

            " INSTANCES THE 'show' VARIABLE WHICH WILL BE USED IN THE PASSWORD ENTRY "
            show = '*'

        elif type_password == 'hide_password':

            " INSTANCES THE TYPE RETURN "
            self.__password_status = 'show_password'
            type_return = self.__password_status

            " CATCH THE 'show_password' IMAGE "
            password_eye = self.__closed_eye_image
            
            " INSTANCES THE 'show' VARIABLE WHICH WILL BE USED IN THE PASSWORD ENTRY "
            show = ''


        " WIDGETS - START "

        " CREATE THE NEW PASSWORD ENTRY "
        self.__password_entry = Entry(login_password_frame, font=('arial', 15, 'bold'), width=20, show=show)
        self.__password_entry.place(x=170, y=143)

        " CREATES THE BUTTON WIDGET WITH THE NEW IMAGE "
        self.__show_hide_password_button = Button(password_frame, image=password_eye, 
        bg='dark salmon', activebackground='salmon', activeforeground='white',
        command=lambda: self.__returnOption(type_return))
        self.__show_hide_password_button.place(x=410, y=138)

        " INSERTS THE PASSWORD "
        self.__password_entry.insert(0, password)

        " WIDGETS - END "


    def __returnOption(self, type_return, **kws):
        
        " this method returns the input of the user "

        " CATCH THE VALUE OF 'password_status', 'login' OR/AND 'password' IF THE USER INFORM IT "
        login = kws.get('login')
        password_status = kws.get('password_status')
        password = kws.get('password')

        " INSTANCES THE WINDOW "
        window = self.__window


        if type_return == 'send_instagram_login':
            
            " CATCH THE DIRECTORY WHICH HAS THE 'return_email.txt' FILE " 
            file_directory = 'controller/communication_file/return_email.txt'
            file_content = f'send_instagram_login-{login}-{password}'

            file_writer = FileWriter(file_content=file_content, file_directory=file_directory)
            file_writer.startFileWriter()
            
            " SHOWS A MESSAGE "
            type_message = 'info'
            title_message = 'Just a minute'
            text_message = 'We are verifying your Instagram account now.\nPlease wait a few seconds.\nYou can close this window'

            message = Message(type_message, title_message, text_message)
            message.startMessage()

            window.destroy()

        else:

            self.__shows_hide_password(type_password=type_return)


    def __startErrorHandling(self, type_return):

        " this method verify if the typed information is valid "

        " INSTANCES THE TYPE RETURN "
        type_return = type_return

        " INSTANCES THE VARIABLES WHICH WILL GET THE LOGIN AND PASSWORD OF THE USER "
        login_entry = self.__login_entry.get()
        password_entry = self.__password_entry.get()

        " INSTANCES THE ERROR HANDLING "
        error_handling = ErrorHandling(login_entry=login_entry, password_entry=password_entry)
        return_error_handling = error_handling.startEmailErrorHandling()


        if return_error_handling == True:
            self.__returnOption(type_return, login=login_entry, password=password_entry)

        else:
            
            " SHOWS A MESSAGE "
            type_message = 'warning'
            title_message = 'Warning'
            text_message = 'One or more information invalid'

            message = Message(type_message=type_message, title_message=title_message, text_message=text_message)
            message.startMessage()


    def startSendButton(self):

        " this method show the button which will return the information writted in the entries "

        " INSTANCES THE MESSAGE "
        send_message = 'SEND'

        " INSTANCES THE WIDGETS "
        send_frame = self.__email_frame

        " INSTANCES THE TYPE RETURN "
        type_return = 'send_instagram_login'

        send_button = Button(send_frame, text=send_message, font=('arial', 15, 'bold'), 
        bg='dark salmon', activebackground='salmon', activeforeground='white',
        command=lambda:self.__startErrorHandling(type_return))
        send_button.place(x=200, y=205)


    def startPasswordButton(self):

        " this method show/hide the writted password "

        " INSTANCES THE VARIABLE WHICH CATCH THE EYE IMAGE "
        password_eye = self.__open_eye_image

        " INSTANCES THE FRAME "
        password_frame = self.__email_frame

        " INSTANCES THE TYPE RETURN "
        type_return = self.__password_status

        " INSTANCES THE WIDGET "
        self.__show_hide_password_button = Button(password_frame, image=password_eye, 
        bg='dark salmon', activebackground='salmon', activeforeground='white',
        command=lambda: self.__returnOption(type_return))
        self.__show_hide_password_button.place(x=410, y=138)


    def startEntries(self):

        " this method shows the login and password entries "

        " INSTANCES THE LABEL TEXTS "
        login_text = 'Login'
        password_text = 'Password'

        " INSTANCES THE WIDGETS "
        login_password_frame = self.__email_frame

        login_label = Label(login_password_frame, text=login_text, font=('arial', 20, 'bold'), bg='floral white')
        login_label.place(x=20, y=90)

        self.__login_entry = Entry(login_password_frame, font=('arial', 15, 'bold'), width=30)
        self.__login_entry.place(x=120, y=93)

        password_label = Label(login_password_frame, text=password_text, font=('arial', 20, 'bold'), bg='floral white')
        password_label.place(x=20, y=140)

        self.__password_entry = Entry(login_password_frame, font=('arial', 15, 'bold'), width=20, show='*')
        self.__password_entry.place(x=170, y=143)


    def startMessageLabel(self):

        " this method show the message writted above the login and password entries "
        
        " INSTANCES THE MESSAGE "
        message_text = 'Please, inform your\nlogin and password of your Instagram'

        " INSTANCES THE WIDGETS "
        message_frame = self.__email_frame

        message_label = Label(message_frame, text=message_text, font=('arial', 15, 'bold'), bg='floral white')
        message_label.place(x=70, y=17)