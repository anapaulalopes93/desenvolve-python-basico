import math
import random

n = int(input("Informe um número: "))
soma = 0

for i in range(n):
    valores = random.randint(0,100)
    print(f"{valores}", end = " ")
    soma += valores

raiz_quadrada = math.sqrt(soma)

print("\n")
print(f"Soma dos valores gerados: {soma:.2f}")
print(f"Raiz quadrada da soma: {raiz_quadrada}")