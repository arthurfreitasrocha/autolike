# TKINTER LIBRARY
from tkinter import *

# VIEW
from view.Widgets import Widgets

class LogoFragment:

    def __init__(self, window):

        """
        this class returns a window with the logo of the app
        """

        " INSTANCES THE WINDOW "
        window = window

        " INSTANCES THE WIDGETS"
        self.__widget = Widgets(window)
        widget = self.__widget

        " INSTANCES THE FRAME "
        self.__logo_frame = widget.startFrame(504, 100, 'dark salmon', TOP)


    def startLogoAppFragment(self, logo):

        " this method creates the logo app fragment "

        " INSTANCES THE FRAME "
        logo_frame = self.__logo_frame

        " INSTANCES THE LOGO OF 'AutoLike' WHICH WILL BE USED IN THE WIDGETS "
        logo = logo

        " INSTANCES THE LABEL "
        logo_label = Label(logo_frame, image=logo)
        logo_label.place(x=0, y=0)
