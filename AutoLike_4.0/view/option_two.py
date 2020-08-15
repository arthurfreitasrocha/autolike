# TKINTER LIBRARY
from tkinter import *

# IMAGE LIBRARY
from PIL import ImageTk, Image

# VIEW
from view.LogoFragment import LogoFragment
from view.OptionTwoFragments import OptionTwoFragments
from view.WindowConfiguration import WindowConfiguration
from view.Message import Message

# CONTROLLER
from controller.file_reader import FileReader
from controller.file_writer import FileWriter

class OptionTwo:

    """
    this class creates the Option Two window
    """

    def __init__(self, app_version):
        
        self.__app_version = app_version


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

        file_directory = 'controller/system_files/option_two/n_selected_users.txt'

        file_reader = FileReader(file_directory=file_directory)
        file_content = file_reader.startFileReader()

        type_message = ''
        if file_content == 'Here will appear\nthe number of selected users':
            type_message = 'database_options-no_user'

        else:
            type_message = 'database_options'
        
        " INSTANCES THE VARIABLES "
        app_version = self.__app_version

        " INSTANCES THE WINDOW "
        self.__window = Tk()
        window = self.__window

        " INSTANCES THE FRAGMENTS OF THE WINDOW "
        logo_fragment = LogoFragment(window)
        fragments = OptionTwoFragments(window)

        """
        FRAGMENTS - START
        """
        " CREATES THE LOGO IN THE WINDOW "
        logo_image = ImageTk.PhotoImage(Image.open('view/images/logo.png')) # LOGO APP
        logo_fragment.startLogoAppFragment(logo_image)

        " CREATES THE INTERFACE WHICH WILL CONTROLL THE INSTAGRAM DATABASE "
        fragments.startMessageLabel(type_message=type_message)
        fragments.startButtons(type_button='database_options')

        " CREATES THE SEPARATOR "
        fragments.startSeparator()

        #" CREATES THE KIND OF LIKES "
        #fragments.startMessageLabel(type_message='user_options')
        #fragments.startRadioButtons()

        #" CREATES THE SEPARATOR "
        #fragments.startSeparator()

        " CREATES THE ENTRY AND BUTTON SEND "
        fragments.startMessageLabel(type_message='send')
        fragments.startEntry()
        fragments.startButtons(type_button='send')
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