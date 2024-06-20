import emoji

def lista():
    emojis = {':red_heart:': '❤️',
        ':thumbs_up:': '👍',
        ':thinking_face:': '🤔',
        ':partying_face:': '🥳'}

    print("Emojis disponíveis:")
    for chave, valor in emojis.items():
        print(f"{valor} - {chave}")

def emojizar(frase):
    emojizada = emoji.emojize(frase)
    return emojizada

lista()
frase = input("Digite uma frase e ela será emojizada: ")
emojizada = emojizar(frase)
print(f"Frase emojizada:\n{emojizada}")
