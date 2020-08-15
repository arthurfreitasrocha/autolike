# TKINTER LIBRARY
from tkinter import *

class LogoFragment:

    """
    this class returns a window with the logo of the app
    """
    def __init__(self, window):

        " constructor "

        " INSTANCES THE WINDOW "
        self.window = window

        " INSTANCES THE FRAME "
        self.logo_frame = Frame(window, width=504, height=100, bg='dark salmon')
        self.logo_frame.pack(side=TOP)


    def startLogoAppFragment(self, logo):

        " this method creates the logo app fragment "

        " INSTANCES THE WINDOW "
        window = self.window

        " INSTANCES THE LOGO OF 'AutoLike' WHICH WILL BE USED IN THE WIDGETS "
        logo = logo

        " INSTANCES THE WIDGETS "
        logo_frame = self.logo_frame

        logo_label = Label(logo_frame, image=logo)
        logo_label.place(x=0, y=0)
