# Verificação se o banco de dados está criado
try:
    nome_arquivo = './database/reservationDatabase/reservationDatabase.csv'
    arquivo = open(nome_arquivo, 'r+', encoding='utf-8')
except FileNotFoundError:   # Se não existente, criar
    arquivo = open(nome_arquivo, 'w+', encoding='utf-8')
    arquivo.writelines('room_number,guest_cpf,checkin_date,checkout_date,total_value,status\n')
arquivo.close()

from .cadastrarReserva import *
from .cancelarReserva import *
from .checkIn import *
from .checkOut import *
from .listarReservas import *
from .reservaExiste import *

__all__ = ['cadastrarReserva', 'cancelarReserva', 'checkIn', 'checkOut', 'listarReservas', 'reservaExiste']