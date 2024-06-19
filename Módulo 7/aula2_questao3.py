import string

def limpeza(frase):
    frase = frase.replace(" ", "").lower()
    frase = frase.translate(str.maketrans('', '', string.punctuation))
    return frase

def palindromo(frase):
    limpa = limpeza(frase)
    invertida = limpa[::-1]
    return limpa == invertida

while True:
    frase = input("Digite uma frase (para encerrrar o programa, digite 'fim'): ")
    if frase.lower() == "fim":
        print("Programa encerrado.")
        break

    if palindromo(frase):
        print(f"'{frase}' é um palíndromo.")
    else:
        print(f"'{frase}' não é um palíndromo.")
