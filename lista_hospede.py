from database.guestDatabase.listarHospedes import listarHospedes

def lista_hospede():

    try:
        # Chama a função do arquivo listarHospedes.py
        hospedes = listarHospedes()[span_2](start_span)[span_2](end_span)

        # Verifica se o banco de dados possui registros
        if not hospedes:
            print("\nNenhum hóspede encontrado.")
            return

        # Exibição dos dados formatados
        print("\n" + "=" * 65)
        print("                 LISTA DE HÓSPEDES CADASTRADOS")
        print("=" * 65)
        print(f"{'CPF':<14} | {'Nome':<25} | {'Telefone':<15} | {'Idade'}")
        print("-" * 65)

        for hospede in hospedes:
            cpf = hospede.get('cpf', 'N/A')
            nome = hospede.get('name', 'N/A')
            telefone = hospede.get('phone_number', 'N/A')
            idade = hospede.get('age', 'N/A')

            print(f"{cpf:<14} | {nome:<25} | {telefone:<15} | {idade}")

        print("-" * 65)
        print(f"Total de registros encontrados: {len(hospedes)}\n")

    except FileNotFoundError:
        print("\nErro: O arquivo de banco de dados (guestDatabase.csv) ainda não foi criado.")
    except Exception as e:
        print(f"\nErro ao carregar a lista de hóspedes: {e}")
