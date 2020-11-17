from tkinter import *
from PIL import Image, ImageTk

class TelaInicio:

    def __init__(self):

        self.__gerarInterface()


    def __gerarInterface(self):

        janela = Tk()

        frame = Frame(janela, width=900, height=100, bg="salmon").pack(side=TOP)
        Label(frame, text="AutoLike v.4.2", font=("arial", 20, "bold")).pack(side=TOP)

        janela.geometry("900x500+500+200")
        janela.mainloop()


if __name__ == "__main__":

    interface = TelaInicio()