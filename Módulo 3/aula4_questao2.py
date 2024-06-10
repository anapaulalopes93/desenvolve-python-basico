nota = int(input("Digite a sua classificação para o filme de '1' a '5', onde '1' é Ruim e '5' é Excelente: "))

if(nota == 1):
    print("Ruim.")
elif(nota == 2):
    print("Regular.")
elif(nota == 3):
    print("Bom.")
elif(nota == 4):
    print("Muito Bom!")
elif(nota == 5):
    print("Excelente!")
else:
    print("Nota inválida.")