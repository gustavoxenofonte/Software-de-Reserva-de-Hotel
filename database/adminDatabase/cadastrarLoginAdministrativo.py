from csv import writer

class UserNameHaveComma(Exception):
    pass

class UserNameHaveSpace(Exception):
    pass

class NullUserName(Exception):
    pass

class UserNameNotStr(Exception):
    pass

class PasswordHaveComma(Exception):
    pass

class PasswordHaveSpace(Exception):
    pass

class NullPassword(Exception):
    pass

class PasswordNotStr(Exception):
    pass

def cadastrarLoginAdministrativo(user_name: str, password: str) -> None:
    # Verificações user_name
    if not isinstance(user_name, str):
        raise UserNameNotStr("User name deve ser uma str")
    if user_name.find(',') != -1:
        raise UserNameHaveComma("User name não pode ter vírgula")
    if user_name.find(' ') != -1:
        raise UserNameHaveSpace("User name não pode ter espaço")
    if len(user_name) == 0 :
        raise NullUserName("User name não pode ser vazio")

    # Verificações password
    if not isinstance(password, str):
        raise PasswordNotStr("Password deve ser uma str")
    if password.find(',') != -1:
        raise PasswordHaveComma("Password não pode ter vírgula")
    if password.find(',') != -1:
        raise PasswordHaveSpace("Password não pode ter espaço")
    if len(password) == 0 :
        raise NullPassword("Password não pode ser vazio")

    # Adicionar no banco de dados
    with open("./database/adminDatabase/adminDatabase.csv", "a", newline='', encoding='utf-8') as database:
        write = writer(database)
        write.writerow([user_name, password])
