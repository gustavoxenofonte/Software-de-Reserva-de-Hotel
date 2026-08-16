from csv import reader, writer

class UserNameHaveComma(Exception):
    pass

class UserNameHaveSpace(Exception):
    pass

class NullUserName(Exception):
    pass

class UserNameNotStr(Exception):
    pass

def alterarUserName(new_user_name: str) -> None:
    # Verificações new_user_name
    if not isinstance(new_user_name, str):
        raise UserNameNotStr("User name deve ser uma str")
    if new_user_name.find(',') != -1:
        raise UserNameHaveComma("User name não pode ter vírgula")
    if new_user_name.find(' ') != -1:
        raise UserNameHaveSpace("User name não pode ter espaço")
    if len(new_user_name) == 0 :
        raise NullUserName("User name não pode ser vazio")

    # Adicionar no banco de dados
    with open("./database/adminDatabase/adminDatabase.csv", "r", encoding='utf-8') as database:
        databaseList = list(reader(database))
        databaseList[1][0] = new_user_name

    with open("./database/adminDatabase/adminDatabase.csv", "w", newline='', encoding='utf-8') as database:
        write = writer(database)
        write.writerows(databaseList)
