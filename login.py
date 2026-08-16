from database.adminDatabase.adminExiste import *
from database.adminDatabase.cadastrarLoginAdministrativo import *
import sys

def login_adm():
    if adminExiste() == True:
        pass
    else:
        while True:
            print("== TELA DE LOGIN == ")
            opcao = input("Não existe nenhum cadastro de login administrativo, deseja criar um? (S/N) ")
            if opcao.upper() == "S":
                usuario = str(input("Usuário: "))
                senha = str(input("Senha: "))
                cadastrarLoginAdministrativo(usuario, senha)
                break
            elif opcao.upper() == "N":
                sys.exit()

login_adm()