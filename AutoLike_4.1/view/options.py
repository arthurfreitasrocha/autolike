# TKINTER LIBRARY
from tkinter import *

# IMAGE LIBRARY
from PIL import ImageTk, Image

# MODEL
from model.ErrorHandling import ErrorHandlingOptionOne
from model.ErrorHandling import ErrorHandlingOptionTwo

# VIEW
from view.user_manipulation.start_user_manipulation import UserManipulation
from view.Widgets import Widgets
from view.LogoFragment import LogoFragment
from view.WindowConfiguration import WindowConfiguration
from view.Message import Message

# CONTROLLER
from controller.file_manipulator import FileReader
from controller.file_manipulator import FileWriter

class OptionOne:

    """
    this class creates the Option One window
    """

    def __init__(self, app_version):
        
        self.__app_version = app_version


    def on_close(self):

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

        " INSTANCES THE WINDOW "
        self.__window = Tk()
        window = self.__window

        " INSTANCES THE FRAGMENTS OF THE WINDOW "
        logo_fragment = LogoFragment(window)
        fragments = OptionOneFragments(window)

        """
        FRAGMENTS - START
        """
        " CREATES THE LOGO IN THE WINDOW "
        logo_image = ImageTk.PhotoImage(Image.open('view/images/logo.png')) # LOGO APP
        logo_fragment.startLogoAppFragment(logo_image)

        " CREATES THE LOGIN AND PASSWORD ENTRIES "
        fragments.startEntries()

        " CREATES THE SEND BUTTON "
        fragments.startButton()

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

class OptionOneFragments:

    """
    this class returns the one option window fragments
    """

    def __init__(self, window):
        
        " INSTANCES THE WINDOW "
        self.__window = window

        " INSTANCES THE WIDGET CLASS "
        self.__widget = Widgets(self.__window)
        widget = self.__widget

        " INSTANCES THE FRAME "
        self.__hashtag_frame = widget.startFrame(500, 300, 'floral white', TOP)


    def startButton(self):

        " this method show the button which will return the information writted in the entries "

        " INSTANCES THE MESSAGE "
        start_message = 'Start'

        " INSTANCES THE WIDGETS "
        widget = self.__widget

        " INSTANCES THE FRAME"
        start_frame = self.__hashtag_frame

        " INSTANCES THE BUTTON "
        widget.startButton(start_frame, self.__hashtag_entry, self.__n_likes_entry, start_message, 'arial-15-bold', 'dark salmon', 'salmon', 'white', 'error-handling-option-one', 240, 140)

        #start_button = Button(start_frame, text=start_message, font=('arial', 15, 'bold'), 
        #bg='dark salmon', activebackground='salmon', activeforeground='white',
        #command=self.__startErrorHandling)
        #start_button.place(x=240, y=140)


    def startEntries(self):

        " this method shows the hashtag and number of likes entries "

        " INSTANCES THE VARIABLES WHICH WILL BE USED IN THE WIDGETS "
        hashtag_text = 'Hashtag'
        n_likes_text = 'Nº Likes'

        " INSTANCES THE WIDGETS "
        hashtag_frame = self.__hashtag_frame

        hashtag_label = Label(hashtag_frame, text=hashtag_text, font=('arial', 20, 'bold'), bg='floral white')
        hashtag_label.place(x=20, y=30)

        self.__hashtag_entry = Entry(hashtag_frame, font=('arial', 18, 'bold'), width=25)
        self.__hashtag_entry.place(x=150, y=33)

        n_likes_label = Label(hashtag_frame, text=n_likes_text, font=('arial', 20, 'bold'), bg='floral white')
        n_likes_label.place(x=20, y=80)

        self.__n_likes_entry = Entry(hashtag_frame, font=('arial', 18, 'bold'), width=25)
        self.__n_likes_entry.place(x=150, y=83)


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

        """
        file_directory = 'controller/system_files/option_two/n_selected_users.txt'

        file_reader = FileReader(file_directory=file_directory)
        file_content = file_reader.startFileReader()

        type_message = ''
        if file_content == 'Here will appear\nthe number of selected users':
            type_message = 'database_options-no_user'

        else:
            type_message = 'database_options'
        """
        
        " INSTANCES THE VARIABLES "
        app_version = self.__app_version

        " INSTANCES THE WINDOW "
        self.__window = Tk()
        window = self.__window

        " INSTANCES THE FRAGMENTS OF THE WINDOW "
        logo_fragment = LogoFragment(window)
        user_manipulation = UserManipulation(window)
        user_manipulation.startUserManipulation()

        fragments = OptionTwoFragments(window)

        """
        FRAGMENTS - START
        """

        " CREATES THE LOGO IN THE WINDOW "
        logo_image = ImageTk.PhotoImage(Image.open('view/images/logo.png')) # LOGO APP
        logo_fragment.startLogoAppFragment(logo_image)

        " CREATES THE ENTRY AND BUTTON SEND "
        fragments.startMessageLabel(type_message='send')
        fragments.startEntry()
        fragments.startButton()

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

