# TKINTER LIBRARY
from tkinter import *

# MODEL
from model.ErrorHandling import ErrorHandlingEmail
from model.ErrorHandling import ErrorHandlingOptionOne
from model.ErrorHandling import ErrorHandlingOptionTwo

from model.ReturnOption import ReturnOptionOne

# VIEW
from view.Message import Message

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


    def startLabel(self):

        pass


    def startButton(self, frame, hashtag_entry, n_likes_entry, text, font, background, activebackground, activeforeground, command, x, y):

        def startCommand(command):

            " INSTANCES MORE VARIABLES "
            window = self.__window

            command = command

            ButtonCommands(command, window=window, hashtag_entry=self.__hashtag_entry, n_likes_entry=self.__n_likes_entry)


        " INSTANCES THE VARIABLES "
        frame = frame
        self.__hashtag_entry = hashtag_entry
        self.__n_likes_entry = n_likes_entry
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


    def startEntry(self, frame, font, width):

        " INSTANCES THE VARIABLES "
        frame = frame
        font = font.split('-')
        width = width


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
        if command == 'error-handling-option-one':
            
            window = kws.get('window')
            hashtag_entry = kws.get('hashtag_entry')
            n_likes_entry = kws.get('n_likes_entry')

            hashtag_entry = hashtag_entry.get()
            n_likes_entry = n_likes_entry.get()

            self.startErrorHandlingOptionOne(window, hashtag_entry, n_likes_entry)


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