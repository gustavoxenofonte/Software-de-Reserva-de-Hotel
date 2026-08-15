import datetime ## biblioteca para tratar as datas

def cadastroReserva():

        cpfHospede = str(input("Insira o CPF do hóspede: ")).strip()
        cpfHospede = "".join(x for x in cpfHospede if x.isnumeric()) ##essa função .join() retira todo caracter que não for númerico da str, como !., e etc.
        while len(cpfHospede) != 11:  ##confere se o cpf é real
            print("CPF inválido")
            cpfHospede = str(input("Insira o CPF do hóspede: ")).strip()
            cpfHospede = "".join(x for x in cpfHospede if x.isnumeric())

        ## criar condição para testar se o hóspede já existe no banco de dados, se sim, não executar os inputs dos dados abaixo

        nomeHospede = str(input("Insira o nome do hóspede que deseja fazer a reserva: ")).strip().title()

        telefoneHospede = str(input("Insira o telefone do hóspede: ")).strip()
        telefoneHospede = "".join(x for x in telefoneHospede if x.isnumeric()) ##realiza o mesmo que na variável cpf
        while len(telefoneHospede) != 11:
            print("Telefone inválido")
            telefoneHospede = str(input("Insira o telefone do hóspede: ")).strip()
            telefoneHospede = "".join(x for x in telefoneHospede if x.isnumeric())
        
        while True:
            try:
                idadeHospede = int(input("Insira a idade do hóspede: "))
                while idadeHospede <= 0:
                    print("Idade inválida")
                    idadeHospede = int(input("Insira a idade do hóspede: "))
                break
            except ValueError:
                print("Valor inválido")

        #cadastrarHospede(cpfHospede, nomeHospede, telefoneHospede, idade)
                
        while True:
            try:         
                numeroQuarto = int(input("Número do quarto a ser reservado: "))
                while numeroQuarto <= 0:
                    print("Número de quarto inválido")
                    numeroQuarto = int(input("Número do quarto a ser reservado: "))

                #quartos = listarQuartos()                     #checa se o quarto existe no banco de dados
                #for i in quartos:
                #    if numeroQuarto != quartos[i]['number']:
                #        pass
                #    else:
                #        print("Quarto válido")
                #        quartoAtual = quartos[i]            #salva o quarto que está sendo cadastrado
                #        break
    
                break
            except ValueError:
                print("Valor inválido")

        while True:
            try:
                dataCheckin = str(input("Insira o a data de check-in(DD/MM/YYYY): ")).strip()
                dataCheckin = datetime.date.strptime(f"{dataCheckin}", '%d/%m/%Y')    #transforma o str que o usuário digitou em uma variável do tipo date
                while dataCheckin <= datetime.date.today():                             #verifica se a data de check-in é válida(apartir do próximo dia)
                    print("Data de check-in inválida")
                    dataCheckin = str(input("Insira o a data de check-in(DD/MM/YYYY): ")).strip()
                    dataCheckin = datetime.date.strptime(f"{dataCheckin}", '%d/%m/%Y')   
                break 
            except ValueError:
                print("Data inválida")

        while True:
            try:
                dataCheckout = str(input("Insira o a data de check-out(DD/MM/YYYY): ")).strip()
                dataCheckout = datetime.date.strptime(dataCheckout, "%d/%m/%Y")
                while dataCheckout < dataCheckin:                      #verifica se a data de check-out é antes da data de check-in, se sim, retorna um erro
                    print("Data de check-out inválida")
                    dataCheckout = str(input("Insira o a data de check-out(DD/MM/YYYY): ")).strip()
                    dataCheckout = datetime.date.strptime(dataCheckout, "%d/%m/%Y")
                break
            except ValueError:
                print("Valor inválido")

        diasHospedados = dataCheckout - dataCheckin
        valorTotal = diasHospedados * quartoAtual['daily_value']

        if dataCheckin == datetime.date.today() and quartoAtual['free'] == True:        #confere se o quarto atual pode receber o check-in
            cadastrarReserva(numeroQuarto, cpfHospede, dataCheckin, dataCheckout, valorTotal, 'hospedado')
            alterarStatusQuarto(numeroQuarto, False)
            check_in(cpfHospede)
            print("Reserva Feita")
            print("Check-in automático realizado")
        if dataCheckin == datetime.date.today() and quartoAtual['free'] == False:
            print("Erro na reserva, quarto reservado para o dia atual, reservar para o dia seguinte")
        else:
            cadastrarReserva(numeroQuarto, cpfHospede, dataCheckin, dataCheckout, valorTotal, 'reservado')
            print("Reserva Feita")
