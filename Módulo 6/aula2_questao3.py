import random
from collections import Counter

lista1 = [random.randint(0, 50) for i in range(20)]
lista2 = [random.randint(0, 50) for i in range(20)]

interseccao = list(set(lista1) & set(lista2))
ordenada = sorted(interseccao[:])
cont_lista1 = Counter(lista1)
cont_lista2 = Counter(lista2)

print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Intersecção ordenada: {ordenada}")
print("Contagem:")
for i in interseccao:
    print(f"{i}: (Lista1 = {cont_lista1[i]}, Lista2 = {cont_lista2[i]})")
