def cadastro_quartos():      #FUNÇÃO PARA CADASTRO DE QUARTOS

    vermelho = "\033[91m"   #COR PARA MENSAGENS DE ERRO
    verde = "\033[92m"      #COR PARA MENSAGENS DE SUCESSO
    reset = "\033[0m"       #VOLTA PARA A COR NORMAL

    #TRATAMENTO DE POSSÍVEL ERRO DE USUÁRIO - NÚMERO DE QUARTO SENDO MENOR OU IGUAL A ZERO
    while True:
        try:          #Testa se o número digitado é menor ou igual a zero. Se o valor retornado for "True", imprime uma mensagem de erro e repete a pergunta
            numero = int(input("Digite o número correspondente ao quarto: "))
            while numero <= 0 or numero > 100:
                print(f"{vermelho}ERRO! NÚMERO DE QUARTO INVÁLIDO!{reset}")
                numero = int(input("Digite o número correspondente ao quarto: "))
            break  
        except ValueError:
            print(f"{vermelho}ERRO! NÚMERO DE QUARTO INVÁLIDO!{reset}")

    #TRATAMENTO DE POSSÍVEL ERRO DE USUÁRIO - NÚMERO DE ANDAR CORRESPONDENTE AO QUARTO SENDO MENOR QUE ZERO (ZERO = ANDAR TÉRREO)
    while True:
        try:          #Testa se o número digitado é menor que zero. Se o valor retornado for "True", imprime uma mensagem de erro e repete a pergunta
            andar = int(input("Digite em qual andar do hotel o quarto está localizado: "))
            while andar < 0 or andar > 5:
                print(f"{vermelho}ERRO! ANDAR NÃO RECONHECIDO!{reset}")
                andar = int(input("Digite em qual andar do hotel o quarto está localizado: "))
            break
        except ValueError:
            print(f"{vermelho}ERRO! ANDAR NÃO RECONHECIDO!{reset}")

    #TRATAMENTO DE POSSÍVEL ERRO DE USUÁRIO - NÚMERO DE PESSOAS ACOMODADAS NO QUARTO SENDO MENOR QUE UM (POIS 0 SIGNIFICARIA QUE O QUARTO NÃO ACOMODA NINGUÉM)
    while True:
        try:          #Testa se o número digitado é menor que um. Se o valor retornado for "True", imprime uma mensagem de erro e repete a pergunta
            acomodacao = int(input("Quantas pessoas esse quarto acomoda? "))
            while acomodacao < 1 or acomodacao > 4:
                print(f"{vermelho}ERRO! OPÇÃO INVÁLIDA!{reset}")
                acomodacao = int(input("Quantas pessoas esse quarto acomoda? "))
            break
        except ValueError:
            print(f"{vermelho}ERRO! OPÇÃO INVÁLIDA!{reset}")

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

    while True:
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
            return {
                "Número": numero,
                "Andar": andar,
                "Acomodação": acomodacao,
                "Categoria": categoria
            }
        
        elif x == 2:
            print(f"{vermelho}Faça seu cadastro novamente com as informações corretas{reset}")
            return cadastro_quartos()   # Retorna para o início da função para o usuário alterar as informações incorretas
        
        else:
            print(f"{vermelho}ERRO! OPÇÃO INVÁLIDA!{reset}")
            
#ATRIBUE A FUNÇÃO "cadastro_quartos()" À VARIÁVEL "CADASTRO"
cadastro = cadastro_quartos()

#IMPRIME A FUNÇÃO
print (cadastro)