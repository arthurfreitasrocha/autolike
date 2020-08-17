# TKINTER LIBRARY
from tkinter import *

# MODEL
from model.bots import LikePhotosByHashtag

# VIEW
from view.Message import Message

# CONTROLLER
from controller.file_manipulator import FileWriter


class ReturnEmailOption:

    def __init__(self):
        
        pass

    
    def startReturnOption(self):

        pass

class ReturnOptionOne:

    def __init__(self, window, hashtag_entry, n_likes_entry):
        
        self.__window = window
        self.__hashtag_entry = hashtag_entry
        self.__n_likes_entry = n_likes_entry


    def startReturnOption(self, type_return):

        " this method returns the input of the user "

        " INSTANCES THE VARIABLES "
        window = self.__window
        hashtag_entry = self.__hashtag_entry
        n_likes_entry = self.__n_likes_entry
        type_return = type_return

        if type_return == True:

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

            " BOT "
            start_like_photos_by_hashtag = LikePhotosByHashtag(hashtag_entry, n_likes_entry)
            return_like_photos = start_like_photos_by_hashtag.startLikePhotosByHashtag()

            if return_like_photos == True:
                
                file_directory = 'controller/communication_file/return_option_one.txt'
                file_content = f'True-{n_likes_entry}'

                file_writer = FileWriter(file_content, file_directory)
                file_writer.startFileWriter()

            else:

                error = return_like_photos[1]

                file_directory = 'controller/communication_file/return_option_one.txt'
                file_content = f'False-{error}'

                file_writer = FileWriter(file_content, file_directory)
                file_writer.startFileWriter()

        elif type_return == False:

            " SHOWS A MESSAGE "
            type_message = 'warning'
            title_message = 'Warning'
            text_message = 'One or more information invalid'

            message = Message(type_message=type_message, title_message=title_message, text_message=text_message)
            message.startMessage()

class ReturnOptionTwo:

    def __init__(self):
        
        pass


    def startReturnOption(self):

        pass

class ReturnOptionThree:

    def __init__(self):
        
        pass


    def startReturnOption(self):

        pass