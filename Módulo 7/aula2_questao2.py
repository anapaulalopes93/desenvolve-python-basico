def substituicao(frase):
    vogais = "aeiouAEIOU"
    modificada = ""
    
    for letra in frase:
        if letra in vogais:
            modificada += "*"
        else:
            modificada += letra

    return modificada

frase = input("Digite uma frase: ")
modificada = substituicao(frase)
print(f"Frase modificada: {modificada}")