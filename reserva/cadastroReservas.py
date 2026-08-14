import datetime ## biblioteca para tratar as datas

def cadastroReserva():

        cpfHospede = str(input("Insira o CPF do hóspede: ")).strip()
        cpfHospede = "".join(x for x in cpfHospede if x.isnumeric()) ##essa função .join() retira todo caracter que não for númerico da str, como !., e etc.
        while len(cpfHospede) != 11:  ##confere se o cpf é real
            print("CPF inválido")
            cpfHospede = str(input("Insira o CPF do hóspede: ")).strip()
            cpfHospede = "".join(x for x in cpfHospede if x.isnumeric())


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
                
        while True:
            try:         
                numeroQuarto = int(input("Número do quarto a ser reservado: "))
                while numeroQuarto <= 0:
                    print("Número de quarto inválido")
                    numeroQuarto = int(input("Número do quarto a ser reservado: "))
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
        