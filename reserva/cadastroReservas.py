import datetime ## biblioteca para tratar as datas

## Exceptions para tratar erros de entrada do usuário


class DataInvalida(Exception):
    pass

class IdadeInvalida(Exception):
    pass

class DiasReservadosInvalidos(Exception):
    pass

class NumeroQuartoInvalido(Exception):
     pass

class CpfInvalido(Exception):
     pass

class TelefoneInvalido(Exception):
     pass

class DataCheckinInvalida(Exception):
     pass

class DataCheckoutInvalida(Exception):
     pass

def cadastroReserva():
        nomeHospede = str(input("Insira o nome do hóspede que deseja fazer a reserva: ")).strip().title()

        cpfHospede = str(input("Insira o CPF do hóspede: ")).strip()
        cpfHospede = "".join(x for x in cpfHospede if x.isnumeric()) ##essa função .join() retira todo caracter que não for númerico da str, como !., e etc.
        while len(cpfHospede) != 11:  ##confere se o cpf é real
            cpfHospede = str(input("Insira o CPF do hóspede: ")).strip()
            cpfHospede = "".join(x for x in cpfHospede if x.isnumeric())
             

        telefoneHospede = str(input("Insira o telefone do hóspede: ")).strip()
        telefoneHospede = "".join(x for x in telefoneHospede if x.isnumeric()) ##realiza o mesmo que na variável cpf
        while len(telefoneHospede) != 11:
            telefoneHospede = str(input("Insira o telefone do hóspede: ")).strip()
            telefoneHospede = "".join(x for x in telefoneHospede if x.isnumeric())
             
        while True:
            try:
                idadeHospede = int(input("Insira a idade do hóspede: "))
                while idadeHospede <= 0:
                    idadeHospede = int(input("Insira a idade do hóspede: "))
            except ValueError:
                 print("Valor inválido")
                 break
                 
                     
                        

        
        numeroQuarto = int(input("Número do quarto a ser reservado: "))
        if numeroQuarto <= 0:
                raise NumeroQuartoInvalido("Número do quarto inválido")

        try:
            dataCheckin = str(input("Insira o a data de check-in(DD/MM/YYYY): ")).strip()
            dataCheckin = datetime.date.strptime(f"{dataCheckin}", '%d/%m/%Y')    #transforma o str que o usuário digitou em uma variável do tipo date
            if dataCheckin <= datetime.date.today():                                 #verifica se a data de check-in é válida(apartir do próximo dia)
                raise DataCheckinInvalida("Data de Chek-in inválida")
            
            dataCheckout = str(input("Insira o a data de check-on(DD/MM/YYYY): ")).strip()
            dataCheckout = datetime.date.strptime(dataCheckout, "%d/%m/%Y")
            if dataCheckout < dataCheckin:                       #verifica se a data de check-out é antes da data de check-in, se sim, retorna um erro

        except ValueError:
            raise DataInvalida("Data inválida")
        
cadastroReserva()