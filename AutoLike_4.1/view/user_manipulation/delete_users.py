# TKINTER LIBRARY
from tkinter import *

# IMAGE LIBRARY
from PIL import ImageTk, Image

# VIEW
from view.LogoFragment import LogoFragment
from view.user_manipulation.ManipulateUsersDatabaseFragments import ManipulateUsersDatabaseFragments
from view.WindowConfiguration import WindowConfiguration
from view.Message import Message

# CONTROLLER
from controller.file_manipulator import FileReader
from controller.file_manipulator import FileWriter

class DeleteUsers:

    def __init__(self, app_version):

        """
        this class returns the 'select users' window
        """
        
        " INSTANCES THE WINDOW "
        self.__app_version = app_version


    def on_close(self):

        window = self.__window

        window.destroy()

        self.readReturn(window_closed=True)


    def readReturn(self, **kws):

        " this method just read the return of 'ManipulateUsersDatabaseFragments.py' "

        window_closed = kws.get('window_closed')

        file_directory = 'controller/communication_file/return_option_two.txt'

        if window_closed == True:

            file_content = 'window_closed'

            file_writer = FileWriter(file_content=file_content, file_directory=file_directory)
            file_writer.startFileWriter()

        file_reader = FileReader(file_directory=file_directory)
        file_content = file_reader.startFileReader()

        return file_content


    def flag(self):

        " show a message confirming all users are selected "

        " INSTANCES THE WINDOW "
        window = self.__window
            
        n_profiles = kws.get('n_profiles')
        n_likes = kws.get('n_likes')

        " SHOW A MESSAGE "
        type_message = 'info'
        title_message = 'Success'
        text_message = f'Success! All the users selecteds'

        message = Message(type_message, title_message, text_message)
        message.startMessage()

        window.destroy()


    def startInterface(self, **kws):

        " this method starts the 'Select Users' interface "

        flag = kws.get('flag')

        " INSTANCES THE VARIABLES "
        app_version = self.__app_version

        " INSTANCES THE WINDOW "
        self.__window = Tk()
        window = self.__window

        " INSTANCES THE FRAGMENTS OF THE WINDOW "
        logo_fragment = LogoFragment(window)
        fragments = ManipulateUsersDatabaseFragments(window)


        """
        FRAGMENTS - START
        """
        " CREATES THE LOGO IN THE WINDOW "
        logo_image = ImageTk.PhotoImage(Image.open('view/images/logo.png')) # LOGO APP
        logo_fragment.startLogoAppFragment(logo_image)

        " CREATES A LABEL WITH A MESSAGE "
        fragments.startMessageLabel('Delete the users')

        " CREATES A LIST WITHE THE INSTAGRAM USERS "
        fragments.startListBox(type_catch='delete_users')

        " CREATES A CHECKBUTTON WHICH CAN SELECT ALL THE USERS "
        fragments.startCheckButton()

        " CREATES A BUTTON "
        fragments.startButton('delete_users')
        """
        FRAGMENTS - END
        """


        " CONFIGURES THE WINDOW "
        window_configuration = WindowConfiguration(window, width=500, height=510, width_distance=3, height_distance=7)
        window_configuration = window_configuration.fullWindowConfiguration()

        " CATCH THE WINDOW GEOMETRY AND THE APP TITLE WITH THE 'window_configuration' RETURNS - lines 32, 33 "
        window_geometry = window_configuration['window_geometry']
        app_title = f'AutoLike - Version: {app_version}' # APP TITLE

        " FINAL WINDOW CONFIGURATION "
        window.protocol("WM_DELETE_WINDOW", self.on_close)
        window.title(app_title)
        window.resizable(width=False, height=False)
        window.geometry(window_geometry)

        if flag == 'show_message':
            self.flag()

        window.mainloop()