from database.adminDatabase.adminExiste import *
from database.adminDatabase.cadastrarLoginAdministrativo import *
from sys import exit


def login_adm():
    print("== TELA DE LOGIN ==")
    if adminExiste() == True:
        pass

    else:
        while True:
            opcao = input("Não existe nenhum cadastro de login administrativo, deseja criar um? (S/N) ")
            if opcao.upper() == "S":
                usuario = str(input("Usuário: "))
                senha = str(input("Senha: "))
                cadastrarLoginAdministrativo(usuario, senha)
                break
            elif opcao.upper() == "N":
                exit()

login_adm()