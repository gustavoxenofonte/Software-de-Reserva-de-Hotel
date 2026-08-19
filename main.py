# Arquivo principal do projeto

from login.loginAdm import *
from login.configAdm import *
from login.menuConfigAdm import *
from reserva.cadastroReservas import *
from reserva.exibirReservas import *
from reserva.excluirReservas import *
from database.guestDatabase import *
from check_out import *
from excluir_quartos import *
from exibir_quartos import *
from cadastro_quartos import *
from cadastro import *
from pesquisar_hospede import *
from time import sleep
from close import *

def menu_principal():

    while True:
        print("== HOTEL - MENU PRINCIPAL ==")
        print("0. Sair")
        print("1. Cadastrar quartos")
        print("2. Excluir quartos")
        print("3. Listar quartos")
        print("4. Cadastrar hóspedes")
        print("5. Consultar hóspedes")
        print("6. Reservar quartos")
        print("7. Check-out")
        print("8. Consultar reservas")
        print("9. Cancelar reserva")
        print("10. Configuração de login administrativo")

        while True:
            opcao = input("Escolha uma opção: ")

            # Valida se é número inteiro entre 1 e 10 antes de aceitar a opção
            if opcao.isdigit():
                opcao = float(opcao)
                if opcao % 1 == 0 and ( opcao >= 0 and opcao <= 10 ) :
                    break

            print("Opção inválida, tente novamente!")

        cls()

        if opcao == 0:
            raise SystemExit

        elif opcao == 1:
            cadastro_quartos()

        elif opcao == 2:
            excluir_quartos()

        elif opcao == 3:
            exibir_quartos()

        elif opcao == 4:
            cadastro_hospede()

        elif opcao == 5:
            consultar_hospede()

        elif opcao == 6:
            cadastroReserva()

        elif opcao == 7:
            check_out()

        elif opcao == 8:
            exibirReservas()

        elif opcao == 9:
            excluirReservas() 

        elif opcao == 10:
            menuConfigAdm() 

        input("Pressione enter para continuar... ")
        print("Limpando a tela...")
        sleep(1.5)
        cls()


# Exige login antes de liberar acesso ao menu principal
if login_adm():
    cls()
    menu_principal()
