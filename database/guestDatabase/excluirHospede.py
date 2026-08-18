from csv import DictReader, DictWriter

class CPFAreNotNumbers(Exception):
    pass

class CPFAreNotCorrect(Exception):
    pass

class GuestDontExists(Exception):
    pass

def excluirHospede(guest_cpf: str) -> None:
    # Verificações
    if not guest_cpf.isdecimal():    # Verifica se o cpf são somente números
        raise CPFAreNotNumbers("O cpf contém outros caracteres que não são números")

    if len(guest_cpf) != 11:    # Verifica se o cpf tem 11 caracteres
        raise CPFAreNotCorrect("O cpf não está correto, não tem 11 números")

    # Salvar a lista de hóspedes
    with open("./database/guestDatabase/guestDatabase.csv", "r", encoding='utf-8') as database:
        databaseList = list(DictReader(database))

    # Verifica se existe e deleta os dados do hóspede
    exists = False
    for i, row in enumerate(databaseList):
        if row['cpf'] == guest_cpf:
            del databaseList[i]
            exists = True

    if not exists:
        raise GuestDontExists("O hóspede desse cpf não existe.")

    fieldnames = ['cpf', 'name', 'phone_number', 'age']
    with open("./database/guestDatabase/guestDatabase.csv", "w", newline='', encoding='utf-8') as database:
        writer = DictWriter(database, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(databaseList)
