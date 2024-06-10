n = int(input("Digite a quantidade de respondentes: "))
cont = 0
soma = 0

while(cont < n):
    idade = int(input("Informe a idade do respondente: "))
    soma += idade
    cont += 1

media = soma / n
print(f"A média de idade dos respondentes é: {media:.2f}")