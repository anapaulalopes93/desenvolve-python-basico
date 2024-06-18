import random

num_elementos = random.randint(5, 20)
print(num_elementos)

elementos = [random.randint(1, 10) for i in range(num_elementos)]
soma = sum(elementos)
media = soma / num_elementos

print(f"Lista elementos: {elementos}")
print(f"Soma dos valores da lista: {soma}")
print(f"Média dos valores da lista: {media:.2f}")