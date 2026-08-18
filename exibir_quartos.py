import database.roomsDatabase

def exibir_quartos():
    print("\n Exibindo quartos...")
    quartos = database.roomsDatabase.listarQuartos()
    print("="*66)
    print("|NO.  |TIPO          |CAPACIDADE  |VALOR       |STATUS    |")
    for i in quartos:
        if i ['free'] == 'True':
            print(f"|{i['number']:<4} |{i['name']:<13} |{i['capacity']:<11} |{i['daily_value']:<11} |{'Disponível':<4}|")
        else:
            print(f"|{i['number']:<4} |{i['name']:<13} |{i['capacity']:<11} |{i['daily_value']:<11} |{'Ocupado':<4}|")
    print("="*66)