# Arquivo principal do projeto
# Responsável: Gustavo Gonçalves Xenofonte
# Tela de login, menu principal, tela de configurações do login e integra as outras funções do projeto

# Observações para a equipe - Commit inicial
# OBS 1: As funções login() e configuracao_login() irei fazer quando o banco de dados estiver funcionando  
# OBS 2: Vou integrando as funções no ifs da função menu_principal() conforme elas forem sendo feitas

from login.loginAdm import *
from login.configAdm import *
from reserva.cadastroReservas import *
from reserva.exibirReservas import *
from check_out import *


def menu_principal():

    while True:
        print("== HOTEL - MENU PRINCIPAL ==")
        print("1. Cadastrar quartos")
        print("2. Listar quartos")
        print("3. Cadastrar hóspedes (check-in)")
        print("4. Listar hóspedes")
        print("5. Reservar quartos")
        print("6. Check-out")
        print("7. Consultar reservas")
        print("8. Relatório de faturamento")
        print("9. Histórico de hospedagens")
        print("10. Configuração de login administrativo")

        while True:
            opcao = input("Escolha uma opção: ")

            if opcao.isdigit():
                opcao = float(opcao)
                if opcao % 1 == 0 and ( opcao > 0 and opcao < 11 ) :
                    break

            print("Opção inválida, tente novamente!")

        if opcao == 1:
            pass

        elif opcao == 2:
            pass

        elif opcao == 3:
            pass

        elif opcao == 4:
            pass

        elif opcao == 5:
            cadastroReserva()

        elif opcao == 6:
            check_out()

        elif opcao == 7:
            exibirReservas()

        elif opcao == 8:
            pass

        elif opcao == 9:
            pass

        elif opcao == 10:
            print("Por questões de segurança, insira o login novamente")
            if login_adm():
                print("== Configuração Login Administrativo ==")
                print("1. Alterar nome de usuário")
                print("2. Alterar senha")

                while True:
                    opcao_adm = input("Escolha uma opção: ")

                    if opcao_adm.isdigit():
                        opcao_adm = float(opcao_adm)
                        if opcao_adm % 1 == 0 and opcao_adm > 0 and opcao_adm < 3:
                            break
                        
                    else:
                        print("Opção inválida, tente novamente")

                if opcao_adm == 1:
                    alterarUserName(menuAlterarUsername())



        while True:    
            continuar = input("Deseja continuar? (S/N): ")
            if continuar.isalpha():
                if continuar.upper() != "S" and continuar.upper() != "N":
                    print("Opção inválida, tente novamente!")
                else:
                    break

        if continuar.upper() == "N":
            raise SystemExit
    
if login_adm():
    menu_principal()
