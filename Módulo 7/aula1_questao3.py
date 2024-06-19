def espacos(frase):
    contador = 0
    for i in frase:
        if i == ' ':
            contador += 1

    return contador

frase = input("Digite uma frase: ")
espacos_branco = espacos(frase)
print(f"Esoaços em branco: {espacos_branco}")