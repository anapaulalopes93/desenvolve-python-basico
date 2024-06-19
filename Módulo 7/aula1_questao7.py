import random

def encrypt(nomes):
    chave = random.randint(1, 10)
    criptografados = []

    for nome in nomes:
        criptografado = ""

        for letra in nome:
            codigo = ord(letra)
            if 33 <= codigo <= 126:
                novo_codigo = codigo + chave
                if novo_codigo > 126:
                    novo_codigo = 33 + (novo_codigo - 127)

                criptografado += chr(novo_codigo)
            else:
                criptografado += letra

        criptografados.append(criptografado)

    return criptografados, chave

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
criptografados, chave = encrypt(nomes)

print(f"Chave de criptografia: {chave}")
print(f"Nomes criptografados: {criptografados}")