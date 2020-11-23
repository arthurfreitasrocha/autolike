
def FileReader(diretorio):

    with open(diretorio, "r") as file:
        return file.read()

def FileWriter(diretorio, conteudo):

    with open(diretorio, "w") as file:
        file.write(conteudo)

def FileAppender(diretorio, conteudo):

    with open(diretorio, "a") as file:
        file.append(conteudo)

