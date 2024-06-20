import random

def palavra():
    with open("gabarito_forca.txt", "r", encoding = "utf-8") as arquivo:
        palavras = arquivo.read().splitlines()
    return random.choice(palavras)

def carregar():
    with open("gabarito_enforcado.txt", "r", encoding = "utf-8") as arquivo:
        estagios_enforcado = arquivo.read().strip().split("\n\n")
    return estagios_enforcado

def enforcado(erros):
    estagios_enforcado = carregar()
    if erros >= 0 and erros < len(estagios_enforcado):
        print(estagios_enforcado[erros])
    else:
        print("Você perdeu!")

palavra_escolhida = palavra().strip().lower()
tamanho = len(palavra_escolhida)
letras_descobertas = ['_'] * tamanho
corretas = set()
incorretas = set()
tentativas = 6

print("JOGO DA FORCA")
print(f"A palavra tem {tamanho} letras.\n")
print(" ".join(letras_descobertas))

while True:
    letra = input("Digite uma letra: ").strip().lower()

    if len(letra) != 1 or not letra.isalpha():
        print("Digite uma letra válida.")
    
    if letra in corretas or letra in incorretas:
        print(f"Você já tentou essa letra: '{letra}'")
        continue

    if letra in palavra_escolhida:
        print(f"A letra '{letra}' está na palavra\n")
        for i, char in enumerate(palavra_escolhida):
            if char == letra:
                letras_descobertas[i] = letra
        corretas.add(letra)
    else:
        print(f"A letra '{letra}' não está na palavra\n")
        incorretas.add(letra)
        tentativas -= 1
        enforcado(6 - tentativas)

    print(" ".join(letras_descobertas))

    if "_" not in letras_descobertas:
        print("Parabéns! Você venceu!")
        break

    if tentativas == 0:
        print(f"Você perdeu!\nA palavra era '{palavra_escolhida}'")
        break

    print(f"Tentativas restantes: {tentativas}\n")