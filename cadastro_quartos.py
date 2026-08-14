def cadastro_quartos():
    
    while True:
        try:
            numero = int(input("Digite o número correspondente ao quarto: "))
            while numero <= 0:
                numero = int(input("Digite o número correspondente ao quarto: "))
            break
        except ValueError:
            print ("ERRO! Número de quarto inválido!")


    while True:
        try:
            andar = int(input("Digite em qual andar do hotel o quarto está localizado: "))
            while andar < 0:
                andar = int(input("Digite em qual andar do hotel o quarto está localizado: "))
            break
        except ValueError:
            print ("ERRO! Andar não reconhecido!")

    while True:
        try:
            acomodacao = int(input("Quantas pessoas esse quarto acomoda? "))
            while acomodacao < 1:
                acomodacao = int(input("Quantas pessoas esse quarto acomoda? "))
            break
        except ValueError:
            print ("ERRO! Opção inválida!")

    while True:
        try:
            categoria = str(input("Qual será a categoria desse quarto (Simples, Intermediário ou Luxo)? ")).strip().capitalize()
            while categoria != "Simples" and categoria != "Intermediário" and categoria != "Luxo":
                categoria = str(input("Qual será a categoria desse quarto (Simples, Intermediário ou Luxo)? ")).strip().capitalize()
            break
        except ValueError:
            print ("ERRO! Opção não disponível!")

    print ("QUARTO CADASTRADO COM SUCESSO!")

    return{
        "Número": numero,
        "Andar": andar,
        "Acomodação": acomodacao,
        "Categoria": categoria
    }

cadastro = cadastro_quartos()

print (cadastro)