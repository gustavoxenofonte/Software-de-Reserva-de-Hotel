

def exibirReservas():
    print("Exibindo reservas...")
    reservas = listarReservas()
    print("="*20)
    print("NO. CPF        CHEK-IN         CHECK-OUT         VALOR             STATUS")
    for i in reservas:
        print(f"{reservas[i]['room_number']:<4} {reservas[i]['guest_cpf']:<13} {reservas[i]['checkin_date']:<11} {reservas[i]['checkout_date']:<11} {reservas[i]['total_value']:<4} {reservas[i]['status']:<10}")
    print("="*20)
exibirReservas()