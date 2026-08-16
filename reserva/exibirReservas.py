import os
import sys

caminho_absoluto = os.path.abspath(os.curdir)
sys.path.insert(0, caminho_absoluto)
import database.reservationDatabase

def exibirReservas():
    print("Exibindo reservas...")
    reservas = database.reservationDatabase.listarReservas()
    print("="*66)
    print("|NO.  |CPF           |CHEK-IN     |CHECK-OUT   |VALOR |STATUS    |")
    for i in reservas:
        print(f"|{i['room_number']:<4} |{i['guest_cpf']:<13} |{i['checkin_date']:<11} |{i['checkout_date']:<11} |{i['total_value']:<4} |{i['status']:<10}|")
    print("="*66)
exibirReservas()