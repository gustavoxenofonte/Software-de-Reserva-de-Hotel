# cadastrarHospede(guest_cpf: str, name: str, phone_number: str, age: int) -> None
# Utilizado para cadastrar hóspedes no banco de dados
# guest_cpf deve ser no padrão: 00011122233 sem caracteres especiais
# phone_number deve ser no padrão: 88988887777 sem caracteres especiais

from csv import writer, DictReader

class CPFAreNotNumbers(Exception):
    pass

class CPFAreNotCorrect(Exception):
    pass

class GuestAlreadyExists(Exception):
    pass

class NameNotStr(Exception):
    pass

class EmptyName(Exception):
    pass

class PhoneNumberNotAllDigits(Exception):
    pass

class PhoneNumberNull(Exception):
    pass

class GuestIsMinor(Exception):
    pass

def cadastrarHospede(guest_cpf: str, name: str, phone_number: str, age: int) -> None:
    # Verificações
    if not guest_cpf.isdecimal():    # Verifica se o cpf são somente números
        raise CPFAreNotNumbers("O cpf contém outros caracteres que não são números")

    if len(guest_cpf) != 11:    # Verifica se o cpf tem 11 caracteres
        raise CPFAreNotCorrect("O cpf não está correto, não tem 11 números")

    with open("./database/guestDatabase/guestDatabase.csv", "r", encoding='utf-8') as database:    # Verifica se o hóspede já existe
        reader = DictReader(database)
        for row in reader:
            if row['cpf'] == guest_cpf:
                raise GuestAlreadyExists("Já existe um hóspede com esse cpf")

    # Verificações nome
    if not isinstance(name, str):
        raise NameNotStr("O nome não é Str")
    if name == '':
        raise EmptyName("O nome não pode ser vazio")

    # Verificações número de telefone
    if not phone_number.isdigit():
        raise PhoneNumberNotAllDigits("O número de telefone contém caracteres que não são dígitos")
    if phone_number == '':
        raise PhoneNumberNull("O número de telefone não pode ser vazio")

    # Verificações idade
    if age < 18:
        raise GuestIsMinor("O hóspede não pode ser menor de idade")

    # Adiciona o hóspede ao banco de dados
    with open("./database/guestDatabase/guestDatabase.csv", "a", newline='',  encoding='utf-8') as database:
        write = writer(database)
        write.writerow([guest_cpf, name, phone_number, age])
