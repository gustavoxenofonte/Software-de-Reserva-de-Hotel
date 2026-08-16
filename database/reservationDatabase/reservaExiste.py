from csv import DictReader

class CPFAreNotNumbers(Exception):
    pass

class CPFAreNotCorrect(Exception):
    pass

def reservaExiste(guest_cpf: str) -> bool:
    if not guest_cpf.isdecimal():    # Verifica se o cpf são somente números
        raise CPFAreNotNumbers("O cpf contém outros caracteres que não são números")

    if len(guest_cpf) != 11:    # Verifica se o cpf tem 11 caracteres
        raise CPFAreNotCorrect("O cpf não está correto, não tem 11 números")

    with open("./database/reservationDatabase/reservationDatabase.csv", "r", encoding='utf-8') as database:
            reader = DictReader(database)

            for row in reader:
                if row['guest_cpf'] == guest_cpf:
                    if row['status'] in ['reservado', 'hospedado']:
                         return True
    return False                                       # Senão, retorna False
