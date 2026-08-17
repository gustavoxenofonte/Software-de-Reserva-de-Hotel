from csv import writer, reader

class PasswordHaveComma(Exception):
    pass

class PasswordHaveSpace(Exception):
    pass

class NullPassword(Exception):
    pass

class PasswordNotStr(Exception):
    pass

def alterarSenha(new_password: str) -> None:
    # Verificações new_password
    if not isinstance(new_password, str):
        raise PasswordNotStr("Password deve ser uma str")
    if new_password.find(',') != -1:
        raise PasswordHaveComma("Password não pode ter vírgula")
    if new_password.find(',') != -1:
        raise PasswordHaveSpace("Password não pode ter espaço")
    if len(new_password) == 0 :
        raise NullPassword("Password não pode ser vazio")

    # Alterar no banco de dados
    with open("./database/adminDatabase/adminDatabase.csv", "r", encoding='utf-8') as database:
        databaseList = list(reader(database))
        databaseList[1][1] = new_password

    with open("./database/adminDatabase/adminDatabase.csv", "w", newline='', encoding='utf-8') as database:
        write = writer(database)
        write.writerows(databaseList)
