<h1 align="center">Software de Reserva de Hotel</h1>
<p align="center">O projeto consiste no desenvolvimento de um software básico para cadastro de hóspedes de um hotel.</p>

<br>

<center>
<a href="https://github.com/gustavoxenofonte/Software-de-Reserva-de-Hotel/graphs/contributors?from=16%2F05%2F2026"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/gustavoxenofonte/Software-de-Reserva-de-Hotel?style=for-the-badge"></a>
<a href="https://www.python.org/downloads/"><img alt="GitHub top language" src="https://img.shields.io/github/languages/top/gustavoxenofonte/Software-de-Reserva-de-Hotel?style=for-the-badge"></a>
<a href="https://github.com/gustavoxenofonte/Software-de-Reserva-de-Hotel/commits/main/"><img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/t/gustavoxenofonte/Software-de-Reserva-de-Hotel?style=for-the-badge"></a>
<a href="https://githubtree.mgks.dev/repo/gustavoxenofonte/Software-de-Reserva-de-Hotel/main/"><img src="https://img.shields.io/badge/Structure-GitHubTree-blue?style=for-the-badge" alt="GitHubTree Structure"></a>
</center>

<br>

## Sumário
- [Descrição do Projeto](#descrição-do-projeto)
- [Problema que o projeto busca resolver](#problema-que-o-projeto-busca-resolver)
- [Instruções de Execução](#instruções-de-execução)
- [Exemplos de uso](#exemplos-de-uso)
- [Arquitetura de arquivos](#arquitetura-de-arquivos)
- [Divisão de tarefas](#divisão-de-tarefas)

<br>

## Descrição do projeto
- O projeto consiste no desenvolvimento de um software básico voltado à organização e ao gerenciamento das informações relacionadas aos hóspedes de um hotel. 

- A proposta busca proporcionar uma forma simples e eficiente de centralizar esses dados, contribuindo para que as informações dos hóspedes sejam mantidas de maneira organizada e de fácil acesso. 

- Dessa forma, o sistema tem como propósito auxiliar na rotina administrativa do estabelecimento, tornando o gerenciamento das hospedagens mais prático e reduzindo possíveis dificuldades relacionadas à organização e ao controle das informações.

<br>

## Problema que o projeto busca resolver
- A administração de um hotel envolve o gerenciamento de diversas informações relacionadas aos hóspedes e às suas respectivas hospedagens. Quando esses dados são armazenados de maneira desorganizada ou por meio de métodos manuais, podem ocorrer dificuldades para localizar informações, manter os registros atualizados e garantir um controle adequado das hospedagens. 

- Além disso, a falta de organização pode aumentar a ocorrência de erros e tornar o atendimento aos hóspedes mais demorado.

- Diante disso, o projeto busca solucionar o problema da desorganização e da dificuldade no gerenciamento das informações dos hóspedes, proporcionando uma forma mais estruturada de armazenar e controlar esses dados. Com isso, pretende-se contribuir para uma administração mais organizada e eficiente das informações utilizadas na rotina do hotel.

<br>

## Instruções de Execução

### Pré-requisitos

Para executar o sistema, é necessário ter o [`Python 3`](https://www.python.org/downloads/) instalado no computador. O projeto não utiliza bibliotecas externas, sendo desenvolvido apenas com recursos nativos da linguagem Python.

### 1. Clonar o repositório

Primeiramente, clone o repositório do projeto:

```bash
git clone https://github.com/gustavoxenofonte/Software-de-Reserva-de-Hotel.git
```

Em seguida, acesse a pasta do projeto:

```bash
cd Software-de-Reserva-de-Hotel
```

### 2. Executar o sistema

Após acessar a pasta do projeto, execute o arquivo principal utilizando o Python:

```bash
python main.py
```

Caso o sistema utilize o comando `python3` no seu ambiente, utilize:

```bash
python3 main.py
```

### 3. Utilização do sistema

Após a execução, o sistema será iniciado no terminal e apresentará as opções disponíveis para o usuário.

As informações cadastradas durante a utilização do sistema serão armazenadas nos arquivos `.csv`, permitindo que os dados permaneçam disponíveis mesmo após o encerramento do programa.


### Observações

* Não é necessário instalar bibliotecas externas para executar o projeto.
* Os arquivos `.csv` fazem parte do funcionamento do sistema e devem ser mantidos.
* Recomenda-se realizar uma cópia dos arquivos `.csv` antes de alterações manuais ou testes que possam modificar os dados.
* O sistema deve ser executado a partir do diretório principal do projeto, onde se encontra o arquivo `main.py`.

<br>

## Exemplos de uso
- Ao utilizar pela primeira vez o sistema, o usuário irá ser recebido com a seguinte mensagem:
```
== TELA DE CRIAÇÃO DE USUÁRIO ==
Não existe nenhum cadastro de login administrativo, deseja criar um? (S/N)
```

- Respondendo com `S`, o sistema pedirá um usuário e senha para ser gravado como o login administrativo:
```
== TELA DE LOGIN ==
Usuário: Admin
Senha: 123456
```
- Nesse caso, irá ficar salvo o usuário `Admin` com a senha `123456` e após o colocar o login novamente, o usuário será direcionado para o menu principal do projeto:
```
== HOTEL - MENU PRINCIPAL ==
0. Sair
1. Cadastrar quartos
2. Excluir quartos
3. Listar quartos
4. Cadastrar hóspedes (check-in)
5. Listar hóspedes
6. Reservar quartos
7. Check-out
8. Consultar reservas
9. Relatório de faturamento
10. Histórico de hospedagens
11. Configuração de login administrativo
Escolha uma opção:
```
- No menu o usuário pode escolher uma das opções e utilizar o software da maneira que mais preferir

<br>

## Arquitetura de arquivos
```
├── database/
│   ├── adminDatabase/
│   │   ├── __init__.py
│   │   ├── adminExiste.py
│   │   ├── alterarSenha.py
│   │   ├── alterarUserName.py
│   │   └── cadastrarLoginAdministrativo.py
│   ├── guestDatabase/
│   │   ├── __init__.py
│   │   ├── cadastrarHospede.py
│   │   ├── excluirHospede.py
│   │   ├── hospedeExiste.py
│   │   └── listarHospedes.py
│   ├── reservationDatabase/
│   │   ├── __init__.py
│   │   ├── cadastrarReserva.py
│   │   ├── cancelarReserva.py
│   │   ├── checkIn.py
│   │   ├── checkOut.py
│   │   ├── listarReservas.py
│   │   └── reservaExiste.py
│   └── roomsDatabase/
│       ├── __init__.py
│       ├── alterarStatusQuarto.py
│       ├── cadastrarQuarto.py
│       ├── excluirQuarto.py
│       ├── listarQuartos.py
│       └── quartoExiste.py
├── docs/
│   ├── databaseDocumentation.md
│   └── generalDocumentation.md
├── login/
│   ├── configAdm.py
│   ├── loginAdm.py
│   └── menuConfigAdm.py
├── reserva/
│   ├── cadastroReservas.py
│   ├── excluirReservas.py
│   └── exibirReservas.py
├── .gitignore
├── cadastro_quartos.py
├── cadastro.py
├── check_out.py
├── close.py
├── excluir_hospede.py
├── excluir_quartos.py
├── exibir_quartos.py
├── lista_hospede.py
├── main.py
├── pesquisar_hospede.py
└── README.md
```

<br>

## Divisão de tarefas
| Desenvolverdor <div style="width: 350px;"> | Responsabilidade |
| --- | --- |
| [**Guilherme Felipe Rodrigues Mariano**](https://github.com/guilhermefrmdev) | Banco de Dados |
| [**Gustavo Gonçalves Xenofonte**](https://github.com/gustavoxenofonte) | Inteface na linha de comando |
|[**Robson Arthur Matias Marques**](https://github.com/robson-arthur)|Implementar as Reservas|
|[**Stênio Vinícius de Souza Cruz**](https://github.com/stenio-vinicius)|Implementar o Cadastro de Quartos|
|[**Crisares Ferreira da Fonseca Filho**](https://github.com/Crisares92)|Implementar o Cadastro de Hóspedes|