# TKINTER LIBRARY
from tkinter import *

# MODEL
from model.bots import LikePhotosByHashtag

# VIEW
from view.Message import Message

# CONTROLLER
from controller.file_manipulator import FileReader
from controller.file_manipulator import FileWriter

# EXTRA LIBRARY
from random import shuffle
import os

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

    def __init__(self, window, n_photos, users_selected):
        
        self.__window = window
        self.__n_photos = n_photos

        " CATCH THE USERS SELECTED "
        file_directory = 'controller/communication_file/return_user_manipulation/return_users_selected.txt'
        file_content = ''

        file_reader = FileReader(file_directory=file_directory)
        file_content = file_reader.startFileReader()

        self.__users_selected = file_content


    def startReturnOption(self):

        " INSTANCE THE VARIABLES "
        n_photos = self.__n_photos
        users_selected = self.__users_selected

        " WRITE THE OPTION TWO RETURN " 
        file_directory = 'controller/communication_file/return_option_two.txt'
        file_content = f'send-random-{n_photos}'

        file_writer = FileWriter(file_content=file_content, file_directory=file_directory)
        file_writer.startFileWriter()

        " WRITE THE SELECTED USERS "
        file_directory = 'controller/communication_file/return_option_two/return_users_selected.txt'
        file_content = users_selected

        file_writer = FileWriter(file_content=file_content, file_directory=file_directory)
        file_writer.startFileWriter()

        " SHOWS A MESSAGE "
        type_message = 'info'
        title_message = 'Logging into Instagram'
        text_message = 'We are logging into Instagram\nYou can close this window'

        message = Message(type_message=type_message, title_message=title_message, text_message=text_message)
        message.startMessage()


class ReturnOptionThree:

    def __init__(self, window, writted_text):
        
        self.__window = window
        self.__writted_text = writted_text


    def startReturnOption(self, type_return):

        " this method returns the input of the user "

        " INSTANCES THE VARIABLES "
        window = self.__window
        writted_text = self.__writted_text
        type_return = type_return


        if type_return == True:

            " WRITE THE OPTION THREE RETURN " 
            file_directory = 'controller/communication_file/return_option_three.txt'
            file_content = f'send-{writted_text}'

            file_writer = FileWriter(file_content=file_content, file_directory=file_directory)
            file_writer.startFileWriter()

            " SHOWS A MESSAGE "
            type_message = 'info'
            title_message = 'Logging into Instagram'
            text_message = 'We are logging into Instagram\nYou can close this window'

            message = Message(type_message=type_message, title_message=title_message, text_message=text_message)
            message.startMessage()

            window.destroy()

        elif type_return == False:

            " SHOWS A MESSAGE "
            type_message = 'warning'
            title_message = 'Warning'
            text_message = 'Please, write a message.'

            message = Message(type_message=type_message, title_message=title_message, text_message=text_message)
            message.startMessage()


class ReturnUserManipulationOption:

    def __init__(self, window):
        
        " this class is responsible to return the users manipulated, how to accrescent or delete users "

        " INSTANCES THE WINDOW "
        self.__window = window


    def startReturnOption(self, type_return, **kws):

        " this method verify the return and work based in each return "

        " INSTANCES THE WINDOW "
        window = self.__window

        " CATCH THE CURRENT USER "
        file_directory = 'controller/system_files/user_instagram.txt'

        file_reader = FileReader(file_directory=file_directory)
        file_content = file_reader.startFileReader()

        user = file_content


        if type_return == 'button-back':
            window.destroy()

        elif type_return == 'select-all-users':

            checkbutton_value = kws.get('checkbutton_value')

            if checkbutton_value == 1:

                " SHOWS A MESSAGE "
                type_message = 'info'
                title_message = 'All users selecteds'
                text_message = 'Success! All users selecteds'

                message = Message(type_message=type_message, title_message=title_message, text_message=text_message)
                message.startMessage()

        elif type_return == 'select-users':

            " INSTANCES VARIABLES"
            users_selected = kws.get('users_selected')
            flag = kws.get('flag')

            if flag == 'no-user-selected':

                " SHOWS A ERROR MESSAGE "
                type_message = 'error'
                title_message = 'Error'
                text_message = 'Please, select at least one profile'

                message = Message(type_message=type_message, title_message=title_message, text_message=text_message)
                message.startMessage()

            else:

                " CATCH THE USERS OF THE MAIN DATABASE "
                file_directory = f'controller/users/{user}/database.txt'

                file_reader = FileReader(file_directory=file_directory)
                file_content = file_reader.startFileReader()

                second_database = file_content.split('-')

                " RANDOMIZE THE USERS SELECTED "
                shuffle(users_selected)


                " CATCH THE NAME OF THE SELECTED USERS "
                users_selected_text = ''
                i = 0
                for current_user in users_selected:

                    if i == 0:
                        users_selected_text += current_user

                    else:
                        users_selected_text += f'-{current_user}'

                    i += 1


                " WRITE THE USERS SELECTEDS IN THE SECOND DATABASE, WHICH WILL USED LATER "
                file_directory = f'controller/users/{user}/second_database.txt'
                file_content = users_selected_text

                file_writer = FileWriter(file_content=file_content, file_directory=file_directory)
                file_writer.startFileWriter()

                " WRITE THE USERS SELECTEDS IN THE COMMUNICATION FILE "
                file_directory = f'controller/communication_file/return_user_manipulation/return_users_selected.txt'
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

        elif type_return == 'delete-users':

            " CATCH THE USERS OF THE SECOND DATABASE "
            file_directory = f'controller/users/{user}/second_database.txt'

            file_reader = FileReader(file_directory=file_directory)
            file_content = file_reader.startFileReader()

            second_database = file_content.split('-')


            " INSTAGRAM USERS SELECTED BY THE USER "
            users_selected = kws.get('users_selected')
            checkbutton_value = kws.get('checkbutton_value')

            " CATCH THE NAME OF THE USERS WILL BE REMOVED "
            users_will_removed = []
            for user_second_database in second_database:

                for user_selected in users_selected:
                    if user_second_database == user_selected:
                        
                        users_will_removed.append(user_second_database)
                        break


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