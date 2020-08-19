# TKINTER LIBRARY
from tkinter import *

# MODEL
from model.ErrorHandling import ErrorHandlingEmail
from model.ErrorHandling import ErrorHandlingOptionOne
from model.ErrorHandling import ErrorHandlingOptionTwo

from model.ReturnOption import ReturnOptionOne
from model.ReturnOption import ReturnUserManipulationOption

# VIEW
from view.Message import Message

# CONTROLLER
from controller.file_manipulator import FileReader
from controller.file_manipulator import FileWriter

class Widgets:

    def __init__(self, window):

        """
        this class was created to decrease the graphical interface code
        by passing smaller parameters

        this class was created exclusively to AutoLike
        """
        
        " INSTANCES THE WINDOW "
        self.__window = window


    def startFrame(self, width, height, background, side):

        " INSTANCES THE VARIABLES "
        window = self.__window
        width = width
        height = height
        background = background
        side = side

        " INSTANCES THE FRAME "
        frame = Frame(window, width=width, height=height, bg=background)
        frame.pack(side=side)

        return frame


    def startLabel(self, frame, text, font, background, x, y):

        " INSTANCES THE VARIABLES "
        frame = frame
        text = text
        font = font.split('-')
        background = background
        x = x
        y = y

        " INSTANCES THE LABEL "
        label = Label(frame, text=text, font=(font[0], font[1], font[2]), bg=background)
        label.place(x=x, y=y)

        return label


    def startEntry(self, frame, font, width, x, y):

        " INSTANCES THE VARIABLES "
        frame = frame
        font = font.split('-')
        width = width
        x = x
        y = y

        " INSTANCES THE FRAME "
        entry = Entry(frame, font=(font[0], font[1], font[2]), width=width)
        entry.place(x=x, y=y)

        return entry


    def startButton(self, frame, text, font, background, activebackground, activeforeground, command, x, y, **kws):

        def startCommand(command):

            " INSTANCES THE WINDOW "
            window = self.__window

            command = command
            
            if command == 'button-back' or command == 'button-select-users':
                ButtonCommands(command, window=window)

            elif command == 'button-view-users' or command == 'button-delete-users':

                " CATCH THE CURRENT USER "
                file_directory = 'controller/system_files/user_instagram.txt'

                file_reader = FileReader(file_directory)
                file_content = file_reader.startFileReader()

                user = file_content

                " CATCH ALL THE USERS "
                file_directory = f'controller/users/{user}/second_database.txt'

                file_reader = FileReader(file_directory)
                file_content = file_reader.startFileReader()

                all_users = file_content


                if all_users == '':
                    flag = 'no-user-selected'
                    
                else:
                    flag = ''

                ButtonCommands(command, window=window, flag=flag)

            elif command == 'select-users' or command == 'delete-users':

                self.__listbox_users = kws.get('listbox_users')
                self.__checkbutton_value = kws.get('checkbutton_value')
                users_selected = self.__listbox_users.curselection()
                checkbutton_value = self.__checkbutton_value.get()

                ButtonCommands(command, window=window, users_selected=users_selected, checkbutton_value=checkbutton_value)

            elif command == 'error-handling-option-one':

                self.__hashtag_entry = kws.get('hashtag_entry')
                self.__n_likes_entry = kws.get('n_likes_entry')
                ButtonCommands(command, window=window, hashtag_entry=self.__hashtag_entry, n_likes_entry=self.__n_likes_entry)

        " INSTANCES THE VARIABLES "
        frame = frame
        text = text
        font = font.split('-')
        background = background
        activebackground = activebackground
        activeforeground = activeforeground
        command = command
        x = x
        y = y


        " INSTANCES THE BUTTON "
        button = Button(frame, text=text, font=(font[0], font[1], font[2]), bg=background, activebackground=activebackground, activeforeground=activeforeground,
        command=lambda:startCommand(command))
        button.place(x=x, y=y)

        return button


    def startCheckButton(self, frame, text, font, background, activebackground, activeforeground, variable, command, x, y):

        def startCommand(command):

            command = command
            
            if command == 'select-all-users':
                CheckButtonCommands(command, checkbutton=variable)

        " INSTANCES THE VARIABLES "
        frame = frame
        text = text
        font = font.split('-')
        background = background
        activebackground = activebackground
        activeforeground = activeforeground
        variable = variable
        command = command
        x = x
        y = y

        " INSTANCES THE CHECK BUTTON "
        checkbutton = Checkbutton(frame, text=text, font=(font[0], font[1], font[2]), bg=background, activebackground=activebackground, activeforeground=activeforeground,
        variable=variable, onvalue=1, offvalue=0, command=lambda:startCommand(command))
        checkbutton.place(x=x, y=y)


