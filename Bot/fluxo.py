from .login import loginInstagram
from .processo import iniciarProcesso, curtirPublicacoes

from os import mkdir, system


def __verificarExistenciaUsuario(usuario, senha):

    # Captura o diretório raiz
    with open('Bot\\diretorio_raiz.txt', 'r') as f:
        diretorio_raiz = f.read()


    # Tenta criar a pasta do usuário no BD
    # Se conseguir = Não existe usuário com esse nome
    # Se NÃO conseguir = Usuário já cadastrado
    try:
        diretorio_pasta = f'{diretorio_raiz}\\Users\\{usuario}'
        mkdir(diretorio_pasta)

        diretorio_usuario = f'{diretorio_raiz}\\Users\\{usuario}\\conta.txt'
        with open(diretorio_usuario, 'w') as f:
            conteudo_usuario = f'{usuario}-{senha}'
            f.write(conteudo_usuario)

        diretorio_usuario = f'{diretorio_raiz}\\Users\\{usuario}\\database.txt'
        with open(diretorio_usuario, 'w') as f:
            conteudo_usuario = f'{usuario}-{senha}'
            f.write('')

        print(f"AUTOLIKE: Usuário {usuario} criado com sucesso")

    except:
        print("AUTOLIKE: Usuário já existente. Atualizando dados do usuário...")

        diretorio_usuario = f'{diretorio_raiz}\\Users\\{usuario}\\conta.txt'
        with open(diretorio_usuario, 'w') as f:
            conteudo_usuario = f'{usuario}-{senha}'
            f.write(conteudo_usuario)

        print("AUTOLIKE: Dados do usuário atualizados com sucesso.")


def iniciarFluxo(janela, usuario, senha, hashtag, perfis, comentario):

    # Fechando interface
    janela.destroy()

    # Verificando se usuário existe no BD
    __verificarExistenciaUsuario(usuario, senha)

    # Realizar login no Instagram
    driver = loginInstagram(usuario, senha)

    # Faz a validação do profile_user antes de entrar
    iniciarProcesso(driver, usuario, hashtag, perfis, comentario)

    system("cls")
    print(f"AUTOLIKE: {perfis} perfis acessados com sucesso!")
    print(f"AUTOLIKE: Fim da execução.")
    exit(0)

