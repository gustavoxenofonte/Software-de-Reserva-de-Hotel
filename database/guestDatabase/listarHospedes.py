from csv import DictReader

# Função de listar os hóspedes
def listarHospedes() -> list:
    with open("./database/guestDatabase/guestDatabase.csv", "r", encoding='utf-8') as database:
        reader = DictReader(database)
        databaseList = list(reader)
    
    return databaseList    # Retorna uma lista de dicionários
