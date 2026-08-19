import datetime ## biblioteca para tratar as datas
import os
import sys
caminho_absoluto = os.path.abspath(os.curdir)
sys.path.insert(0, caminho_absoluto)
import database.roomsDatabase
import database.reservationDatabase
import database.guestDatabase

def cadastroReserva():
        #Função para exibir o menu
        def menu():
            print("="*50)
            print("MENU CADASTRO DE RESERVA")
            print("Insira 0 a qualquer momento para sair desse menu")
            print("="*50)
            print()
            
        while True:
            menu()

            cpfHospede = str(input("Insira o CPF do hóspede: ")).strip()
            cpfHospede = "".join(x for x in cpfHospede if x.isnumeric()) ##essa função .join() retira todo caracter que não for númerico da str, como !., e etc.
            if cpfHospede == '0':
                return print("Fim do programa")
            while len(cpfHospede) != 11:  ##confere se o cpf é real
                print("CPF inválido")
                cpfHospede = str(input("Insira o CPF do hóspede: ")).strip()
                cpfHospede = "".join(x for x in cpfHospede if x.isnumeric())
                if cpfHospede == '0':    #interrompe a execução
                    return print("Fim do programa")
            if database.reservationDatabase.reservaExiste(cpfHospede):      #testa se já há uma reserva com esse cpf para evitar cópias
                print("Erro. CPF já existe no branco de dados de reservas.")
                return print("Fim do programa")

            try:
                if database.guestDatabase.hospedeExiste(cpfHospede):    #checa se o hóspede já está cadastrado
                    print("Usuário já cadastrado")
                    break
            except:
                nomeHospede = str(input("Insira o nome do hóspede que deseja fazer a reserva: ")).strip().title()
                if nomeHospede == '0':
                    return print("Fim do programa")

                telefoneHospede = str(input("Insira o telefone do hóspede: ")).strip()
                telefoneHospede = "".join(x for x in telefoneHospede if x.isnumeric()) ##realiza o mesmo que na variável cpf
                if telefoneHospede == '0':
                    return print("Fim do programa")
                while len(telefoneHospede) != 11:
                    print("Telefone inválido")
                    telefoneHospede = str(input("Insira o telefone do hóspede: ")).strip()
                    telefoneHospede = "".join(x for x in telefoneHospede if x.isnumeric())
                    if telefoneHospede == '0':
                        return print("Fim do programa")
                
                while True:
                    try:
                        idadeHospede = int(input("Insira a idade do hóspede: "))
                        if idadeHospede == 0:
                            return print("Fim do programa")
                        while idadeHospede < 18:
                            print("Idade inválida ou Hóspede menor de idade")
                            idadeHospede = int(input("Insira a idade do hóspede: "))
                            if idadeHospede == 0:
                                return print("Fim do programa")
                        break
                    except ValueError:
                        print("Valor inválido")

                #Pergunta se o usuário confirma, se não, reinicia apenas o loop dos dados do hóspede
                confirmar = str(input("Confirma as informações acima?(S/N) ")).strip().upper()
                while confirmar not in "SN":
                    print("Opção inválida")
                    confirmar = str(input("Confirma as informações acima?(S/N) ")).strip().upper()
                if confirmar == 'S':
                    database.guestDatabase.cadastrarHospede(cpfHospede, nomeHospede, telefoneHospede, idadeHospede)
                    os.system('cls' if os.name == 'nt' else 'clear')  ##limpa o terminal das informações anteriores
                    menu()
                    print("Usuário cadastrado")
                    break
                elif confirmar == 'N':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Insira novamente as informações")


        while True:
            while True:
                try:         
                    numeroQuarto = int(input("Número do quarto a ser reservado: "))
                    if numeroQuarto == 0:
                        return print("Fim do programa")
                    while numeroQuarto < 0:
                        print("Número de quarto inválido")
                        numeroQuarto = int(input("Número do quarto a ser reservado: "))
                        if numeroQuarto == 0:
                            return print("Fim do programa")

                    if database.roomsDatabase.quartoExiste(numeroQuarto):           #checa se o quarto existe no banco de dados
                        quartos = database.roomsDatabase.listarQuartos()            #salva uma lista com todos os quartos   
                        for quarto in quartos:
                            if numeroQuarto == int(quarto['number']):
                                print("Quarto válido")
                                valorquartoAtual = float(quarto['daily_value'])            #salva o quarto que está sendo cadastrado
                                quartoAtualReservado = quarto['free']
                                if quartoAtualReservado == 'True':
                                    quartoAtualReservado = True
                                else:
                                    quartoAtualReservado = False
                                break            
                        break
                    else:
                        print("Quarto não existe")
                            
                except ValueError:
                    print("Valor inválido")

            while True:
                try:
                    dataCheckin = str(input("Insira o a data de check-in(DD/MM/YYYY): ")).strip()
                    if dataCheckin == '0':
                        return print("Fim do programa")
                    dataCheckin = datetime.date.strptime(f"{dataCheckin}", '%d/%m/%Y')    #transforma o str que o usuário digitou em uma variável do tipo date
                    while dataCheckin < datetime.date.today():                             #verifica se a data de check-in é válida(apartir do dia atual)
                        print("Data de check-in inválida")
                        dataCheckin = str(input("Insira o a data de check-in(DD/MM/YYYY): ")).strip()
                        if dataCheckin == '0':
                            return print("Fim do programa")
                        dataCheckin = datetime.date.strptime(f"{dataCheckin}", '%d/%m/%Y')   
                    break 
                except ValueError:
                    print("Data inválida")

            while True:
                try:
                    dataCheckout = str(input("Insira o a data de check-out(DD/MM/YYYY): ")).strip()
                    if dataCheckout == '0':
                        return print("Fim do programa")
                    dataCheckout = datetime.date.strptime(dataCheckout, "%d/%m/%Y")
                    while dataCheckout < dataCheckin:                      #verifica se a data de check-out é antes da data de check-in, se sim, retorna um erro
                        print("Data de check-out inválida")
                        dataCheckout = str(input("Insira o a data de check-out(DD/MM/YYYY): ")).strip()
                        if dataCheckout == '0':
                            return print("Fim do programa")
                        dataCheckout = datetime.date.strptime(dataCheckout, "%d/%m/%Y")
                    break
                except ValueError:
                    print("Valor inválido")

            confirmar = str(input("Confirma as informações acima?(S/N) ")).strip().upper()
            while confirmar not in "SN":
                print("Opção inválida")
                confirmar = str(input("Confirma as informações acima?(S/N) ")).strip().upper()
            if confirmar == 'S':
                os.system('cls' if os.name == 'nt' else 'clear')
                menu()
                print("Reserva sendo analisada")
            elif confirmar == 'N':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Insira novamente as informações")
                continue

            diasHospedados = dataCheckout - dataCheckin
            valorTotal = (1 + diasHospedados.days) * valorquartoAtual  ##o .days converte a variável diasHospedados em um número inteiro

            if dataCheckin == datetime.date.today() and quartoAtualReservado == False:      #caso o quarto já esteja hospedado, exibe o erro
                print("Erro na reserva, quarto reservado para o dia atual, reservar para o dia seguinte")
                continue
            else:
                # cadastra a reserva
                database.reservationDatabase.cadastrarReserva(numeroQuarto, cpfHospede, dataCheckin, dataCheckout, valorTotal, 'reservado')
                print("Reserva Feita")
                #confere se o quarto atual pode receber o check-in automático caso a data seja a do dia atual
                if dataCheckin == datetime.date.today() and quartoAtualReservado == True:        
                    database.reservationDatabase.checkIn(cpfHospede)
                    print("Check-in automático realizado")
                    print(f"Valor da reserva: R${valorTotal}")
                break
