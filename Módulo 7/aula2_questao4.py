import re

def validador_senha(senha):
    if len(senha) < 8:
        return False
    
    maiuscula = False
    minuscula = False
    for letra in senha:
        if letra.isupper():
            maiuscula = True
        elif letra.islower():
            minuscula = True
        if maiuscula and minuscula:
            break

    if not(maiuscula and minuscula):
        return False
    
    numero = any(letra.isdigit() for letra in senha)
    if not numero:
        return False
    
    especiais = "!@#$%^&()-+"
    especial = any(letra in especiais for letra in senha)
    if not especial:
        return False
    
    return True

# EXEMPLOS
# senha1 = "Senha123@"
# senha2 = "senhafraca"
# senha3 = "Senha_fraca"
# print(validador_senha(senha1))
# print(validador_senha(senha2))
# print(validador_senha(senha3))

senha = input("Digite uma nova senha: ")
print(validador_senha(senha))

