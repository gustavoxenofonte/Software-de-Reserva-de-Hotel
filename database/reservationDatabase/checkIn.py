from csv import DictReader, DictWriter
from ..roomsDatabase import alterarStatusQuarto
from .reservaExiste import reservaExiste

class CPFAreNotNumbers(Exception):
    pass

class CPFAreNotCorrect(Exception):
    pass

class ReservationDontExists(Exception):
    pass

class GuestAlreadyStaying(Exception):
    pass

class ReservationCompleted(Exception):
    pass

class ReservationCancelled(Exception):
    pass

def checkIn(guest_cpf: str) -> None:
    # Verificações
    if not guest_cpf.isdecimal():    # Verifica se o cpf são somente números
        raise CPFAreNotNumbers("O cpf contém outros caracteres que não são números")

    if len(guest_cpf) != 11:    # Verifica se o cpf tem 11 caracteres
        raise CPFAreNotCorrect("O cpf não está correto, não tem 11 números")

    if reservaExiste(guest_cpf) == False:    # Verifica se a reserva existe
        raise ReservationDontExists("A reserva não existe")

    # Cria uma lista com todas as reservas
    with open("./database/reservationDatabase/reservationDatabase.csv", "r", encoding='utf-8') as database:
        databaseList = list(DictReader(database))
    
    for row in databaseList:
        if row['guest_cpf'] == guest_cpf:

            # Verificação se a reserva está como hospedado, finalizado ou cancelado
            if row['status'] == 'hospedado':
                raise GuestAlreadyStaying("Hóspede já está hospedado")
            elif row['status'] == 'finalizado':
                raise ReservationCompleted("A reserva já foi finalizada")
            elif row['status'] == 'cancelado':
                raise ReservationCancelled("A reserva foi cancelada")

            row['status'] = 'hospedado'    # Atualiza o status da reserva para hospedado
            room = row['room_number']     # Salva o número do quarto

    alterarStatusQuarto(int(room), False)    # Atualiza o status Free do quarto para False

    # Reescreve o banco de dados com os dados atualizados
    fieldnames = ['room_number', 'guest_cpf', 'checkin_date', 'checkout_date', 'total_value', 'status']
    with open("./database/reservationDatabase/reservationDatabase.csv", "w", newline='', encoding='utf-8') as database:
        writer = DictWriter(database, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(databaseList)