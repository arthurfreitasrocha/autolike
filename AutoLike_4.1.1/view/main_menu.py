# TKINTER LIBRARY
from tkinter import *

# IMAGE LIBRARY
from PIL import ImageTk, Image

# VIEW
from view.LogoFragment import LogoFragment
from view.WindowConfiguration import WindowConfiguration
from view.Message import Message

# MODEL
from model.file_manipulator import FileReader
from model.file_manipulator import FileWriter

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
        window_configuration = WindowConfiguration(window, width=500, height=570, width_distance=3, height_distance=6)
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

class MainMenuFragments:

    """
    this class returns the main menu window
    """
    def __init__(self, window):
        
        " constructor "

        " INSTANCES THE WINDOW "
        self.window = window

    
    def __returnOption(self, type_return, **kws):
        
        " this method returns the input of the user "

        " CATCH THE VALUE OF 'n_option' IF THE USER INFORM IT - line 21 "
        n_option = kws.get('n_option')

        " INSTANCES THE WINDOW - line 21 "
        window = self.window

        " CATCH THE DIRECTORY WHICH HAS THE 'return_main_menu.txt' FILE - line 27" 
        file_directory = 'controller/communication_file/return_main_menu.txt'
        

        " WRITE IN THE RETURN FILE THE USER CHOICE - lines 30 - 48 "
        if type_return == 'email_option':
            
            file_content = 'email_option'

            file_writer = FileWriter(file_content=file_content, file_directory=file_directory)
            file_writer.startFileWriter()

            window.destroy()
        
        elif type_return == 'user_option':
            
            file_content = f'user_option-{n_option}'

            file_writer = FileWriter(file_content=file_content, file_directory=file_directory)
            file_writer.startFileWriter()

            window.destroy()


    def startSeparator(self):

        " this method creates a widget which can separate others widgets "

        " INSTANCES THE WINDOW "
        window = self.window

        " CREATE THE FRAME SEPARATOR "
        separator_frame = Frame(window, width=500, height=10, bg='dark salmon')
        separator_frame.pack(side=TOP)


    def startUserOptions(self):

        " this method creates the user options with radio buttons "

        " INSTANCES THE WINDOW "
        window = self.window

        " CATCH THE USER OPTION "
        n_options = IntVar()

        " INSTANCES THE FRAME AND THE LABEL OF THE USER OPTIONS "
        frame_user_options = Frame(window, width=500, height=310, bg='floral white')
        frame_user_options.pack(side=TOP)

        label_user_options = Label(frame_user_options, text='User Options',
        font=('arial', 15,'bold'), bg='floral white')
        label_user_options.place(x=150, y=20)

        " TEXT ABOUT ANY OPTION "
        text_option_01 = 'Like photos using a hashtag'
        text_option_02 = 'Like photos of an specific Instagram profile'
        text_option_03 = 'Send message in Direct'

        " INSTANCES THE RADIO BUTTONS - lines 87-97 "
        radiobutton_option_01 = Radiobutton(frame_user_options, text=text_option_01, font=('arial', 15,'bold'), bg='dark salmon',
            activebackground='salmon', activeforeground='white', variable=n_options, value=1)
        radiobutton_option_01.place(x=95, y=80)

        radiobutton_option_02 = Radiobutton(frame_user_options, text=text_option_02, font=('arial', 15,'bold'), bg='dark salmon',
            activebackground='salmon', activeforeground='white', variable=n_options, value=2)
        radiobutton_option_02.place(x=30, y=130)

        radiobutton_option_03 = Radiobutton(frame_user_options, text=text_option_03, font=('arial', 15,'bold'), bg='dark salmon',
            activebackground='salmon', activeforeground='white', variable=n_options, value=3)
        radiobutton_option_03.place(x=120, y=180)

        " INSTANCES THE BUTTON - lines 100-102 "
        button_user_option = Button(frame_user_options, text='Select', font=('arial', 15, 'bold'), bg='dark salmon',
        activebackground='salmon', activeforeground='white', command=lambda: self.__returnOption('user_option', n_option=n_options.get()))
        button_user_option.place(x=210, y=250)


    def startEmailFragment(self, user_email):

        " this method shows the email of the user and a button to switch the email "

        " INSTANCES THE WINDOW "
        window = self.window

        " INSTANCES THE STRINGS WILL BE USED IN THE WIDGETS "
        user_email = f'EMAIL: {user_email}'
        text_email_button = 'Switch Instagram Email'
        
        " INSTANCES THE WIDGETS "
        email_frame = Frame(window, width=500, height=150, bg='floral white')
        email_frame.pack(side=TOP)

        email_label = Label(email_frame, text=user_email, font=('arial', 15, 'bold'), bg='floral white')
        email_label.place(x=50, y=20)

        email_button = Button(email_frame, text=text_email_button, font=('arial', 15,'bold'), bg='dark salmon',
            activebackground='salmon', activeforeground='white', command=lambda: self.__returnOption('email_option'))
        email_button.place(x=130, y=80)
