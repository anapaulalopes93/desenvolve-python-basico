import os

frase = input("Digite uma frase: ")
diretorio_atual = os.getcwd()
caminho = os.path.join(diretorio_atual, "frase.txt")

with open(caminho, 'w') as arquivo:
    arquivo.write(frase)

print(f"Frase salva em {caminho}")