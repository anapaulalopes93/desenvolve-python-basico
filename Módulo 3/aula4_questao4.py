distancia = float(input("Informe a distância da entrega em quilômetros: "))
peso = float(input("Informe o peso do pacote em kg: "))

if(distancia <= 100):
    valor = 1
elif(distancia > 100 and distancia <= 300):
    valor = 1.50
else:
    valor = 2

if(peso > 10):
    taxa = 10
else:
    taxa = 0

frete = (valor * peso) + taxa
print(f"O valor do frete é R${frete:.2f}")