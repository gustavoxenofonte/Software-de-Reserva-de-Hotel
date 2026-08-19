from csv import DictReader, DictWriter
from .reservaExiste import reservaExiste
from ..guestDatabase import excluirHospede

class CPFAreNotNumbers(Exception):
    pass

class CPFAreNotCorrect(Exception):
    pass

class ReservationDontExists(Exception):
    pass

class ThereAreNoOpenReservations(Exception):
    pass

def cancelarReserva(guest_cpf: str) -> None:
    if not guest_cpf.isdecimal():    # Verifica se o cpf são somente números
        raise CPFAreNotNumbers("O cpf contém outros caracteres que não são números")

    if len(guest_cpf) != 11:    # Verifica se o cpf tem 11 caracteres
        raise CPFAreNotCorrect("O cpf não está correto, não tem 11 números")

    if reservaExiste(guest_cpf) == False:    # Verifica se a reserva existe
        raise ReservationDontExists("A reserva não existe")

    # Cria uma lista com todas as reservas
    with open("./database/reservationDatabase/reservationDatabase.csv", "r", encoding='utf-8') as database:
        databaseList = list(DictReader(database))

    # Verificar se há reservas em aberto
    openReservations = False
    for row in databaseList:
        if row['guest_cpf'] == guest_cpf:
            # Verificação se a reserva está como finalizado ou cancelado
            if row['status'] in ['reservado', 'hospedado']:
                row['status'] = 'cancelado' 
                openReservations = True   # Define o status da reserva pra cancelado
    
    if not openReservations:
        raise ThereAreNoOpenReservations("Não há reservas em aberto.")     # Se não houver, haverá um erro

    # Reescreve o banco de dados das reservas atualizado
    fieldnames = ['room_number', 'guest_cpf', 'checkin_date', 'checkout_date', 'total_value', 'status']
    with open("./database/reservationDatabase/reservationDatabase.csv", "w", newline='', encoding='utf-8') as database:
        writer = DictWriter(database, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(databaseList)

    # Remover o hóspede do banco de dados de hóspedes
    excluirHospede(guest_cpf)