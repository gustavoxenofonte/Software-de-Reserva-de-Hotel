from database.guestDatabase.excluirHospede import (
    excluirHospede, 
    GuestDontExists, 
    CPFAreNotNumbers, 
    CPFAreNotCorrect
)

def menu_excluir_hospede():
    while True:
        cpf = input('Digite o CPF do hóspede a ser excluído (apenas números): ')

        # Validação do algoritmo do CPF antes do envio ao banco
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
            print('CPF inválido.')
            continue

        # Chamada da função do banco de dados para exclusão
        try:
            excluirHospede(guest_cpf=cpf)
            print("Hóspede excluído com sucesso!")
            break
        except GuestDontExists:
            print("Erro: Nenhum hóspede foi encontrado com o CPF informado.")
        except (CPFAreNotNumbers, CPFAreNotCorrect) as e:
            print(f"Erro no formato do CPF: {e}")
        except Exception as e:
            print(f"Erro inesperado ao excluir: {e}")

# Execução da rotina
menu_excluir_hospede()