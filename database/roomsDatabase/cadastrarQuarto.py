from csv import writer

# Exceptions customizadas para melhor tratamento de erros
class RoomNumberNotInt(Exception):
    pass

class RoomNumberZero(Exception):
    pass

class NameNotStr(Exception):
    pass

class EmptyName(Exception):
    pass

class RoomCapacityNotInt(Exception):
    pass

class RoomCapacityZero(Exception):
    pass

class DailyValueNotFloat(Exception):
    pass

class RoomDailyValueZero(Exception):
    pass

class FreeNotBool(Exception):
    pass

def cadastrarQuarto(number: int,name: str,capacity: int,daily_value: float,free: bool) -> None:
    # Verificações number
    if not isinstance(number, int):
        raise RoomNumberNotInt("Número do quarto não é inteiro")
    if number == 0:
        raise RoomNumberZero("Número do quarto não pode ser Zero")

    # Verificações name
    if not isinstance(name, str):
        raise NameNotStr("O nome do quarto não é Str")
    if name == '':
        raise EmptyName("O nome não pode ser vazio")

    # Verificações capacity
    if not isinstance(capacity, int):
        raise RoomCapacityNotInt("A capacidade do quarto não é inteiro")
    if capacity == 0:
        raise RoomCapacityZero("A capacidade do quarto não pode ser Zero")

    # Verificações daily_value
    if not isinstance(daily_value, float):
        raise DailyValueNotFloat("O valor do quarto não é float")
    if capacity == 0.0:
        raise RoomDailyValueZero("O valor do quarto não pode ser Zero")

    # Verificações free
    if not isinstance(free, bool):
        raise FreeNotBool("Livre não é um boleano")

    # Fazer o cadastro do quarto
    with open("./database/roomsDatabase/roomsDatabase.csv", "a", newline='', encoding='utf-8') as database:
        write = writer(database)
        write.writerow([number, name, capacity, daily_value, free])