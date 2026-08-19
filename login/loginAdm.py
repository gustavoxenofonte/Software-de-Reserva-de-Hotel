from database.adminDatabase.adminExiste import *
from database.adminDatabase.cadastrarLoginAdministrativo import *
from time import sleep
from close import *

def login_adm():
    while True:
        try:
            lista = adminExiste() # Lança AdminLoginDontExists se ainda não houver login cadastrado

            print("== TELA DE LOGIN ==")
            
            for tentativas in range (3, 0, -1):
                usuario = str(input("Usuário: "))
                senha = str(input("Senha: "))

                if lista[0] == usuario and lista[1] == senha:
                    return True

                # Só avisa tentativas restantes se ainda sobrar alguma            
                if tentativas > 1:
                    print(f"Senha incorreta, você possui mais {tentativas - 1} tentativas.")

                # Última tentativa falhou, encerra o programa
                if tentativas == 1:
                    print("Você excedeu o número de tentativas")
                    raise SystemExit

        except AdminLoginDontExists:
            # Se não existe login cadastrado, oferece a criação do login
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

                        # Cada exception trata uma regra de validação
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

                    print("Login criado com sucesso")
                    print("Limpando a tela...")

                    sleep(1.5)
                    cls()
                    break

                elif opcao.upper() == "N":
                    raise SystemExit