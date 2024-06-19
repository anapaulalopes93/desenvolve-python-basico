def completar(numero):
    if len(numero) == 8:
        completo = "9" + numero
    elif len(numero) == 9:
        if numero[0] == "9":
            completo = numero[:5] + "-" + numero[5:]
        else:
            completo = numero[:5] + "-" + numero[5:]

    return completo

numero = input("Digite o número: ")
completo = completar(numero)

print(f"Número completo: {completo}")
