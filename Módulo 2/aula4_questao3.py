nome1 = input("Digite o nome do produto 1: ")
preco1 = float(input("Digite o preço do produto 1: "))
quantidade1 = int(input("Digite a quatidade do produto 1: "))

nome2 = input("\nDigite o nome do produto 2: ")
preco2 = float(input("Digite o preço do produto 2: "))
quantidade2 = int(input("Digite a quatidade do produto 2: "))

nome3 = input("\nDigite o nome do produto 3: ")
preco3 = float(input("Digite o preço do produto 3: "))
quantidade3 = int(input("Digite a quatidade do produto 3: "))

total1 = preco1 * quantidade1
total2 = preco2 * quantidade2
total3 = preco3 * quantidade3

total_compra = total1 + total2 + total3
print(f"\nTotal: R${total_compra:,.2f}")