from csv import DictReader

class CPFAreNotNumbers(Exception):
    pass

class CPFAreNotCorrect(Exception):
    pass

class GuestDontExists(Exception):
    pass

def hospedeExiste(guest_cpf: str) -> bool:
    if not guest_cpf.isdecimal():    # Verifica se o cpf são somente números
        raise CPFAreNotNumbers("O cpf contém outros caracteres que não são números")

    if len(guest_cpf) != 11:    # Verifica se o cpf tem 11 caracteres
        raise CPFAreNotCorrect("O cpf não está correto, não tem 11 números")

    with open("./database/guestDatabase/guestDatabase.csv", "r", encoding='utf-8') as database:
            reader = DictReader(database)

            for row in reader:
                if row['cpf'] == guest_cpf:
                    return row                         # Se houver o cpf no banco de dados retorna o hóspede
    raise GuestDontExists("O hóspede não existe")      # Senão, dispara um erro
