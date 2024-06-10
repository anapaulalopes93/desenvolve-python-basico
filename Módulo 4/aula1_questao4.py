n = int(input("Digite um número n: "))
maior = 0

while(n > 0):
    x = int(input("Digite um número x: "))
    if(x > maior):
        maior = x
    else:
        n -= 1
print(maior)