class OptionTwoFragments:

    """
    this class returns the one option window fragments
    """

    def __init__(self, window):
        
        " INSTANCES THE WINDOW "
        self.__window = window

        " INSTANCES THE FRAME "
        self.__message_frame = Frame(window, width=500, height=150, bg='floral white')
        self.__message_frame.pack(side=TOP)


    def __returnOption(self, type_return, **kws):
        
        " this method returns the input of the user "

        " INSTANCES THE WINDOW "
        window = self.__window

        if type_return == 'send':

            " VARIABLES WHICH WILL USED "
            users_selected = kws.get('users_selected') # STR
            kind_likes = kws.get('kind_likes') # INT
            n_photos = kws.get('n_photos') # INT

            if kind_likes == 1:
                kind_likes = 'sequence'

            elif kind_likes == 2:
                kind_likes = 'random'

            n_photos = n_photos
            
            " WRITE THE OPTION TWO RETURN " 
            file_directory = 'controller/communication_file/return_option_two.txt'
            file_content = f'send-{kind_likes}-{n_photos}'

            file_writer = FileWriter(file_content=file_content, file_directory=file_directory)
            file_writer.startFileWriter()

            " WRITE THE SELECTED USERS "
            file_directory = 'controller/communication_file/return_option_two/return_selected_users.txt'
            file_content = users_selected

            file_writer = FileWriter(file_content=file_content, file_directory=file_directory)
            file_writer.startFileWriter()

            " SHOWS A MESSAGE "
            type_message = 'info'
            title_message = 'Logging into Instagram'
            text_message = 'We are logging into Instagram\nYou can close this window'

            message = Message(type_message=type_message, title_message=title_message, text_message=text_message)
            message.startMessage()

            window.destroy()


        elif type_return == 'manipulate_database':

            button = kws.get('button')

            file_directory = f'controller/system_files/user_instagram.txt'

            file_reader = FileReader(file_directory=file_directory)
            file_content = file_reader.startFileReader()

            user = file_content

            file_directory = f'controller/users/{user}/second_database.txt'

            file_reader = FileReader(file_directory=file_directory)
            file_content = file_reader.startFileReader()

            if file_content == '':

                " INFORMS WHAT THE 'second_database.txt' IS EMPTY " 
                file_directory = 'controller/communication_file/return_option_two.txt'

                if button == 'select_users':
                    file_content = button
                    window.destroy()
                
                else:
                    " SHOW A MESSAGE "
                    type_message = 'error'
                    title_message = 'No users selected'
                    text_message = f'Please, select at least one user before viewing or deleting him'

                    message = Message(type_message, title_message, text_message)
                    message.startMessage()

                file_writer = FileWriter(file_content=file_content, file_directory=file_directory)
                file_writer.startFileWriter()

            else:

                " CATCH THE DIRECTORY WHICH HAS THE 'return_option_one.txt' FILE " 
                file_directory = 'controller/communication_file/return_option_two.txt'
                file_content = f'{button}'

                file_writer = FileWriter(file_content=file_content, file_directory=file_directory)
                file_writer.startFileWriter()

                window.destroy()


    def __startErrorHandling(self, send_entry):

        " this method verify if the typed information is valid "

        " INSTANCES THE VARIABLES WHICH WILL GET THE LOGIN AND PASSWORD OF THE USER "
        kind_likes = 2
        send_entry = send_entry

        " CATCH THE CURRENT USER "
        file_directory = 'controller/system_files/user_instagram.txt'

        file_reader = FileReader(file_directory=file_directory)
        file_content = file_reader.startFileReader()

        user = file_content

        " CATCH THE SELECTED INSTAGRAM USERS "
        file_directory = f'controller/users/{user}/second_database.txt'
        
        file_reader = FileReader(file_directory=file_directory)
        file_content = file_reader.startFileReader()

        users_selected = file_content

        " INSTANCES THE ERROR HANDLING "
        error_handling = ErrorHandlingOptionTwo(users_selected=users_selected, send_entry=send_entry, kind_likes=kind_likes)
        return_EH = error_handling.startErrorHandling() # ERROR HANLING = EH

        users_selected_EH = return_EH[0]
        kind_likes_EH = return_EH[1]
        send_entry_EH = return_EH[2]

        if users_selected_EH == True and send_entry_EH == True and kind_likes_EH == True:

            " CALL THE METHOD WHICH WILL WRITE THE INFORMATION "
            self.__returnOption(type_return='send', users_selected=users_selected, kind_likes=kind_likes, n_photos=send_entry)

        else:

            if users_selected_EH == False and send_entry_EH == False and kind_likes_EH == False:
                
                " SHOWS A MESSAGE "
                type_message = 'warning'
                title_message = 'Warning'
                text_message = 'Please, selected at least one Instagram User to likes\nNumber of photos will be liked invalid\nPlease, selected at least one Kind of Likes'

                message = Message(type_message=type_message, title_message=title_message, text_message=text_message)
                message.startMessage()

            elif users_selected_EH == False:

                " SHOWS A MESSAGE "
                type_message = 'warning'
                title_message = 'Warning'
                text_message = 'Please, selected at least one Instagram User to likes'

                message = Message(type_message=type_message, title_message=title_message, text_message=text_message)
                message.startMessage()

            elif kind_likes_EH == False:

                " SHOWS A MESSAGE "
                type_message = 'warning'
                title_message = 'Warning'
                text_message = 'Please, selected at least one Kind of Likes'

                message = Message(type_message=type_message, title_message=title_message, text_message=text_message)
                message.startMessage()

            elif send_entry_EH == False:

                " SHOWS A MESSAGE "
                type_message = 'warning'
                title_message = 'Warning'
                text_message = 'Number of photos will be liked invalid'

                message = Message(type_message=type_message, title_message=title_message, text_message=text_message)
                message.startMessage()


    def startEntry(self):

        " INSTANCES THE FRAME "
        entry_frame = self.__message_frame

        self.__send_entry = Entry(entry_frame, font=('arial', 15), width=10)
        self.__send_entry.place(x=150, y=98)


    def startButton(self, ):

        " this method creates the buttons which will manipulate the user database "

        " INSTANCES THE WINDOW "
        window = self.__window

        " INSTANCES THE FRAME "
        button_send_frame = self.__message_frame

        " TEXT ABOUT ANY OPTION "
        text_button = 'Send'

        button_send = Button(button_send_frame, text=text_button, font=('arial', 15, 'bold'), 
        bg='dark salmon', activebackground='salmon', activeforeground='white',
        command=lambda:self.__startErrorHandling(send_entry=self.__send_entry.get()))
        button_send.place(x=280, y=90)


    def startMessageLabel(self, type_message):

        " this method write a message in the window "

        " INSTANCES THE WINDOW "
        window = self.__window

        " INSTANCES THE MESSAGE "
        message_text = 'Inform the amount of photos\nwill be liked of each user'

        message_frame = self.__message_frame

        self.__message_label = Label(message_frame, text=message_text, font=('arial', 15, 'bold'), bg='floral white')
        self.__message_label.place(x=110, y=15)


