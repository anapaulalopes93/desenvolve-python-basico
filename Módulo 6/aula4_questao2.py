frase = input("Digite uma frase: ")
vogais = 'aeiouAEIOU'

lista_vogais = [char for char in frase if char in vogais]
consoantes = [char for char in frase if char.isalpha() and char not in vogais]
lista_vogais.sort()

print(f"Vogais: {lista_vogais}")
print(f"Consoantes: {consoantes}")