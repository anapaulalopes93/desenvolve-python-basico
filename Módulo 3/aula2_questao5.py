genero = input("Informe o seu gênero ('F' ou 'M'): ")
idade = int(input("Informe a sua idade: "))
servico = int(input("Informe o seu tempo de serviço: "))

if(genero == 'F'):
    aposentadoria = idade > 60 or servico >= 30 or idade >= 60 and servico >= 25
    print(f"Pode se aposentar? {aposentadoria}")
elif(genero == 'M'):
    aposentadoria = idade > 65 or servico >= 30 or idade >= 60 and servico >= 25
    print(f"Pode se aposentar? {aposentadoria}")