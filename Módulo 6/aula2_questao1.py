import random

valores = [random.randint(-100, 100) for i in range(20)]

ordenada = sorted(valores[:])
maior = valores.index(max(valores))
menor = valores.index(min(valores))

print(f"Lista ordenada: {ordenada}")
print(f"Lista original: {valores}")
print(f"Índice do maior valor da lista: {maior}")
print(f"Índice do menor valor da lista: {menor}")