from csv import DictReader

# Função de listar as reservas
def listarReservas() -> list:
    with open("./database/reservationDatabase/reservationDatabase.csv", "r", encoding='utf-8') as database:
        reader = DictReader(database)
        databaseList = list(reader)
    
    return databaseList    # Retorna uma lista de dicionários
