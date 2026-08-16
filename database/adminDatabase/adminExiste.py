from csv import reader

def adminExiste() -> bool:
    try:
        with open("./database/adminDatabase/adminDatabase.csv", "r", encoding='utf-8') as database:
            read = list(reader(database))
            admin = read[1]                # Tenta adcionar o login administrativo a uma variável
        return True                        # Se conseguir, retorna True
    except:
        return False       # Se der erro, retorna false
