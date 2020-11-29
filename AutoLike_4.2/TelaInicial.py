import PySimpleGUI as sg

class gerarTelaInicial:

    def __init__(self):
        self.__gerarInterface()


    def __gerarInterface(self):

        sg.theme("light blue")

        layout = [
            [sg.Text("Seu email:"),sg.Input(), sg.Button("Alterar")],
            [sg.Checkbox("Curtir com Hashtag", key="hashtag"), sg.Checkbox("Curtir com BD", key="bd")],
            [sg.Button("Enviar")]
        ]


        janela = sg.Window("AutoLike v4.2", layout)

        while True:

            button, event = janela.read()

            if event == sg.WIN_CLOSED:
                print(button)
                janela.close()
                break
