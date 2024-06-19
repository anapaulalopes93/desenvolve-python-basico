lista = []
while (len(lista) < 4):
    numero = int(input("Digite um número inteiro: "))
    lista.append(numero)

print(f"Lista original: {lista}")
print(f"Os 3 primeiros elementos: {lista[:3]}")
print(f"Os 2 últimos elementos: {lista[-2:]}")
print(f"Lista invertida: {lista[::-1]}")
print(f"Elementos de índice par: {lista[::2]}")
print(f"Elementos de índice ímpar: {lista[1::2]}")