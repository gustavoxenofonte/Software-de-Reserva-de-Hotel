# Arquivo principal do projeto
# Responsável: Gustavo Gonçalves Xenofonte
# Tela de login, menu principal, tela de configurações do login e integra as outras funções do projeto

# Observações para a equipe - Commit inicial
# OBS 1: As funções login() e configuracao_login() irei fazer quando o banco de dados estiver funcionando  
# OBS 2: Vou integrando as funções no ifs da função menu_principal() conforme elas forem sendo feitas

def login(): 
    pass

def configuracao_login():
    pass

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

        while True:
            opcao = input("Escolha uma opção: ")

            if opcao.isdigit():
                opcao = float(opcao)
                if opcao % 1 == 0 and ( opcao > 0 and opcao < 10 ) :
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
            pass

        elif opcao == 6:
            pass

        elif opcao == 7:
            pass

        elif opcao == 8:
            pass

        elif opcao == 9:
            pass

        while True:    
            continuar = input("Deseja continuar? (S/N): ")
            if continuar.isalpha():
                if continuar.upper() != "S" and continuar.upper() != "N":
                    print("Opção inválida, tente novamente!")
                else:
                    break

        if continuar.upper() == "N":
            break
    










