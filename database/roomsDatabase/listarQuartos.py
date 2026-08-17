from csv import DictReader

# Criação da função para listar os quartos
def listarQuartos() -> list:
    with open("./database/roomsDatabase/roomsDatabase.csv", "r", encoding='utf-8') as database:
        reader = DictReader(database)
        databaseList = list(reader)

    return databaseList # Retorna uma lista de dicionários