# TKINTER LIBRARY
from tkinter import *

# IMAGE LIBRARY
from PIL import ImageTk, Image

# MODEL
from model.ErrorHandling import ErrorHandlingOptionOne
from model.ErrorHandling import ErrorHandlingOptionTwo
from model.ErrorHandling import ErrorHandlingOptionThree

# VIEW
from view.user_manipulation.start_user_manipulation import UserManipulation
from view.Widgets import Widgets
from view.LogoFragment import LogoFragment
from view.WindowConfiguration import WindowConfiguration
from view.Message import Message

# CONTROLLER
from controller.clear_return import ClearReturn

from controller.file_manipulator import FileReader
from controller.file_manipulator import FileWriter

class OptionOne:

    """
    this class creates the Option One window
    """

    def __init__(self, app_version):
        
        " INSTANCES THE APP VERSION "
        self.__app_version = app_version

        " INSTANCES THE WINDOW "
        self.__window = Tk()

        " INSTANCES THE WIDGET CLASS "
        self.__widget = Widgets(self.__window)


    def on_close(self):

        """
        this method overwrites the on_close native method
        """

        window = self.__window

        window.destroy()

        self.readReturn(window_closed=True)


    def readReturn(self, **kws):

        " this method just read the return of 'OptionOneFragments.py' "

        window_closed = kws.get('window_closed')

        file_directory = 'controller/communication_file/return_option_one.txt'

        if window_closed == True:

            file_content = 'window_closed'

            file_writer = FileWriter(file_content=file_content, file_directory=file_directory)
            file_writer.startFileWriter()

        file_reader = FileReader(file_directory=file_directory)
        file_content = file_reader.startFileReader()

        return file_content


    def flag(self, flag, **kws):

        " INSTANCES THE WINDOW "
        window = self.__window

        if flag == 'success':

            n_likes = kws.get('n_likes')

            " SHOW A MESSAGE "
            type_message = 'info'
            title_message = 'Success'
            text_message = f'Success! {n_likes} photos liked'

            message = Message(type_message, title_message, text_message)
            message.startMessage()

            window.destroy()

        elif flag == 'failed':

            error = kws.get('error')

            " SHOW A MESSAGE "
            type_message = 'error'
            title_message = 'Failed'
            text_message = f'Some things get wrong.\nCall the programmer of this software to solve this.\nError: {error}'

            message = Message(type_message, title_message, text_message)
            message.startMessage()

            window.destroy()


    def startInterface(self, **kws):

        " this method starts the 'OptionOne' interface "

        flag = kws.get('flag')
        n_likes = kws.get('n_likes')
        error = kws.get('error')
        
        " INSTANCES THE VARIABLES "
        app_version = self.__app_version
        window = self.__window
        widget = self.__widget

        start_message = 'Start'
        hashtag_text = 'Hashtag'
        n_likes_text = 'Nº Likes'


        " INSTANCES THE FRAGMENTS OF THE WINDOW "
        logo_fragment = LogoFragment(window)

        """
        FRAGMENTS - START
        """

        " CREATES THE LOGO IN THE WINDOW "
        logo_image = ImageTk.PhotoImage(Image.open('view/images/logo.png')) # LOGO APP
        logo_fragment.startLogoAppFragment(logo_image)


        " INSTANCES THE FRAME "
        hashtag_frame = widget.startFrame(500, 300, 'floral white', TOP)

        " INSTANCES THE LABELS "
        widget.startLabel(hashtag_frame, hashtag_text, 'arial-18-bold', 'floral white', 20, 30)
        widget.startLabel(hashtag_frame, n_likes_text, 'arial-18-bold', 'floral white', 20, 80)
        
        " INSTANCES THE ENTRIES "
        self.__hashtag_entry = widget.startEntry(hashtag_frame, 'arial-18-bold', 25, 150, 33)
        self.__n_likes_entry = widget.startEntry(hashtag_frame, 'arial-18-bold', 25, 150, 83)

        " INSTANCES THE BUTTON "
        widget.startButton(hashtag_frame, start_message, 'arial-15-bold', 'dark salmon', 'salmon', 'white', 'error-handling-option-one', 240, 140, hashtag_entry=self.__hashtag_entry, n_likes_entry=self.__n_likes_entry)

        """
        FRAGMENTS - END
        """


        " CONFIGURES THE WINDOW "
        window_configuration = WindowConfiguration(window, width=500, height=300, width_distance=3, height_distance=4)
        window_configuration = window_configuration.fullWindowConfiguration()

        " CATCH THE WINDOW GEOMETRY AND THE APP TITLE WITH THE 'window_configuration' RETURNS - lines 32, 33 "
        window_geometry = window_configuration['window_geometry']
        app_title = f'AutoLike - Version: {app_version}' # APP TITLE

        " FINAL WINDOW CONFIGURATION "
        window.protocol("WM_DELETE_WINDOW", self.on_close)
        window.title(app_title)
        window.resizable(width=False, height=False)
        window.geometry(window_geometry)

        if flag == 'success':
            self.flag(flag=flag, n_likes=n_likes)
        
        elif flag == 'failed':
            self.flag(flag=flag, error=error)

        window.mainloop()


