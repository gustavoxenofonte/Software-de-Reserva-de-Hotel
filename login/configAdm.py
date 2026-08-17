from database.adminDatabase.alterarSenha import *
from database.adminDatabase.alterarUserName import *
from database.adminDatabase.cadastrarLoginAdministrativo import *

def menuAlterarUsername():
    while True:
        try:
            novo_usuario = str(input("Novo usuário: "))
            print(f"Nome de usuário trocado para: {novo_usuario}")
            return novo_usuario
        except PasswordNotStr:
            print("Senha inválida, tente novamente")
        except UserNameHaveComma:
            print("Senha não pode ter virgula, tente novamente")
        except PasswordHaveSpace:
            print("Senha não pode ter espaço, tente novamente")
        except NullPassword:
            print("Senha nao pode ser vazia, tente novamente")



