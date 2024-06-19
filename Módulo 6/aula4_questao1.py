pares = [num for num in range(20, 51, 2)]
print(f"Todos os números pares entre 20 e 50: {pares}")

quadrados = [num ** 2 for num in [1, 2, 3, 4, 5, 6, 7, 8, 9]]
print(f"Os quadrados de todos os valores da lista [1, 2, 3, 4, 5, 6, 7, 8, 9]: {quadrados}")

divisivel = [num for num in range(1, 101) if num % 7 == 0]
print(f"Todos os números entre 1 e 100 divisíveis por 7: {divisivel}")

par_impar = ["Par" if num % 2 == 0 else "Ímpar" for num in range(0, 30, 3)]
print(f"Para todos os valores em range (0, 30, 3): {par_impar}")