class OptionTwo:

    def __init__(self, app_version):

        """
        this class creates the Option Two window
        """

        name_file = 'controller/communication_file/return_user_manipulation/return_window_selected.txt'

        clear_return = ClearReturn(name_file)
        clear_return.startClearReturn()

        " INSTANCES THE APP VERSION "
        self.__app_version = app_version

        " INSTANCES THE WINDOW "
        self.__window = Tk()

        " INSTANCES THE WIDGET CLASS "
        self.__widget = Widgets(self.__window)


    def on_close(self):

        window = self.__window

        window.destroy()

        self.readReturn(window_closed=True)


    def readReturn(self, **kws):

        " this method just read the return of 'OptionTwoFragments.py' "

        window_closed = kws.get('window_closed')

        file_directory = 'controller/communication_file/return_option_two.txt'

        if window_closed == True:

            file_content = 'window_closed'

            file_writer = FileWriter(file_content=file_content, file_directory=file_directory)
            file_writer.startFileWriter()

        file_reader = FileReader(file_directory=file_directory)
        file_content = file_reader.startFileReader()

        return file_content


    def flag(self, flag, **kws):

        " show a success/fail message "

        " INSTANCES THE WINDOW "
        window = self.__window

        if flag == 'success':
            
            n_profiles = kws.get('n_profiles')
            n_likes = kws.get('n_likes')

            " SHOW A MESSAGE "
            type_message = 'info'
            title_message = 'Success'
            text_message = f'Success! {n_likes} photos liked from {n_profiles} Instagram profiles'

            message = Message(type_message, title_message, text_message)
            message.startMessage()

            window.destroy()

        elif flag == 'failed':

            error = kws.get('error')

            " SHOW A MESSAGE "
            type_message = 'error'
            title_message = 'Failed'
            text_message = f'Some things get wrong.\nCall the programmer of this software to solve this.\nError: {error}'

            message = Message(type_message, title_message, text_message)
            message.startMessage()

            window.destroy()


    def startInterface(self, **kws):

        " this method starts the 'OptionTwo' interface "

        flag = kws.get('flag')
        n_profiles = kws.get('n_profiles')
        n_likes = kws.get('n_likes')
        error = kws.get('error')
        
        " INSTANCES THE VARIABLES "
        app_version = self.__app_version
        window = self.__window
        widget = self.__widget

        message_text = 'Inform the amount of photos\nwill be liked of each user'
        text_button = 'Send'

        " INSTANCES THE FRAGMENTS OF THE WINDOW "
        logo_fragment = LogoFragment(window)

        " INSTANCES THE USER MANIPULATION CLASS "
        user_manipulation = UserManipulation(window)
        user_manipulation.startUserManipulation()

        """
        FRAGMENTS - START
        """

        " CREATES THE LOGO IN THE WINDOW "
        logo_image = ImageTk.PhotoImage(Image.open('view/images/logo.png')) # LOGO APP
        logo_fragment.startLogoAppFragment(logo_image)


        " INSTANCES THE FRAME "
        message_frame = widget.startFrame(500, 150, 'floral white', TOP)

        " INSTANCES THE LABEL "
        widget.startLabel(message_frame, message_text, 'arial-15-bold', 'floral white', 110, 15)

        " INSTANCES THE ENTRY "
        self.__send_entry = widget.startEntry(message_frame, 'arial-15-bold', 10, 150, 98)

        " INSTANCES THE BUTTON "
        widget.startButton(message_frame, text_button, 'arial-15-bold', 'dark salmon', 'salmon', 'white', 'error-handling-option-two', 280, 90, n_photos=self.__send_entry)

        """
        FRAGMENTS - END
        """


        " CONFIGURES THE WINDOW "
        window_configuration = WindowConfiguration(window, width=500, height=400, width_distance=3, height_distance=5)
        window_configuration = window_configuration.fullWindowConfiguration()

        " CATCH THE WINDOW GEOMETRY AND THE APP TITLE WITH THE 'window_configuration' RETURNS - lines 32, 33 "
        window_geometry = window_configuration['window_geometry']
        app_title = f'AutoLike - Version: {app_version}' # APP TITLE

        " FINAL WINDOW CONFIGURATION "
        window.protocol("WM_DELETE_WINDOW", self.on_close)
        window.title(app_title)
        window.resizable(width=False, height=False)
        window.geometry(window_geometry)

        if flag == 'success':
            self.flag(flag=flag, n_profiles=n_profiles, n_likes=n_likes)
        
        elif flag == 'failed':
            self.flag(flag=flag, error=error)

        window.mainloop()


