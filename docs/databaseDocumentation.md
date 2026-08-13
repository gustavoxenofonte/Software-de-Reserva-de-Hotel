# Documentação dos Bancos de dados
 
 <br>

## Banco de dados dos quartos
- Colunas: `number`, `name` , `capacity`, `daily_value`, `free`
### Funcionalidades
- `alterarStatusQuarto(number: int, free: bool) -> None`
    - Altera o status do quarto se está livre (free = True) ou está ocupado (free = False)
- `cadastrarQuarto(number: int,name: str,capacity: int,daily_value: float,free: bool) -> None`
    - Cadastra um novo quarto
- `excluirQuarto(number: int)`
    - Exclui um quarto específico
- `listarQuartos() -> list`
    - Retorna uma lista de dicionários correspondente aos quartos, em que as informações estão como esse exemplo: `linha['number'] = numero_do_quarto`

<br>

## Banco de dados das Reservas
- Colunas:  `room_number`, `guest_cpf`, `checkin_date`, `checkout_date`, `total_value`, `status`

### Funcionalidades
- `cadastrarReserva(room_number: int, guest_cpf_: str, checkin_date: date, checkout_date: date, total_value: float, status: str) -> None`
    - Deverá ser usado a biblioteca datetime pra criar os tipos date
    - Status deve ser uma dessas opções: (reservada, hospedado, finalizada, cancelada)
- `listarReservas() -> list`
    - Retorna uma lista de dicionários correspondente às reservas, em que as informações estão como esse exemplo: `linha['room_number'] = numero_do_quarto`
- `check_in(guest_cpf: str) -> None`
    - Irá fazer o checkin do cliente, atualizará o status free do quarto para False, e da reserva para hospedado
- `check_out(guest_cpf: str) -> float`
    - Irá retornar o valor total da hospedagem
    - Irá remover o hospede do banco de dados, atualizará o status free do quarto para True e a reserva para finalizada.
- `cancelar_reserva(guest_cpf: str) -> None`
    - Irá remover o hospede do banco de dados, e atualizar a reserva para cancelada.

<br>

## Banco de dados dos Hóspedes
- Colunas: `cpf`, `name`, `phone_number`, `age`