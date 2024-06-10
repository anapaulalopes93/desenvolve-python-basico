n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

m = (n1 + n2 + n3) / 3
print(f"{m:.2f}")

if(m >= 60):
    print("Aprovado")
elif(m >= 40):
    print("Recuperação")
else:
    print("Reprovado")
print("Fim")