class OptionThree:

    def __init__(self, app_version):

        """
        this class creates the Option Three window
        """

        name_file = 'controller/communication_file/return_user_manipulation/return_window_selected.txt'

        clear_return = ClearReturn(name_file)
        clear_return.startClearReturn()

        " INSTANCES THE APP VERSION "
        self.__app_version = app_version

        " INSTANCES THE WINDOW "
        self.__window = Tk()

        " INSTANCES THE WIDGET "
        self.__widget = Widgets(self.__window)


    def on_close(self):

        """
        this method overwrites the on_close native method
        """

        window = self.__window

        window.destroy()

        self.readReturn(window_closed=True)


    def readReturn(self, **kws):

        " this method just read the return of 'OptionThreeFragments.py' "

        window_closed = kws.get('window_closed')

        file_directory = 'controller/communication_file/return_option_three.txt'

        if window_closed == True:

            file_content = 'window_closed'

            file_writer = FileWriter(file_content=file_content, file_directory=file_directory)
            file_writer.startFileWriter()

        file_reader = FileReader(file_directory=file_directory)
        file_content = file_reader.startFileReader()

        return file_content


    def flag(self, flag, **kws):

        " show a success/fail message "

        " INSTANCES THE WINDOW "
        window = self.__window

        if flag == 'success':
            
            n_profiles = kws.get('n_profiles')
            n_likes = kws.get('n_likes')

            " SHOW A MESSAGE "
            type_message = 'info'
            title_message = 'Success'
            text_message = f'Success! {n_likes} photos liked from {n_profiles} Instagram profiles'

            message = Message(type_message, title_message, text_message)
            message.startMessage()

            window.destroy()

        elif flag == 'failed':

            error = kws.get('error')

            " SHOW A MESSAGE "
            type_message = 'error'
            title_message = 'Failed'
            text_message = f'Some things get wrong.\nCall the programmer of this software to solve this.\nError: {error}'

            message = Message(type_message, title_message, text_message)
            message.startMessage()

            window.destroy()


    def startInterface(self, **kws):

        " this method starts the 'OptionTwo' interface "

        flag = kws.get('flag')
        n_profiles = kws.get('n_profiles')
        n_likes = kws.get('n_likes')
        error = kws.get('error')

        " INSTANCES THE VARIABLES "
        app_version = self.__app_version
        window = self.__window
        widget = self.__widget

        send_message = 'Send'
        text = 'Write the message which will be sended'

        " INSTANCES THE FRAGMENTS OF THE WINDOW "
        logo_fragment = LogoFragment(window)
        user_manipulation = UserManipulation(window)
        user_manipulation.startUserManipulation()

        """
        FRAGMENTS - START
        """

        " CREATES THE LOGO IN THE WINDOW "
        logo_image = ImageTk.PhotoImage(Image.open('view/images/logo.png')) # LOGO APP
        logo_fragment.startLogoAppFragment(logo_image)


        " INSTANCES THE FRAME "
        message_frame = widget.startFrame(500, 300, 'floral white', TOP)

        " INSTANCES THE LABEL "
        widget.startLabel(message_frame, text, 'arial-15-bold', 'floral white', 50,15)

        " INSTANCES THE TEXT "
        self.__message_text = widget.startText(message_frame, 'arial-15-bold', 41, 7, 20, 60)

        " INSTANCES THE BUTTON "
        widget.startButton(message_frame, send_message, 'arial-15-bold', 'dark salmon', 'salmon', 'white', 'error-handling-option-three', 220, 245, writted_text=self.__message_text)

        """
        FRAGMENTS - END
        """

        " CONFIGURES THE WINDOW "
        window_configuration = WindowConfiguration(window, width=500, height=550, width_distance=3, height_distance=5)
        window_configuration = window_configuration.fullWindowConfiguration()

        " CATCH THE WINDOW GEOMETRY AND THE APP TITLE WITH THE 'window_configuration' RETURNS - lines 32, 33 "
        window_geometry = window_configuration['window_geometry']
        app_title = f'AutoLike - Version: {app_version}' # APP TITLE

        " FINAL WINDOW CONFIGURATION "
        window.protocol("WM_DELETE_WINDOW", self.on_close)
        window.title(app_title)
        window.resizable(width=False, height=False)
        window.geometry(window_geometry)

        if flag == 'success':
            self.flag(flag=flag, n_profiles=n_profiles, n_likes=n_likes)
        
        elif flag == 'failed':
            self.flag(flag=flag, error=error)

        window.mainloop()