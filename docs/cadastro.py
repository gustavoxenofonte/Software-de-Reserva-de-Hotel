while True:
  try:
    cpf = input('CPF: ')
    if len(cpf) != 11 or not cpf.isdigit():
      print('CPF inválido')
      continue


    soma = 0
    multiplicador = 10
    for digito in cpf[:9]:
      numero = int(digito) * multiplicador
      multiplicador -= 1
      soma += numero
    resto = soma % 11
    if resto == 0 or resto == 1:
      verificador1 = 0
    else:
      verificador1 = 11 - resto


    soma = 0
    multiplicador = 11
    for digito in cpf[:10]:
      numero = int(digito) * multiplicador
      multiplicador -= 1
      soma += numero
    resto = soma % 11
    if resto == 0 or resto == 1:
      verificador2 = 0
    else:
      verificador2 = 11 - resto
    
    verificador = [verificador1, verificador2]
    verificador_o = [int(cpf[-2]), int(cpf[-1])]
    if verificador == verificador_o:
      break
    else:
      print('CPF inválido')
  except ValueError:
        print('CPF inválido') 