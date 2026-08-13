def cadastroReserva():
    try:
        nomeHospede = str(input("Insira o nome do hóspede que deseja fazer a reserva: ")).strip().title()
        cpfHospede = str(input("Insira o CPF do hóspede: ")).strip()
        cpfHospede = "".join(x for x in cpfHospede if x.isnumeric()) ##essa função retira todo caracter que não for númerico da str, como !., e etc.
        telefoneHospede = str(input("Insira o telefone do hóspede: ")).strip()
        telefoneHospede = "".join(x for x in telefoneHospede if x.isnumeric())
        while True:
            diasReservados = int(input("Insira por quantos dias deseja reservar o quarto: "))
            if diasReservados <= 0:
                print("Quantidade de dias inválido.")
            else:
                break    
    except ValueError:
        print("Valor inválido inserido.")
        return False