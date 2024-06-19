def validar(cpf):
    cpf = cpf.replace(".", "").replace("-", "")
    if len(cpf) != 11:
        return False
    
    digitos = [int(cpf[i]) for i in range(9)]

    soma = 0
    multiplicador = 10
    for digito in digitos:
        soma += digito * multiplicador
        multiplicador -= 1

    resto = soma % 11
    if resto < 2:
        primeiro = 0
    else:
        primeiro = 11 - resto
    digitos.append(primeiro)

    soma = 0
    multiplicador = 11
    for digito in digitos:
        soma += digito * multiplicador
        multiplicador -= 1

    resto = soma % 11
    if resto < 2:
        segundo = 0
    else:
        segundo = 11 - resto
    digitos.append(segundo)

    pos_calculo = "".join(map(str, digitos))
    if cpf == pos_calculo:
        return "Válido"
    else:
        return "Inválido"
    
''' cpfs = ["545.315.761-52", "473.063.662-70", "775.682.566-77", "545.315.761-12", "473.063.662-98", "775.682.566-13"]

for cpf in cpfs:
    if validar(cpf):
        print(f"{cpf}: Válido")
    else:
        print(f"{cpf}: Inválido") '''

cpf = input("Digite um CPF na forma XXX.XXX.XXX-XX: ")
teste = validar(cpf)
print(f"{teste}")