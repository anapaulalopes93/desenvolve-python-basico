import random

lista = [random.randint(-10, 10) for i in range(20)]
print(f"Original: {lista}")

intervalo = []
cont = 0
for i in lista:
    if(i < 0):
        cont += 1
    else:
        if cont > len(intervalo):
            intervalo = lista[lista.index(i) - cont: lista.index(i)]
        cont = 0

for i in intervalo:
    lista.remove(i)

print(f"Editada: {lista}")