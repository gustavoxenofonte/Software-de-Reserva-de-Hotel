import os
import sys
caminho_absoluto = os.path.abspath(os.curdir)
sys.path.insert(0, caminho_absoluto)
import database.roomsDatabase
import database.reservationDatabase
import database.guestDatabase

def excluirReservas():
    print("Exibindo reservas...")
    reservas = database.reservationDatabase.listarReservas()
    print("="*66)
    print("|NO.  |CPF           |CHEK-IN     |CHECK-OUT   |VALOR |STATUS    |")
    for i in reservas:
        print(f"|{i['room_number']:<4} |{i['guest_cpf']:<13} |{i['checkin_date']:<11} |{i['checkout_date']:<11} |{i['total_value']:<4} |{i['status']:<10}|")
    print("="*66)
    print("="*50)
    print("MENU CANCELAMENTO DE RESERVA")
    print("Insira 0 a qualquer momento para sair desse menu")
    print("="*50)
    print()

    cpfHospede = str(input("Insira o CPF do hóspede: ")).strip()
    cpfHospede = "".join(x for x in cpfHospede if x.isnumeric()) ##essa função .join() retira todo caracter que não for númerico da str, como !., e etc.
    if cpfHospede == '0':
        return print("Fim do programa")
    while len(cpfHospede) != 11:  ##confere se o cpf é real
        print("CPF inválido")
        cpfHospede = str(input("Insira o CPF do hóspede: ")).strip()
        cpfHospede = "".join(x for x in cpfHospede if x.isnumeric())
        if cpfHospede == '0':
            return print("Fim do programa")
    try:
        if database.reservationDatabase.reservaExiste(cpfHospede):
            database.reservationDatabase.cancelarReserva(cpfHospede)
            print("Reserva cancelada")
    except:
        print("Reserva não encontrada ou já finalizada")