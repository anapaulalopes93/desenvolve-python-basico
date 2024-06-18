quantidade1 = int(input("Digite a quantidade de elementos da lista 1: "))
print(f"Digite os {quantidade1} elementos da lista 1: ")

lista1 = []
for i in range(quantidade1):
    elemento = int(input())
    lista1.append(elemento)

quantidade2 = int(input("Digite a quantidade de elementos da lista 2: "))
print(f"Digite os {quantidade2} elementos da lista 2: ")

lista2 = []
for i in range(quantidade2):
    elemento = int(input())
    lista2.append(elemento)

lista3 = []
for i in range(max(quantidade1, quantidade2)):
    if(i < quantidade1):
        lista3.append(lista1[i])
    if(i < quantidade2):
        lista3.append(lista2[i])

# print(lista1)
# print(lista2)
print(f"Lista intercalada: {lista3}")