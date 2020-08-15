# TKINTER LIBRARY
from tkinter import *

# MODEL
from model.start_error_handling import ErrorHandling

# VIEW
from view.Message import Message

# CONTROLLER
from controller.file_writer import FileWriter

class OptionOneFragments:

    """
    this class returns the one option window fragments
    """

    def __init__(self, window):
        
        " INSTANCES THE WINDOW "
        self.__window = window

        " INSTANCES THE FRAME "
        self.__hashtag_frame = Frame(window, width=500, height=300, bg='floral white')
        self.__hashtag_frame.pack(side=TOP)


    def __returnOption(self, hashtag_entry, n_likes_entry):
        
        " this method returns the input of the user "

        " INSTANCES THE WINDOW "
        window = self.__window

        " VARIABLES WHICH WILL USED "
        hashtag_entry = hashtag_entry
        n_likes_entry = n_likes_entry
        
        " CATCH THE DIRECTORY WHICH HAS THE 'return_option_one.txt' FILE " 
        file_directory = 'controller/communication_file/return_option_one.txt'
        file_content = f'{hashtag_entry}-{n_likes_entry}'

        file_writer = FileWriter(file_content=file_content, file_directory=file_directory)
        file_writer.startFileWriter()

        " SHOWS A MESSAGE "
        type_message = 'info'
        title_message = 'Logging into Instagram'
        text_message = 'We are logging into Instagram\nYou can close this window'

        message = Message(type_message=type_message, title_message=title_message, text_message=text_message)
        message.startMessage()

        window.destroy()


    def __startErrorHandling(self):

        " this method verify if the typed information is valid "

        " INSTANCES THE VARIABLES WHICH WILL GET THE LOGIN AND PASSWORD OF THE USER "
        hashtag_entry = self.__hashtag_entry.get()
        n_likes_entry = self.__n_likes_entry.get()

        " INSTANCES THE ERROR HANDLING "
        error_handling = ErrorHandling(hashtag_entry=hashtag_entry, n_likes_entry=n_likes_entry)
        return_error_handling = error_handling.startOptionOneErrorHandling()

        if return_error_handling == True:
            self.__returnOption(hashtag_entry=hashtag_entry, n_likes_entry=n_likes_entry)

        else:
            
            " SHOWS A MESSAGE "
            type_message = 'warning'
            title_message = 'Warning'
            text_message = 'One or more information invalid'

            message = Message(type_message=type_message, title_message=title_message, text_message=text_message)
            message.startMessage()


    def startButton(self):

        " this method show the button which will return the information writted in the entries "

        " INSTANCES THE MESSAGE "
        start_message = 'Start'

        " INSTANCES THE WIDGETS "
        start_frame = self.__hashtag_frame

        start_button = Button(start_frame, text=start_message, font=('arial', 15, 'bold'), 
        bg='dark salmon', activebackground='salmon', activeforeground='white',
        command=self.__startErrorHandling)
        start_button.place(x=240, y=140)


    def startEntries(self):

        " this method shows the hashtag and number of likes entries "

        " INSTANCES THE VARIABLES WHICH WILL BE USED IN THE WIDGETS "
        hashtag_text = 'Hashtag'
        n_likes_text = 'Nº Likes'

        " INSTANCES THE WIDGETS "
        hashtag_frame = self.__hashtag_frame

        hashtag_label = Label(hashtag_frame, text=hashtag_text, font=('arial', 20, 'bold'), bg='floral white')
        hashtag_label.place(x=20, y=30)

        self.__hashtag_entry = Entry(hashtag_frame, font=('arial', 18, 'bold'), width=25)
        self.__hashtag_entry.place(x=150, y=33)

        n_likes_label = Label(hashtag_frame, text=n_likes_text, font=('arial', 20, 'bold'), bg='floral white')
        n_likes_label.place(x=20, y=80)

        self.__n_likes_entry = Entry(hashtag_frame, font=('arial', 18, 'bold'), width=25)
        self.__n_likes_entry.place(x=150, y=83)