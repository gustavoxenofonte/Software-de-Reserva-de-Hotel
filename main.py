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
from lista_hospede import *

def menu_principal():

    while True:
        print("== HOTEL - MENU PRINCIPAL ==")
        print("0. Sair")
        print("1. Cadastrar quartos")
        print("2. Excluir quartos")
        print("3. Listar quartos")
        print("4. Cadastrar hóspedes")
        print("5. Consultar hóspedes")
        print("6. Listar hóspedes")
        print("7. Reservar quartos")
        print("8. Check-out")
        print("9. Consultar reservas")
        print("10. Cancelar reserva")
        print("11. Configuração de login administrativo")

        while True:
            opcao = input("Escolha uma opção: ")

            # Valida se é número inteiro entre 0 e 11 antes de aceitar a opção
            if opcao.isdigit():
                opcao = float(opcao)
                if opcao % 1 == 0 and ( opcao >= 0 and opcao <= 11 ) :
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
            lista_hospede()

        elif opcao == 7:
            cadastroReserva()

        elif opcao == 8:
            check_out()

        elif opcao == 9:
            exibirReservas()

        elif opcao == 10:
            excluirReservas() 

        elif opcao == 11:
            menuConfigAdm() 

        input("Pressione enter para continuar... ")
        print("Limpando a tela...")
        sleep(1.5)
        cls()


# Exige login antes de liberar acesso ao menu principal
if login_adm():
    cls()
    menu_principal()
