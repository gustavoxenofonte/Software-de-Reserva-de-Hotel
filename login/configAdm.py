from database.adminDatabase.alterarSenha import *
from database.adminDatabase.alterarUserName import *

def menuAlterarUsername():
    while True:
        try:
            novo_usuario = str(input("Novo usuário: "))
            alterarUserName(novo_usuario)
            print(f"Nome de usuário trocado para: {novo_usuario}")
            return novo_usuario
        except UserNameNotStr:
            print("Nome de usuário inválido, tente novamente")
        except UserNameHaveComma:
            print("Nome de usuário ter virgula, tente novamente")
        except UserNameHaveSpace:
            print("Nome de usuário não pode ter espaço, tente novamente")
        except NullUserName:
            print("Nome de usuário não pode ser vazia, tente novamente")

def menuAlterarSenha():
    while True:
        try:
            nova_senha = str(input("Nova senha: "))
            alterarSenha(nova_senha)
            print(f"Senha trocada para: {nova_senha}")
            return nova_senha
        except PasswordNotStr:
            print("Senha inválida, tente novamente")
        except PasswordHaveComma:
            print("A senha não deve ter vírgula, tente novamente")
        except PasswordHaveSpace:
            print("A senha não deve ter espaço, tente novamente")
        except NullPassword:
            print("A senha não pode ser vazia")


