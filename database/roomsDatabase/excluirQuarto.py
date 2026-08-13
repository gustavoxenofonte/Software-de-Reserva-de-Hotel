from csv import DictWriter, DictReader

# Criação de Exceptions para tratativa de erros
class RoomNumberNotInt(Exception):
    pass

class RoomNumberZero(Exception):
    pass

class RoomDontExists(Exception):
    pass

# Criação da função para deletar quarto
def excluirQuarto(number: int):

    # Verificações
    if not isinstance(number, int):  #Verifica se number é inteiro
        raise RoomNumberNotInt("Número do quarto não é inteiro")
    if number == 0:  #Verifica se number é igual a 0
        raise RoomNumberZero("Número do quarto não pode ser Zero")

    # Cria uma lista pythom com as informações do banco de dados
    with open("./database/roomsDatabase/roomsDatabase.csv", "r", encoding='utf-8') as database:
        reader = DictReader(database)
        databaseList = list(reader)

    # Verificação se existe o quarto
    roomExists = False
    for row in databaseList:
        if row["number"] == f'{number}' :
            roomExists = True
    if not roomExists:
        raise RoomDontExists("O quarto não existe")


    # Deleta o quarto em específico e escreve novamente o banco de dados
    fieldnames = ['number', 'name', 'capacity', 'daily_value', 'free']
    with open("./database/roomsDatabase/roomsDatabase.csv", "w", newline='', encoding='utf-8') as database:
        for i, row in enumerate(databaseList):
            if row['number'] == f'{number}':
                del databaseList[i]
        writerDB = DictWriter(database, fieldnames=fieldnames)
        writerDB.writeheader()
        writerDB.writerows(databaseList)