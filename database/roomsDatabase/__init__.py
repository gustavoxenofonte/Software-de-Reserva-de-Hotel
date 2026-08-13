# Verificação se o banco de dados está criado
try:
    nome_arquivo = './database/roomsDatabase/roomsDatabase.csv'
    arquivo = open(nome_arquivo, 'r+')
except FileNotFoundError:   # Se não existente, criar
    arquivo = open(nome_arquivo, 'w+')
    arquivo.writelines('number,name,capacity,daily_value,free\n')
arquivo.close()

from .cadastrarQuarto import *
from .excluirQuarto import *

__all__ = ['cadastrarQuarto', 'excluirQuarto']