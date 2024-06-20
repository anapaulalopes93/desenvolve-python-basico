comprimento = int(input("Digite o comprimento do terreno: "))
largura = int(input("Digite a largura do terreno: "))
metro_quadrado = float(input("Digite o valor do metro quadrado da região: "))

area = comprimento * largura
preco = metro_quadrado * area
print(f"O terreno possui {area}m2 e custa R${preco:,.2f}")