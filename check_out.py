def check_out():
    cpfHospede = str(input("Insira o CPF do hóspede: ")).strip()
    cpfHospede = "".join(x for x in cpfHospede if x.isnumeric()) ##essa função .join() retira todo caracter que não for númerico da str, como !., e etc.
    while len(cpfHospede) != 11:  ##confere se o cpf é real
        print("CPF inválido")
        cpfHospede = str(input("Insira o CPF do hóspede: ")).strip()
        cpfHospede = "".join(x for x in cpfHospede if x.isnumeric())
    
    ## criar condição para testar se o hóspede já existe no banco de dados, se sim, fazer o check-out, se não, exibir o erro "Hóspede não encontrado"
    valor = check_out(cpfHospede)
    print("Check-out realizado")
    print(f"Valor total da estadia: R${valor:.2f}")