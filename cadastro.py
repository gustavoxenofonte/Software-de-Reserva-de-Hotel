from datetime import datetime
from database.guestDatabase.cadastrarHospede import cadastrarHospede, GuestIsMinor, GuestAlreadyExists

def cadastro_hospede()
    def nascimento():
        print('digite a data de nascimento do hóspede')
    
        while True:
            try:
                dia = int(input('dia: '))
                if 1 <= dia <= 31:
                    break
                else:
                    print('Dia inválido. Digite o dia do nascimento do hóspede.')
            except ValueError:
                print('Entrada inválida. Por favor, digite apenas números')
    
        while True:
            try:
                mes = int(input('mês: '))
                if 1 <= mes <= 12:
                    break
                else:
                    print('mês inválido. Digite o mês do nascimento do hóspede.')
            except ValueError:
                print('Entrada inválida. Por favor, digite apenas números.')
    
        while True:
            try:
                ano = int(input('ano: '))
                if 1900 <= ano <= 2026:
                    break
                else:
                    print('ano inválido. Digite o ano do nascimento do hóspede no formato AAAA.')
            except ValueError:
                print('Entrada inválida. Por favor, digite apenas números.')
    
        return dia, mes, ano
    
    # Nome do hóspede
    nome = input('Nome do hóspede: ')
    
    # Data de nascimento
    dia, mes, ano = nascimento()
    data_formatada = f'{dia}/{mes}/{ano}'
    
    # Cálculo da idade com base na data de nascimento
    hoje = datetime.now()
    idade = hoje.year - ano - ((hoje.month, hoje.day) < (mes, dia))
    
    # CPF (com validação)
    while True:
        try:
            cpf = input('CPF: ')
    
            if len(cpf) != 11 or not cpf.isdigit():
                print('CPF inválido')
                continue
    
            soma = 0
            multiplicador = 10
            for digito in cpf[:9]:
                numero = int(digito) * multiplicador
                multiplicador -= 1
                soma += numero
            resto = soma % 11
            verificador1 = 0 if resto in (0, 1) else 11 - resto
    
            soma = 0
            multiplicador = 11
            for digito in cpf[:10]:
                numero = int(digito) * multiplicador
                multiplicador -= 1
                soma += numero
            resto = soma % 11
            verificador2 = 0 if resto in (0, 1) else 11 - resto
    
            verificador = [verificador1, verificador2]
            verificador_o = [int(cpf[-2]), int(cpf[-1])]
    
            if verificador == verificador_o:
                break
            else:
                print('CPF inválido')
    
        except ValueError:
            print('CPF inválido')
    
    # Telefone
    telefone = input('Telefone (apenas números): ')
    
    # Envio das informações coletadas para o banco de dados
    try:
        cadastrarHospede(guest_cpf=cpf, name=nome, phone_number=telefone, age=idade)
        print("Hóspede cadastrado com sucesso!")
    except GuestIsMinor:
        print("Erro: O hóspede é menor de idade e não pode ser cadastrado.")
    except GuestAlreadyExists:
        print("Erro: Já existe um hóspede cadastrado com esse CPF.")
    except Exception as e:
        print(f"Erro ao cadastrar: {e}")
