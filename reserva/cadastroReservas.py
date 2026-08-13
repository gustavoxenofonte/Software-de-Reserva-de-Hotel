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


def cadastroReserva():
    try:
        nomeHospede = str(input("Insira o nome do hóspede que deseja fazer a reserva: ")).strip().title()

        cpfHospede = str(input("Insira o CPF do hóspede: ")).strip()
        cpfHospede = "".join(x for x in cpfHospede if x.isnumeric()) ##essa função .join() retira todo caracter que não for númerico da str, como !., e etc.

        telefoneHospede = str(input("Insira o telefone do hóspede: ")).strip()
        telefoneHospede = "".join(x for x in telefoneHospede if x.isnumeric()) ##realiza o mesmo que na variável cpf

        idadeHospede = int(input("Insira a idade do hóspede: "))
        if idadeHospede <= 0:
                raise IdadeInvalida("Idade inválida")
        
        diasReservados = int(input("Insira por quantos dias deseja reservar o quarto: "))
        if diasReservados <= 0:
                raise DiasReservadosInvalidos("Dias reservados inválidos")

        numeroQuarto = int(input("Número do quarto a ser reservado: "))
        if numeroQuarto <= 0:
                raise NumeroQuartoInvalido("Número do quarto inválido")

        try:
            diaCheckin = int(input("Insira o dia de Check-in do hóspede: "))
            mesCheckin = int(input("Insira o mês de Check-in do hóspede(digite 0 para o mês atual): "))
            anoCheckin = int(input("Insira o ano de Check-in do hóspede(digite 0 para o ano atual): "))
            dataCheckin = datetime.date(anoCheckin,mesCheckin,diaCheckin)
        except ValueError:
            raise DataInvalida("Data inválida")
        
    except ValueError:
        print("Valor inválido inserido.")
        return False