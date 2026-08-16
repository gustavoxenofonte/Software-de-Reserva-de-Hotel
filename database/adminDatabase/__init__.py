# Verificação se o banco de dados está criado
try:
    nome_arquivo = './database/adminDatabase/adminDatabase.csv'
    arquivo = open(nome_arquivo, 'r+', encoding='utf-8')
except FileNotFoundError:   # Se não existente, criar
    arquivo = open(nome_arquivo, 'w+', encoding='utf-8')
    arquivo.writelines('user_name,password\n')
arquivo.close()

from .cadastrarLoginAdministrativo import *
from .alterarSenha import *
from .alterarUserName import *
from .adminExiste import *

__all__ = ['cadastrarLoginAdministrativo', 'alterarSenha', 'alterarUserName', 'adminExiste']