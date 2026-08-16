from database.adminDatabase.adminExiste import *
from database.adminDatabase.cadastrarLoginAdministrativo import *
from sys import exit
from pathlib import Path
from csv import DictReader

def login_adm():
    print("== TELA DE LOGIN ==")
    while True:
        if adminExiste():
            usuario = str(input("Usuário: "))
            senha = str(input("Senha: "))
            caminho = Path("database/adminDatabase/adminDatabase.csv")

            with open(caminho, 'r', encoding='utf-8') as arquivo:
                leitor = DictReader(arquivo)
                for linha in leitor:
                    if linha["user_name"] == usuario and linha["password"] == senha:
                        return True
                        
                    else:
                        return False

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