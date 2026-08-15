from csv import writer
from datetime import date
from ..roomsDatabase import quartoExiste

class RoomDontExists(Exception):
    pass

class CPFAreNotNumbers(Exception):
    pass

class CPFAreNotCorrect(Exception):
    pass

class CheckInDateIsNotDatetime(Exception):
    pass

class CheckOutDateIsNotDatetime(Exception):
    pass

class CheckInDateInPast(Exception):
    pass

class CheckOutDateInPast(Exception):
    pass

class TotalValueIsNotFloat(Exception):
    pass

class StatusIsNotCorrect(Exception):
    pass

def cadastrarReserva(room_number: int, guest_cpf: str, checkin_date: date, checkout_date: date, total_value: float, status: str) -> None:

    # Verificações  
    if quartoExiste(room_number) == False:   # Verifica se o quarto existe
        raise RoomDontExists("O quarto não existe")

    if not guest_cpf.isdecimal():    # Verifica se o cpf são somente números
        raise CPFAreNotNumbers("O cpf contém outros caracteres que não são números")

    if len(guest_cpf) != 11:    # Verifica se o cpf tem 11 caracteres
        raise CPFAreNotCorrect("O cpf não está correto, não tem 11 números")

    if not isinstance(checkin_date, date):  # Verificar se é do tipo datetime
        raise CheckInDateIsNotDatetime("O checkin_date não é tipo datetime")

    if not isinstance(checkout_date, date):  # Verificar se é do tipo datetime
        raise CheckOutDateIsNotDatetime("O checkout_date não é tipo datetime")

    if checkin_date < date.today():    # Verifica se a data já passou
        raise CheckInDateInPast("A data do checkin já passou")

    if checkout_date < date.today():    # Verifica se a data já passou
        raise CheckOutDateInPast("A data do checkout já passou")

    if not isinstance(total_value, float):    # Verificar se o total_value é float
        raise TotalValueIsNotFloat("Total_value não é float")

    if status not in ['reservado', 'hospedado', 'finalizado', 'cancelado']:    # Verificar se status está no escopo (reservado, hospedado, finalizado, cancelado)
        raise StatusIsNotCorrect("Status não está no escopo (reservado, hospedado, finalizado, cancelado)")

    with open("./database/reservationDatabase/reservationDatabase.csv", "a", newline='', encoding='utf-8') as database:
        write = writer(database)
        write.writerow([room_number, guest_cpf, checkin_date, checkout_date, total_value, status])
