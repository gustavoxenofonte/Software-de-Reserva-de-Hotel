from database.adminDatabase.adminExiste import *
from database.adminDatabase.cadastrarLoginAdministrativo import *
from sys import exit

def login_adm():
    while True:
        try:
            lista = adminExiste()

            print("== TELA DE LOGIN ==")
            
            for tentativas in range (3, 0, -1):
                usuario = str(input("Usuário: "))
                senha = str(input("Senha: "))

                if lista[0] == usuario and lista[1] == senha:
                    return True
                            
                if tentativas > 1:
                    print(f"Senha incorreta, você possui mais {tentativas - 1} tentativas.")

                if tentativas == 1:
                    print("Você excedeu o número de tentativas")
                    exit()

        except AdminLoginDontExists:
            while True:
                print("== TELA DE CRIAÇÃO DE USUÁRIO ==")
                opcao = input("Não existe nenhum cadastro de login administrativo, deseja criar um? (S/N) ")
                if opcao.upper() == "S":
                    usuario = str(input("Usuário: "))
                    senha = str(input("Senha: "))
                    cadastrarLoginAdministrativo(usuario, senha)
                    break
                elif opcao.upper() == "N":
                    exit()