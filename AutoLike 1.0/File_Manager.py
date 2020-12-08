

def fileWriter(destino, conteudo):

    with open(destino, "w") as file:
        file.write(conteudo)


def fileAppender(destino, conteudo):

    with open(destino, "a") as file:
        file.write(conteudo)


def fileReader(destino):

    with open(destino, "r") as file:
        conteudo = file.write()

    return conteudo