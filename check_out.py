import database.reservationDatabase
import database.guestDatabase

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

    #confere se a reserva existe no bd        
    if database.reservationDatabase.reservaExiste(cpfHospede):
        try:
            #confere se o hóspede está cadastrado no bd
            database.guestDatabase.hospedeExiste(cpfHospede)
            valor = float(database.reservationDatabase.checkOut(cpfHospede))
            print("Check-out realizado")
            print(f"Valor total da estadia: R${valor:.2f}")
        except:
            print("Usuário não encontrado")
    else:
        print("Reserva não existe")
