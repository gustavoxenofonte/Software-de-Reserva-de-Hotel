import database.roomsDatabase

def cadastro_quartos():      #FUNÇÃO PARA CADASTRO DE QUARTOS

    vermelho = "\033[91m"   #COR PARA MENSAGENS DE ERRO
    verde = "\033[92m"      #COR PARA MENSAGENS DE SUCESSO
    reset = "\033[0m"       #VOLTA PARA A COR NORMAL

    print("\n--- CADASTRAR NOVO QUARTO ---")

    #TRATAMENTO DE POSSÍVEL ERRO DE USUÁRIO - NÚMERO DE QUARTO SENDO MENOR OU IGUAL A ZERO
    while True:
        try:          #Testa se o número digitado é menor ou igual a zero. Se o valor retornado for "True", imprime uma mensagem de erro e repete a pergunta.
            numero = int(input("Digite o número correspondente ao quarto: "))
            while numero <= 0 or numero > 100:
                print(f"{vermelho}ERRO! NÚMERO DE QUARTO INVÁLIDO!{reset}")
                numero = int(input("Digite o número correspondente ao quarto: "))
            if database.roomsDatabase.quartoExiste(numero):
                print(f"{vermelho}ERRO! QUARTO JÁ EXISTENTE!")
            else:
                break
        except ValueError:
            print(f"{vermelho}ERRO! NÚMERO DE QUARTO INVÁLIDO!{reset}")
        

    #TRATAMENTO DE POSSÍVEL ERRO DE USUÁRIO - NÚMERO DE PESSOAS ACOMODADAS NO QUARTO SENDO MENOR QUE UM (POIS 0 SIGNIFICARIA QUE O QUARTO NÃO ACOMODA NINGUÉM)
    while True:
        try:          #Testa se o número digitado é menor que um. Se o valor retornado for "True", imprime uma mensagem de erro e repete a pergunta.
            acomodacao = int(input("Quantas pessoas esse quarto acomoda? "))
            while acomodacao < 1 or acomodacao > 4:
                print(f"{vermelho}ERRO! OPÇÃO INVÁLIDA!{reset}")
                acomodacao = int(input("Quantas pessoas esse quarto acomoda? "))
            break
        except ValueError:
            print(f"{vermelho}ERRO! OPÇÃO INVÁLIDA!{reset}")

    while True:
            try:          #Testa se o número digitado é menor ou igual a zero. Se o valor retornado for "True", imprime uma mensagem de erro e repete a pergunta.
                valor = float(input("Digite o valor da diária do quarto: "))
                while valor <= 0 or valor > 1000:
                    print(f"{vermelho}ERRO! VALOR NÃO RECONHECIDO!{reset}")
                    valor = int(input("Digite o valor da diária do quarto: "))
                break
            except ValueError:
                print(f"{vermelho}ERRO! VALOR NÃO RECONHECIDO!{reset}")

    #TRATAMENTO DE POSSÍVEL ERRO DE USUÁRIO - CATEGORIA DO QUARTO SENDO DIFERENTE DE "SIMPLES, INTERMEDIÁRIO E LUXO"
    while True:
        try:          #Testa se a categoria digitada é diferente de "Simples, Intermediário e Luxo". Se o valor retornado for "True", imprime uma mensagem de erro e repete a pergunta
            categoria = str(input("Qual será a categoria desse quarto (Simples, Intermediário ou Luxo)? ")).strip().capitalize()
            while categoria != "Simples" and categoria != "Intermediário" and categoria != "Luxo":
                print(f"{vermelho}ERRO! OPÇÃO INVÁLIDA!{reset}")
                categoria = str(input("Qual será a categoria desse quarto (Simples, Intermediário ou Luxo)? ")).strip().capitalize()
            break
        except ValueError:
            print(f"{vermelho}ERRO! OPÇÃO INVÁLIDA!{reset}")

    while True:          #Confirma informações para cadastro, evitando cadastro acidental.
        print("Confirma as Informações para Cadastro?")
        print("1.SIM")
        print("2.NÃO")
        try:
            x = int(input("Digite o número correspondente a opção desejada: "))
        except ValueError:
            print(f"{vermelho}ERRO! OPÇÃO INVÁLIDA!{reset}")
            continue
    
        if x == 1:
            print(f"{verde}QUARTO CADASTRADO COM SUCESSO!{reset}")
            break
        
        elif x == 2:
            print(f"{vermelho}Faça seu cadastro novamente com as informações corretas{reset}")
            return cadastro_quartos()   # Retorna para o início da função para o usuário alterar as informações incorretas
        
        else:
            print(f"{vermelho}ERRO! OPÇÃO INVÁLIDA!{reset}")

    database.roomsDatabase.cadastrarQuarto(numero,categoria,acomodacao,valor,True)