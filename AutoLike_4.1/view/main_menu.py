# TKINTER LIBRARY
from tkinter import *

# IMAGE LIBRARY
from PIL import ImageTk, Image

# VIEW
from view.LogoFragment import LogoFragment
from view.MainMenuFragments import MainMenuFragments
from view.WindowConfiguration import WindowConfiguration
from view.Message import Message

# CONTROLLER
from controller.file_reader import FileReader
from controller.file_writer import FileWriter

class MainMenu:

    """
    this class creates the AutoLike main menu
    """
    def __init__(self, user_instagram, app_version):

        self.__user_instagram = user_instagram
        self.__app_version = app_version


    def on_close(self):

        window = self.__window

        window.destroy()

        self.readReturn(window_closed=True)


    def readReturn(self, **kws):

        " this method just read the return of 'MainMenuFragments.py' "

        window_closed = kws.get('window_closed')

        file_directory = 'controller/communication_file/return_main_menu.txt'

        if window_closed == True:

            file_content = 'window_closed'

            file_writer = FileWriter(file_content=file_content, file_directory=file_directory)
            file_writer.startFileWriter()

        file_reader = FileReader(file_directory=file_directory)
        file_content = file_reader.startFileReader()

        return file_content


    def flag(self, flag):

        if flag == 'success':

            " SHOW A MESSAGE "
            type_message = 'info'
            title_message = 'Success'
            text_message = 'Your Instagram account has been changed with success!'

            message = Message(type_message, title_message, text_message)
            message.startMessage()

        elif flag == 'no_option':

            " SHOW A MESSAGE "
            type_message = 'error'
            title_message = 'Error'
            text_message = 'Please, select at least option'

            message = Message(type_message, title_message, text_message)
            message.startMessage()


    def startInterface(self, **kws):

        " this method starts the 'MainMenu' interface "

        flag = kws.get('flag')

        user_instagram = self.__user_instagram
        app_version = self.__app_version

        " INSTANCES THE WINDOW "
        self.__window = Tk()
        window = self.__window

        " INSTANCES THE FRAGMENTS OF THE WINDOW "
        logo_fragment = LogoFragment(window)
        fragments = MainMenuFragments(window)

        """
        FRAGMENTS - START
        """
        " CREATES THE LOGO IN THE WINDOW "
        logo_image = ImageTk.PhotoImage(Image.open('view/images/logo.png')) # LOGO APP
        logo_fragment.startLogoAppFragment(logo_image)

        " CREATES THE EMAIL TEXT AND EMAIL BUTTON "
        fragments.startEmailFragment(user_instagram)

        " CREATES THE SEPARATOR "
        fragments.startSeparator()

        " CREATES THE USER OPTIONS "
        fragments.startUserOptions()
        """
        FRAGMENTS - END
        """

        " CONFIGURES THE WINDOW "
        window_configuration = WindowConfiguration(window, width=500, height=570, width_distance=3, height_distance=13)
        window_configuration = window_configuration.fullWindowConfiguration()

        " CATCH THE WINDOW GEOMETRY AND THE APP TITLE WITH THE 'window_configuration' RETURNS "
        window_geometry = window_configuration['window_geometry']
        app_title = f'AutoLike - Version: {app_version}' # APP TITLE

        " FINAL WINDOW CONFIGURATION "
        window.protocol("WM_DELETE_WINDOW", self.on_close)
        window.title(app_title)
        window.resizable(width=False, height=False)
        window.geometry(window_geometry)

        if flag == 'success':
            self.flag(flag='success')

        elif flag == 'no_option':
            self.flag(flag='no_option')
        
        window.mainloop()
