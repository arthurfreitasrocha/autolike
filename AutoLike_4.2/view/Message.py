# TKINTER LIBRARY'S
from tkinter import *
from tkinter import messagebox

class Message:

    """
    this class show a message box
    """

    def __init__(self, type_message, title_message, text_message):
        
        self.__type_message = type_message
        self.__title_message = title_message
        self.__text_message = text_message


    def startMessage(self):

        type_message = self.__type_message
        title_message = self.__title_message
        text_message = self.__text_message

        if type_message == 'info':
            messagebox.showinfo(title_message, text_message)

        elif type_message == 'warning':
            messagebox.showwarning(title_message, text_message)

        elif type_message == 'error':
            messagebox.showerror(title_message, text_message)