from collections import Counter
def anagrama(palavra1, palavra2):
    return Counter(palavra1.lower()) == Counter(palavra2.lower())

def encontra_anagramas(frase, objetivo):
    anagramas = []
    palavras = frase.split()

    for palavra in palavras:
        if anagrama(palavra, objetivo):
            anagramas.append(palavra)

    return anagramas

frase = input("Digite uma frase: ")
objetivo = input("Digite a plavra objetivo: ")
anagramas = encontra_anagramas(frase, objetivo)
print(f"Anagramas: {anagramas}")