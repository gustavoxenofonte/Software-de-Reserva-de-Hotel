from database.guestDatabase.hospedeExiste import (
    hospedeExiste, 
    GuestDontExists, 
    CPFAreNotNumbers, 
    CPFAreNotCorrect
)

def consultar_hospede():
    while True:
        cpf = input('CPF do hóspede: ')

        # Validação do CPF
        if len(cpf) != 11 or not cpf.isdigit():
            print('CPF inválido')
            continue

        soma = 0
        multiplicador = 10
        for digito in cpf[:9]:
            soma += int(digito) * multiplicador
            multiplicador -= 1
        resto = soma % 11
        verificador1 = 0 if resto in (0, 1) else 11 - resto

        soma = 0
        multiplicador = 11
        for digito in cpf[:10]:
            soma += int(digito) * multiplicador
            multiplicador -= 1
        resto = soma % 11
        verificador2 = 0 if resto in (0, 1) else 11 - resto

        if [verificador1, verificador2] != [int(cpf[-2]), int(cpf[-1])]:
            print('CPF inválido')
            continue

        # Consulta no banco de dados
        try:
            hospede = hospedeExiste(guest_cpf=cpf)
            print("Hóspede:")
            print(f"Nome: {hospede.get('name')}")
            print(f"Idade: {hospede.get('age')}")
            print(f"CPF: {hospede.get('cpf')}")
            print(f"Telefone: {hospede.get('phone_number')}")
            break
        except GuestDontExists:
            print("Hóspede não encontrado.")
            break
        except (CPFAreNotNumbers, CPFAreNotCorrect) as e:
            print(f"Erro no formato do CPF: {e}")
        except Exception as e:
            print(f"Erro inesperado: {e}")
