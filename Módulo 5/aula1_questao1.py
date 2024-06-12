num1 = float(input("Digite um número decimal: "))
num2 = float(input("Digite um segundo número decimal: "))

diferenca = abs(num1 - num2)
arredondado = round(diferenca, 2)
print(f"A diferença absoluta entre os números é: {arredondado}")