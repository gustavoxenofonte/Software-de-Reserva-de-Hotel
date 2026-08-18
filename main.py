# Arquivo principal do projeto
# Responsável: Gustavo Gonçalves Xenofonte
# Tela de login, menu principal, tela de configurações do login e integra as outras funções do projeto

# Observações para a equipe - Commit inicial
# OBS 1: As funções login() e configuracao_login() irei fazer quando o banco de dados estiver funcionando  
# OBS 2: Vou integrando as funções no ifs da função menu_principal() conforme elas forem sendo feitas

from login.loginAdm import *
from login.configAdm import *
from login.menuConfigAdm import *
from reserva.cadastroReservas import *
from reserva.exibirReservas import *
from check_out import *
from excluir_quartos import *
from exibir_quartos import *
from cadastro_quartos import *

def menu_principal():

    while True:
        print("== HOTEL - MENU PRINCIPAL ==")
        print("0. Sair")
        print("1. Cadastrar quartos")
        print("2. Excluir quartos")
        print("3. Listar quartos")
        print("4. Cadastrar hóspedes (check-in)")
        print("5. Listar hóspedes")
        print("6. Reservar quartos")
        print("7. Check-out")
        print("8. Consultar reservas")
        print("9. Relatório de faturamento")
        print("10. Histórico de hospedagens")
        print("11. Configuração de login administrativo")

        while True:
            opcao = input("Escolha uma opção: ")

            # Valida se é número inteiro entre 1 e 10 antes de aceitar a opção
            if opcao.isdigit():
                opcao = float(opcao)
                if opcao % 1 == 0 and ( opcao >= 0 and opcao <= 11 ) :
                    break

            print("Opção inválida, tente novamente!")

        if opcao == 0:
            raise SystemExit

        elif opcao == 1:
            cadastro_quartos()

        elif opcao == 2:
            excluir_quartos()

        elif opcao == 3:
            exibir_quartos()

        elif opcao == 4:
            pass

        elif opcao == 5:
            pass

        elif opcao == 6:
            cadastroReserva()

        elif opcao == 7:
            check_out()

        elif opcao == 8:
            exibirReservas()

        elif opcao == 9:
            pass

        elif opcao == 10:
            pass

        elif opcao == 11:
            menuConfigAdm()

        # Pergunta se o usuário quer voltar ao menu ou encerrar o programa
        while True:    
            continuar = input("Deseja continuar? (S/N): ")
            if continuar.isalpha():
                if continuar.upper() != "S" and continuar.upper() != "N":
                    print("Opção inválida, tente novamente!")
                else:
                    break
    
        if continuar.upper() == "N":
            raise SystemExit

# Exige login antes de liberar acesso ao menu principal
if login_adm():
    menu_principal()
