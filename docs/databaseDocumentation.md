# Documentação dos Bancos de dados
 
 <br>

## Como importar os bancos de dados
- Importando a partir da main
 - `import database.<nomeDoBancoDeDados>`
- Se importar a partir de uma pasta ou outro diretório e ocorrer o erro: `ImportError: attempted relative import with no known parent package`
  - Utilize o seguinte código antes da importação:
```
import os
import sys

caminho_absoluto = os.path.abspath(os.curdir)
sys.path.insert(0, caminho_absoluto)
```

- Se houver dúvidas sobre essa importação relativa, veja o vídeo: https://youtu.be/spXh5vDKaZU

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
- `quartoExiste(room_number: int) -> bool`
    - Retorna se o quarto com o número `room_number` existe
    - `True` = existe; `False` = não existe

<br>

## Banco de dados das Reservas
- Colunas:  `room_number`, `guest_cpf`, `checkin_date`, `checkout_date`, `total_value`, `status`

### Funcionalidades
- `cadastrarReserva(room_number: int, guest_cpf_: str, checkin_date: date, checkout_date: date, total_value: float, status: str="reservado") -> None`
    - Deverá ser usado a biblioteca datetime pra criar os tipos date
    - `status` deve ser uma dessas opções: (reservado, hospedado, finalizado, cancelado)
    - Se não passar o parâmetro status, será definido reservado automaticamente
- `listarReservas() -> list`
    - Retorna uma lista de dicionários correspondente às reservas, em que as informações estão como esse exemplo: `[{'room_number': '10', 'guest_cpf': '00011122233'}]`
- `checkIn(guest_cpf: str) -> None`
    - Irá fazer o checkin do cliente, atualizará o status free do quarto para False, e da reserva para hospedado
- `checkOut(guest_cpf: str) -> float`
    - Irá retornar o valor total da hospedagem
    - Irá remover o hospede do banco de dados, atualizará o status free do quarto para True e a reserva para finalizada.
- `cancelarReserva(guest_cpf: str) -> None`
    - Irá remover o hospede do banco de dados, e atualizar a reserva para cancelada.
- `reservaExiste(guest_cpf: str) -> bool`
    - Retorna se a reserva do cpf `guest_cpf` existe
    - `True` = existe; `False` = não existe

<br>

## Banco de dados dos Hóspedes
- Colunas: `cpf`, `name`, `phone_number`, `age`

### Funcionalidades
- `cadastrarHospede(guest_cpf: str, name: str, phone_number: str, age: int) -> None`
    - Utilizado para cadastrar hóspedes no banco de dados
    - `guest_cpf` deve ser no padrão: `00011122233` sem caracteres especiais
    - `phone_number` deve ser no padrão: `88988887777` sem caracteres especiais
- `excluirHospede(guest_cpf: str) -> None`
    - Utilizado para excluir o cadastro de um hóspede do banco de dados
    - `guest_cpf` deve ser no padrão: `00011122233` sem caracteres especiais
- `hospedeExiste(guest_cpf: str) -> bool` 
    - Retorna se o hospede com o cpf `guest_cpf` existe
    - `True` = existe; `False` = não existe

<br>

## Banco de dados Login Administrativo
- Colunas: `user_name`, `password`

### Funcionalidades
- `cadastrarLoginAdministrativo(user_name: str, password: str) -> None`
    - Irá fazer o cadastro de login
    - `user_name` deverá ser somente caracteres sem espaços
    - `password` deverá ser somente caracteres sem espaços
- `alterarUserName(new_user_name: str) -> None`
    - Irá mudar o nome de usuário
    - `new_user_name` deverá ser somente caracteres sem espaços
- `alterarSenha(new_password: str) -> None`
    - Irá mudar a senha
    - `new_password` deverá ser somente caracteres sem espaços
