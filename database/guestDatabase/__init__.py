# Verificação se o banco de dados está criado
try:
    nome_arquivo = './database/guestDatabase/guestDatabase.csv'
    arquivo = open(nome_arquivo, 'r+', encoding='utf-8')
except FileNotFoundError:   # Se não existente, criar
    arquivo = open(nome_arquivo, 'w+', encoding='utf-8')
    arquivo.writelines('cpf,name,phone_number,age\n')
arquivo.close()

from .cadastrarHospede import *
from .excluirHospede import *
from .hospedeExiste import *
from .listarHospedes import *

__all__ = ['cadastrarHospede', 'excluirHospede', 'hospedeExiste', 'listarHospedes']