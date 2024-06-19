import random

def embaralhar_palavras(frase):
    palavras = frase.split()
    nova = []

    for palavra in palavras:
        if len(palavra) > 2:
            primeira = palavra[0]
            ultima = palavra[-1]
            internas = list(palavra[1:-1])
            random.shuffle(internas)
            palavra_embaralhada = primeira + ''.join(internas) + ultima
        else:
            palavra_embaralhada = palavra

        nova.append(palavra_embaralhada)

    frase_embaralhada = ' '.join(nova)
    return frase_embaralhada

# frase = "Python é uma linguagem de programação"
# nova = embaralhar_palavras(frase)
# print(nova)

frase = input("Digite uma frase: ")
nova = embaralhar_palavras(frase)
print(nova)