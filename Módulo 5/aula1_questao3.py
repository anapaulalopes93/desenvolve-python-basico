import random

numero_aleatorio = random.randint(1,10)

while(True):
    palpite = int(input("Adivinhe o número do dia (escolha entre 1 e 10): "))
    if(palpite == numero_aleatorio):
        print(f"Correto! O número é {numero_aleatorio}.")
        break
    elif(palpite > numero_aleatorio):
        print("Muito alto, tente novamente!")    
    else:
        print("Muito baixo, tente novamente!")