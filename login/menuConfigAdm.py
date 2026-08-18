from login.loginAdm import *
from login.configAdm import *

# Exige login novamente antes de liberar acesso à área de configuração
def menuConfigAdm():
    print("Por questões de segurança, insira o login novamente")
    if login_adm():
        print("== Configuração Login Administrativo ==")
        print("0. Sair")
        print("1. Alterar login")

        while True:
            opcao_adm = input("Escolha uma opção: ")

            if opcao_adm.isdigit():
                opcao_adm = float(opcao_adm)
                if opcao_adm % 1 == 0 and opcao_adm == 1 or opcao_adm == 0:
                    break
                
            else:
                print("Opção inválida, tente novamente")

        if opcao_adm == 1:
            menuAlterarUsername()
            menuAlterarSenha()
        else:
            pass