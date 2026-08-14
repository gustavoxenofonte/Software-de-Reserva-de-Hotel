def cadastro_quartos():
    numero = int(input("Digite o número correspondente ao quarto: "))
    while numero < 0:
        print("ERRO! Número de quarto inváido")

    andar = int(input("Digite em qual andar do hotel o quarto está localizado: "))
    acomodação = int(input("Quantas pessoas o quarto acomoda? "))
    categoria = str(input("Qual será a categoria desse quarto (Simples, Intermediário ou Luxo)? "))

cadastro_quartos()

