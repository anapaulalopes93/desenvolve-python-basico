classe = input("Escolha a classe (guerreiro, mago ou arqueiro): ")
forca = int(input("Digite os pontos de força (de 1 a 20): "))
magia = int(input("Digite os pontos de magia (de 1 a 20): "))

if(classe == 'guerreiro'):
    if forca >= 15 and magia <= 10:
        print(True)
    else:
        print(False)
elif(classe == 'mago'):
    if forca <= 10 and magia >= 15:
        print(True)
    else:
        print(False)
elif(classe == 'arqueiro'):
    if 5 < forca < 15 and 5 < magia < 15:
        print(True)
    else:
        (print(False))

else:
    print("Classe não identificada.")