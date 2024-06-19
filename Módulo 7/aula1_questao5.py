def contar(frase):
    vogais = "aeiouAEIOU"
    indicev = []
    contador = 0

    for indice, letra in enumerate(frase):
        if letra in vogais:
            contador += 1
            indicev.append(indice)

    return contador, indicev

frase = input("Digite uma frase: ")
quant_vogais, indices = contar(frase)

#print(f"{frase}")
print(f"{quant_vogais} vogais")
print(f"Índices: {indices}")