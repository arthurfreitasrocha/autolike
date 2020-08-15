# TKINTER LIBRARY'S
from tkinter import *
from tkinter import messagebox

# IMAGE LIBRARY
from PIL import ImageTk, Image

# VIEW
from view.LogoFragment import LogoFragment
from view.EmailFragments import EmailFragments
from view.WindowConfiguration import WindowConfiguration
from view.Message import Message

# CONTROLLER
from controller.file_reader import FileReader
from controller.file_writer import FileWriter


class Email:

    """
    this class creates the Login Instagram window
    """
    def __init__(self, app_version):

        " constructor "

        self.app_version = app_version


    def on_close(self):

        window = self.__window

        window.destroy()

        self.readReturn(window_closed=True)

    
    def readReturn(self, **kws):

        " this method just read the return of 'EmailFragments.py' "

        window_closed = kws.get('window_closed')

        file_directory = 'controller/communication_file/return_email.txt'

        if window_closed == True:

            file_content = 'window_closed'

            file_writer = FileWriter(file_content=file_content, file_directory=file_directory)
            file_writer.startFileWriter()

        file_reader = FileReader(file_directory=file_directory)
        file_content = file_reader.startFileReader()

        return file_content


    def flag(self):

        " this method shows a message if any error was ocurred "

        type_message = 'warning'
        title_message = 'Failed'
        text_message = 'Failed to login in Instagram\nAre you sure your credentials are correct?'

        message = Message(type_message, title_message, text_message)
        message.startMessage()


    def startInterface(self, **kws):

        " this method starts the 'Email' interface "

        " INSTANCES THE VARIABLES "
        app_version = self.app_version
        password_status = kws.get('password_status')
        password = kws.get('password')
        login = kws.get('login')
        flag = kws.get('flag')

        " INSTANCES THE WINDOW "
        self.__window = Tk()
        window = self.__window

        " CREATES THE 'show/hide' PASSWORD VARIABLES "
        open_eye_image = ImageTk.PhotoImage(Image.open('view/images/visible_password.png'))
        closed_eye_image = ImageTk.PhotoImage(Image.open('view/images/hidden_password.png'))

        " INSTANCES THE FRAGMENTS OF THE WINDOW "
        logo_fragment = LogoFragment(window)
        fragments = EmailFragments(window=window, open_eye_image=open_eye_image, closed_eye_image=closed_eye_image)

        """
        FRAGMENTS - START
        """
        " CREATES THE LOGO IN THE WINDOW "
        logo_image = ImageTk.PhotoImage(Image.open('view/images/logo.png')) # LOGO APP
        logo_fragment.startLogoAppFragment(logo_image)

        " CREATES THE MESSAGE LABEL "
        fragments.startMessageLabel()

        " CREATES THE LOGIN AND PASSWORD ENTRIES "
        fragments.startEntries()

        fragments.startPasswordButton()

        " CREATES THE SEND BUTTON "
        fragments.startSendButton()
        """
        FRAGMENTS - END
        """


        " CONFIGURES THE WINDOW "
        window_configuration = WindowConfiguration(window, width=500, height=370, width_distance=3, height_distance=5)
        window_configuration = window_configuration.fullWindowConfiguration()

        " CATCH THE WINDOW GEOMETRY AND THE APP TITLE WITH THE 'window_configuration' RETURNS "
        window_geometry = window_configuration['window_geometry']
        app_title = f'AutoLike - Version: {app_version}' # APP TITLE

        " FINAL WINDOW CONFIGURATION "
        window.protocol("WM_DELETE_WINDOW", self.on_close)
        window.title(app_title)
        window.resizable(width=False, height=False)
        window.geometry(window_geometry)

        if flag == 'failed':
            self.flag()
            
        window.mainloop()