class ButtonCommands:

    def __init__(self, command, **kws):

        """
        this class is responsible to execute the command passed by parameter when the button is pressed

        the **kws avaliable is:
        window - hashtag_entry - n_likes_entry - users_selected - checkbutton_value - flag
        """

        " INSTANCES THE WINDOW "
        self.__window = kws.get('window')
        
        " INSTANCES THE COMMAND "
        command = command


        " VERIFY WHAT COMMAND IT'S TO EXECUTE "
        if command == 'button-back' or command == 'button-select-users' or command == 'button-view-users' or command == 'button-delete-users':

            " INSTANCES THE WINDOW "
            window = self.__window

            " INSTANCES THE TYPE BUTTON "
            type_button = command

            " INSTANCES THE FLAG "
            flag = kws.get('flag')

            self.startTypeButton(type_button, flag=flag)

        elif command == 'select-users' or command == 'delete-users':

            users_selected = kws.get('users_selected')
            checkbutton_value = kws.get('checkbutton_value')

            if command == 'select-users':
                self.startSelectDeleteUsers('select-users', users_selected, checkbutton_value)

            elif command == 'delete-users':
                self.startSelectDeleteUsers('delete-users', users_selected, checkbutton_value)

        elif command == 'error-handling-option-one':
            
            hashtag_entry = kws.get('hashtag_entry')
            n_likes_entry = kws.get('n_likes_entry')

            hashtag_entry = hashtag_entry.get()
            n_likes_entry = n_likes_entry.get()

            self.startErrorHandlingOptionOne(window, hashtag_entry, n_likes_entry)


    def startTypeButton(self, type_button, **kws):

        " this method execute the Back button or the Send button "

        " INSTANCES THE TYPE BUTTON "
        type_button = type_button

        " INSTANCES THE WINDOW "
        window = self.__window

        if type_button == 'button-back':

            return_back_option = ReturnUserManipulationOption(window)
            return_back_option.startReturnOption(type_button)

        else:

            flag = kws.get('flag')

            if type_button == 'button-select-users':
                
                file_directory = 'controller/communication_file/return_user_manipulation/return_selected_window.txt'
                file_content = 'window-select-users'

                file_writer = FileWriter(file_content, file_directory)
                file_writer.startFileWriter()

            elif type_button == 'button-view-users':

                if flag == 'no-user-selected':
                    " SHOWS A ERROR MESSAGE "
                    type_message = 'error'
                    title_message = 'Error'
                    text_message = 'Please, select at least one Instagram profile in\nSelect New Users option'

                    message = Message(type_message=type_message, title_message=title_message, text_message=text_message)
                    message.startMessage()

                else:

                    file_directory = 'controller/communication_file/return_user_manipulation/return_selected_window.txt'
                    file_content = 'window-view-users'

                    file_writer = FileWriter(file_content, file_directory)
                    file_writer.startFileWriter()

            elif type_button == 'button-delete-users':

                if flag == 'no-user-selected':
                    " SHOWS A ERROR MESSAGE "
                    type_message = 'error'
                    title_message = 'Error'
                    text_message = 'Please, select at least one Instagram profile in\nSelect New Users option'

                    message = Message(type_message=type_message, title_message=title_message, text_message=text_message)
                    message.startMessage()

                else:

                    file_directory = 'controller/communication_file/return_user_manipulation/return_selected_window.txt'
                    file_content = 'window-delete-users'

                    file_writer = FileWriter(file_content, file_directory)
                    file_writer.startFileWriter()

            if flag != 'no-user-selected':
                window.destroy()


    def startSelectDeleteUsers(self, type_manipulation, users_selected, checkbutton_value):

        type_manipulation = type_manipulation

        " INSTANCES THE WINDOW "
        window = self.__window

        " INSTANCES THE VARIABLES "
        users_selected = users_selected
        checkbutton_value = checkbutton_value

        " CATCH THE CURRENT USER "
        file_directory = 'controller/system_files/user_instagram.txt'

        file_reader = FileReader(file_directory)
        file_content = file_reader.startFileReader()

        user = file_content


        if type_manipulation == 'select-users':


            " CATCH ALL THE USERS "
            file_directory = f'controller/users/{user}/database.txt'

            file_reader = FileReader(file_directory)
            file_content = file_reader.startFileReader()

            all_users = file_content.split('-')

            if checkbutton_value == 1:
                users_selected = all_users

            else:
                
                """
                AS THE VALUES CHOSEN BY THE USER ARE RETURNED IN A NUMERIC TUPLE,
                HERE I HAD TO OBTAIN THE INDEX OF EACH INSTAGRAM ACCOUNT STORED IN THE DATABASE
                TO VERIFY WHICH ACCOUNT THE USER CHOSE TO ACCESS AND LIKES.
                """
                temp_list = []
                for user in all_users:
                    user_index = all_users.index(user)

                    for user_selected in users_selected:
                        user_selected_index = users_selected.index(user_selected)

                        if user_index == user_selected_index:
                            temp_list.append(user)
                            break

                users_selected = temp_list


            if checkbutton_value == 0 and users_selected == ():
                flag = 'no-user-selected'

            else:
                flag = ''

            return_back_option = ReturnUserManipulationOption(window)
            return_back_option.startReturnOption(type_manipulation, users_selected=users_selected, flag=flag)

        elif type_manipulation == 'delete-users':


            " CATCH ALL THE USERS "
            file_directory = f'controller/users/{user}/second_database.txt'

            file_reader = FileReader(file_directory)
            file_content = file_reader.startFileReader()

            all_users = file_content.split('-')

            if checkbutton_value == 1:
                users_selected = all_users

            else:
                
                """
                AS THE VALUES CHOSEN BY THE USER ARE RETURNED IN A NUMERIC TUPLE,
                HERE I HAD TO OBTAIN THE INDEX OF EACH INSTAGRAM ACCOUNT STORED IN THE DATABASE
                TO VERIFY WHICH ACCOUNT THE USER CHOSE TO ACCESS AND LIKES.
                """
                temp_list = []
                for user in all_users:
                    user_index = all_users.index(user)

                    for user_selected in users_selected:
                        user_selected_index = users_selected.index(user_selected)

                        if user_index == user_selected_index:
                            temp_list.append(user)
                            break

                users_selected = temp_list


            if checkbutton_value == 0 and users_selected == ():
                flag = 'no-user-selected'

            else:
                flag = ''

            return_back_option = ReturnUserManipulationOption(window)
            return_back_option.startReturnOption(type_manipulation, users_selected=users_selected, flag=flag)


    def startErrorHandlingOptionOne(self, window, hashtag_entry, n_likes_entry):

        " this method execute the Error Handling of the Option One "

        " INSTANCES THE VARIABLES "
        window = window
        hashtag_entry = hashtag_entry
        n_likes_entry = n_likes_entry

        " INSTANCES THE ERROR HANDLING CLASS "
        error_handling = ErrorHandlingOptionOne(hashtag_entry, n_likes_entry)
        return_error_handling = error_handling.startErrorHandling()

        " EXECUTE THE RETURN OPTION WITH THE RETURN OF THE ERROR HANDLING CLASS "
        if return_error_handling == True:

            return_option_one = ReturnOptionOne(window, hashtag_entry, n_likes_entry)
            return_option_one.startReturnOption(True)

        elif return_error_handling == False:
            
            return_option_one = ReturnOptionOne(window, hashtag_entry, n_likes_entry)
            return_option_one.startReturnOption(False)


class CheckButtonCommands:

    def __init__(self, command, **kws):

        """
        this class is responsible to execute the command passed by parameter when the button is pressed

        the **kws avaliable is:
        window
        """
        
        " INSTANCES THE COMMAND "
        command = command


        " VERIFY WHAT COMMAND IT'S TO EXECUTE "
        if command == 'select-all-users':
            
            " INSTANCES THE WINDOW "
            window = kws.get('window')
            
            " INSTANCES THE CHECK BUTTON "
            checkbutton = kws.get('checkbutton')
            checkbutton_value = checkbutton.get()

            self.startSelectAllUsers(window, checkbutton_value)


    def startSelectAllUsers(self, window, checkbutton_value):

        " INSTANCES THE WINDOW "
        window = window

        " INSTANCES THE CHECK BUTTON "
        checkbutton_value = checkbutton_value

        " INSTANCES THE TYPE BUTTON"
        type_button = 'select-all-users'

        select_all_users = ReturnUserManipulationOption(window)
        select_all_users.startReturnOption(type_button, checkbutton_value=checkbutton_value)