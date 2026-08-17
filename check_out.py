import database.reservationDatabase

def check_out():
    print("="*50)
    print("MENU CHECK-OUT")
    print("Insira 0 para sair")
    print("="*50)
    cpfHospede = str(input("Insira o CPF do hóspede: ")).strip()
    cpfHospede = "".join(x for x in cpfHospede if x.isnumeric()) ##essa função .join() retira todo caracter que não for númerico da str, como !., e etc.
    if cpfHospede == '0':
        return("Fim do menu")
    while len(cpfHospede) != 11:  ##confere se o cpf é real
        print("CPF inválido")
        cpfHospede = str(input("Insira o CPF do hóspede: ")).strip()
        cpfHospede = "".join(x for x in cpfHospede if x.isnumeric())
        if cpfHospede == '0':
            return ("Fim do menu")
            
    
    ## criar condição para testar se o hóspede já existe no banco de dados, se sim, fazer o check-out, se não, exibir o erro "Hóspede não encontrado"
    valor = database.reservationDatabase.checkOut(cpfHospede)
    print("Check-out realizado")
    print(f"Valor total da estadia: R${valor:.2f}")