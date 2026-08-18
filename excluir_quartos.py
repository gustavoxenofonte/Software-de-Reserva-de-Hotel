from database.roomsDatabase import excluirQuarto
from database.roomsDatabase import quartoExiste

def excluir_quartos():

    vermelho = "\033[91m"   #COR PARA MENSAGENS DE ERRO
    verde = "\033[92m"      #COR PARA MENSAGENS DE SUCESSO
    reset = "\033[0m"       #VOLTA PARA A COR NORMAL

    print("\n--- EXCLUIR QUARTO ---")

    # Pede o número do quarto, com validação de erro
    while True:
        try:
            numero = int(input("Digite o número do quarto que deseja excluir: "))
            if numero <= 0:
                print(f"{vermelho}ERRO! Número de quarto inválido!{reset}")
                continue
            break
        except ValueError:
            print(f"{vermelho}ERRO! Digite um número válido!{reset}")

    #Verificação da existência do quarto pelo respectivo número
    if not quartoExiste(numero):
        print(f"{vermelho}ERRO! Quarto {numero} não encontrado no banco de dados. {reset}")
        return

    # Confirmação antes de excluir (evita exclusão acidental)
    while True:
        print(f"Tem certeza que deseja excluir o quarto {numero}?")
        print("1. SIM")
        print("2. NÃO")
        try:
            opcao = int(input("Digite o número correspondente a opção desejada: "))
        except ValueError:
            print(f"{vermelho}ERRO! OPÇÃO INVÁLIDA!{reset}")
            continue

        if opcao == 1:
            excluirQuarto(numero)
            print(f"{verde}QUARTO {numero} EXCLUÍDO COM SUCESSO!{reset}")
            break

        elif opcao == 2:
            print("Operação cancelada.")
            break

        else:
            print(f"{vermelho}ERRO! OPÇÃO INVÁLIDA!{reset}")