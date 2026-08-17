from database.adminDatabase.adminExiste import *
from database.adminDatabase.cadastrarLoginAdministrativo import *

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
                    raise SystemExit

        except AdminLoginDontExists:
            while True:
                print("== TELA DE CRIAÇÃO DE USUÁRIO ==")
                opcao = input("Não existe nenhum cadastro de login administrativo, deseja criar um? (S/N) ")
                if opcao.upper() == "S":
                    while True:
                        try:
                            usuario = str(input("Usuário: "))
                            senha = str(input("Senha: "))
                            cadastrarLoginAdministrativo(usuario, senha)
                            break
                        except UserNameNotStr:
                            print("Nome de usuário inválido, tente novamente")
                        except UserNameHaveComma:
                            print("O nome de usuário não pode ter vírgula, tente novamente")
                        except UserNameHaveSpace:
                            print("O nome de usuário não pode ter espaço, tente novamente")
                        except NullUserName:
                            print("O nome de usuário não pode ser vazio, tente novamente")
                        except PasswordNotStr:
                            print("Senha inválida, tente novamente")
                        except PasswordHaveComma:
                            print("A senha não pode ter vírgula, tente novamente")
                        except PasswordHaveSpace:
                            print("A senha não pode ter espaço, tente novamente")
                        except NullPassword:
                            print("A senha não pode ser vazia, tente novamente")

                    break

                elif opcao.upper() == "N":
                    raise SystemExit