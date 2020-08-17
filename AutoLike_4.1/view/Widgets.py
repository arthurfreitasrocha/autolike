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
            
            if command == 'button-back' or command == 'button-select-users' or command == 'button-view-users' or command == 'button-delete-users':
                ButtonCommands(command, window=window)

            elif command == 'error-handling-option-one':
                ButtonCommands(command, window=window, hashtag_entry=self.__hashtag_entry, n_likes_entry=self.__n_likes_entry)


        " INSTANCES THE VARIABLES "
        frame = frame
        self.__hashtag_entry = kws.get('hashtag_entry')
        self.__n_likes_entry = kws.get('n_likes_entry')
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
        window - hashtag_entry - n_likes_entry
        """
        
        " INSTANCES THE COMMAND "
        command = command


        " VERIFY WHAT COMMAND IT'S TO EXECUTE "
        if command == 'button-back' or command == 'button-select-users' or command == 'button-view-users' or command == 'button-delete-users':
            
            " INSTANCES THE WINDOW "
            window = kws.get('window')
            self.__window = window

            " INSTANCES THE TYPE BUTTON "
            type_button = command

            self.startTypeButton(type_button)

        elif command == 'error-handling-option-one':
            
            window = kws.get('window')
            hashtag_entry = kws.get('hashtag_entry')
            n_likes_entry = kws.get('n_likes_entry')

            hashtag_entry = hashtag_entry.get()
            n_likes_entry = n_likes_entry.get()

            self.startErrorHandlingOptionOne(window, hashtag_entry, n_likes_entry)


    def startTypeButton(self, type_button):

        " this method execute the Back button or the Send button "

        " INSTANCES THE TYPE BUTTON "
        type_button = type_button

        " INSTANCES THE WINDOW "
        window = self.__window

        if type_button == 'button-back':

            return_back_option = ReturnUserManipulationOption(window)
            return_back_option.startReturnOption(type_button)

        else:

            if type_button == 'button-select-users':
                
                file_directory = 'controller/communication_file/return_user_manipulation/return_selected_window.txt'
                file_content = 'window-select-users'

                file_writer = FileWriter(file_content, file_directory)
                file_writer.startFileWriter()

            elif type_button == 'button-view-users':

                file_directory = 'controller/communication_file/return_user_manipulation/return_selected_window.txt'
                file_content = 'window-view-users'

                file_writer = FileWriter(file_content, file_directory)
                file_writer.startFileWriter()

            elif type_button == 'button-delete-users':

                file_directory = 'controller/communication_file/return_user_manipulation/return_selected_window.txt'
                file_content = 'window-delete-users'

                file_writer = FileWriter(file_content, file_directory)
                file_writer.startFileWriter()

            window.destroy()


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
        window - hashtag_entry - n_likes_entry
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