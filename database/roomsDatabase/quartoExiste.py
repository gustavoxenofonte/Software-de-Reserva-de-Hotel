from csv import DictReader

class RoomNumberNotInt(Exception):
    pass

class RoomNumberZero(Exception):
    pass

def quartoExiste(room_number: int):
        
    # Verificações
    if not isinstance(room_number, int):  #Verifica se number é inteiro
        raise RoomNumberNotInt("Número do quarto não é inteiro")
    if room_number == 0:  #Verifica se number é igual a 0
        raise RoomNumberZero("Número do quarto não pode ser Zero")

    # Cria uma lista pythom com as informações do banco de dados
    with open("./database/roomsDatabase/roomsDatabase.csv", "r", encoding='utf-8') as database:
        reader = DictReader(database)
        databaseList = list(reader)

    # Verificação se existe o quarto
    roomExists = False
    for row in databaseList:
        if row["number"] == f'{room_number}' :
            roomExists = True

    return roomExists