class OptionThree:

    """
    this class creates the Option Three window
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

        " INSTANCES THE VARIABLES "
        app_version = self.__app_version

        " INSTANCES THE WINDOW "
        self.__window = Tk()
        window = self.__window

        " INSTANCES THE FRAGMENTS OF THE WINDOW "
        logo_fragment = LogoFragment(window)
        user_manipulation = UserManipulation(window)
        user_manipulation.startUserManipulation()

        fragments = OptionThreeFragments(window)

        """
        FRAGMENTS - START
        """


        " CREATES THE MESSAGE LABEL "
        fragments.startMessageLabel()

        " CREATES THE TEXT CAMP "
        fragments.startText()

        " CREATES THE BUTTON "
        fragments.startButton()

        """
        FRAGMENTS - END
        """

        " CREATES THE LOGO IN THE WINDOW "
        logo_image = ImageTk.PhotoImage(Image.open('view/images/logo.png')) # LOGO APP
        logo_fragment.startLogoAppFragment(logo_image)

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

class OptionThreeFragments:

    """
    this class returns the option three window fragments
    """

    def __init__(self, window):
        
        " INSTANCES THE WINDOW "
        self.__window = window

        " INSTANCES THE FRAME "
        self.__message_frame = Frame(window, width=500, height=300, bg='floral white')
        self.__message_frame.pack(side=TOP)


    def __returnOption(self, type_return, **kws):
        
        " this method returns the input of the user "

        " INSTANCES THE WINDOW "
        window = self.__window

        if type_return == 'send':

            " VARIABLES WHICH WILL USED "
            users_selected = kws.get('users_selected') # STR
            kind_likes = kws.get('kind_likes') # INT
            n_photos = kws.get('n_photos') # INT

            if kind_likes == 1:
                kind_likes = 'sequence'

            elif kind_likes == 2:
                kind_likes = 'random'

            n_photos = n_photos
            
            " WRITE THE OPTION TWO RETURN " 
            file_directory = 'controller/communication_file/return_option_two.txt'
            file_content = f'send-{kind_likes}-{n_photos}'

            file_writer = FileWriter(file_content=file_content, file_directory=file_directory)
            file_writer.startFileWriter()

            " WRITE THE SELECTED USERS "
            file_directory = 'controller/communication_file/return_option_two/return_selected_users.txt'
            file_content = users_selected

            file_writer = FileWriter(file_content=file_content, file_directory=file_directory)
            file_writer.startFileWriter()

            " SHOWS A MESSAGE "
            type_message = 'info'
            title_message = 'Logging into Instagram'
            text_message = 'We are logging into Instagram\nYou can close this window'

            message = Message(type_message=type_message, title_message=title_message, text_message=text_message)
            message.startMessage()

            window.destroy()


        elif type_return == 'manipulate_database':

            button = kws.get('button')

            file_directory = f'controller/system_files/user_instagram.txt'

            file_reader = FileReader(file_directory=file_directory)
            file_content = file_reader.startFileReader()

            user = file_content

            file_directory = f'controller/users/{user}/second_database.txt'

            file_reader = FileReader(file_directory=file_directory)
            file_content = file_reader.startFileReader()

            if file_content == '':

                " INFORMS WHAT THE 'second_database.txt' IS EMPTY " 
                file_directory = 'controller/communication_file/return_option_two.txt'

                if button == 'select_users':
                    file_content = button
                    window.destroy()
                
                else:
                    " SHOW A MESSAGE "
                    type_message = 'error'
                    title_message = 'No users selected'
                    text_message = f'Please, select at least one user before viewing or deleting him'

                    message = Message(type_message, title_message, text_message)
                    message.startMessage()

                file_writer = FileWriter(file_content=file_content, file_directory=file_directory)
                file_writer.startFileWriter()

            else:

                " CATCH THE DIRECTORY WHICH HAS THE 'return_option_one.txt' FILE " 
                file_directory = 'controller/communication_file/return_option_two.txt'
                file_content = f'{button}'

                file_writer = FileWriter(file_content=file_content, file_directory=file_directory)
                file_writer.startFileWriter()

                window.destroy()


    def __startErrorHandling(self, writted_text):

        " this method verify if the typed information is valid "

        " INSTANCES THE VARIABLE WHICH WILL STORE THE MESSAGE WRITTED BY THE USER "
        writted_text = writted_text

        " CATCH THE CURRENT USER "
        file_directory = 'controller/system_files/user_instagram.txt'

        file_reader = FileReader(file_directory=file_directory)
        file_content = file_reader.startFileReader()

        user = file_content

        " CATCH THE SELECTED INSTAGRAM USERS "
        file_directory = f'controller/users/{user}/second_database.txt'
        
        file_reader = FileReader(file_directory=file_directory)
        file_content = file_reader.startFileReader()

        users_selected = file_content

        " INSTANCES THE ERROR HANDLING "
        error_handling = ErrorHandling(users_selected=users_selected, send_entry=send_entry, kind_likes=kind_likes)
        return_EH = error_handling.startOptionTwoErrorHandling() # ERROR HANLING = EH

        users_selected_EH = return_EH[0]
        kind_likes_EH = return_EH[1]
        send_entry_EH = return_EH[2]

        if users_selected_EH == True and send_entry_EH == True and kind_likes_EH == True:

            " CALL THE METHOD WHICH WILL WRITE THE INFORMATION "
            self.__returnOption(type_return='send', users_selected=users_selected, kind_likes=kind_likes, n_photos=send_entry)

        else:

            if users_selected_EH == False and send_entry_EH == False and kind_likes_EH == False:
                
                " SHOWS A MESSAGE "
                type_message = 'warning'
                title_message = 'Warning'
                text_message = 'Please, selected at least one Instagram User to likes\nNumber of photos will be liked invalid\nPlease, selected at least one Kind of Likes'

                message = Message(type_message=type_message, title_message=title_message, text_message=text_message)
                message.startMessage()

            elif users_selected_EH == False:

                " SHOWS A MESSAGE "
                type_message = 'warning'
                title_message = 'Warning'
                text_message = 'Please, selected at least one Instagram User to likes'

                message = Message(type_message=type_message, title_message=title_message, text_message=text_message)
                message.startMessage()

            elif kind_likes_EH == False:

                " SHOWS A MESSAGE "
                type_message = 'warning'
                title_message = 'Warning'
                text_message = 'Please, selected at least one Kind of Likes'

                message = Message(type_message=type_message, title_message=title_message, text_message=text_message)
                message.startMessage()

            elif send_entry_EH == False:

                " SHOWS A MESSAGE "
                type_message = 'warning'
                title_message = 'Warning'
                text_message = 'Number of photos will be liked invalid'

                message = Message(type_message=type_message, title_message=title_message, text_message=text_message)
                message.startMessage()


    def startButton(self):

        " this method show the button which will return the information writted in the entries "

        " INSTANCES THE MESSAGE "
        start_message = 'Start'

        " INSTANCES THE WIDGETS "
        start_frame = self.__message_frame

        start_button = Button(start_frame, text=start_message, font=('arial', 15, 'bold'), 
        bg='dark salmon', activebackground='salmon', activeforeground='white',
        command=lambda:self.__startErrorHandling(self.__message_text.get(0, END)))
        start_button.place(x=220, y=245)


    def startText(self):

        " this method shows the text widget "

        " INSTANCES THE FRAME "
        message_frame = self.__message_frame

        self.__message_text = Text(message_frame, font=('arial', 15, 'bold'), width=41, height=7)
        self.__message_text.place(x=20, y=60)


    def startMessageLabel(self):

        " this method shows the labels "

        " INSTANCES THE FRAME "
        message_frame = self.__message_frame

        " INSTANCES THE TEXT VARIABLE "
        text = 'Write the message which will be sended'

        " INSTANCES THE WIDGET "
        message_label = Label(message_frame, text=text, font=('arial', 15, 'bold'), bg='floral white')
        message_label.place(x=50, y=15)
