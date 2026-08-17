from csv import reader

class AdminLoginDontExists(Exception):
    pass

def adminExiste() -> bool:
    try:
        with open("./database/adminDatabase/adminDatabase.csv", "r", encoding='utf-8') as database:
            read = list(reader(database))
            admin = read[1]                # Tenta adcionar o login administrativo a uma variável
        return admin                        # Se conseguir, retorna a lista
    except:
        raise AdminLoginDontExists("O login administrativo não existe")      # Se der erro, retorna o erro de login inexistente