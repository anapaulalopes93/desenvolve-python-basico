print(" ---- Clube Juvenil de Jogos de Tabuleiro ----")
idade = int(input("Qual a sua idade? "))
jogos = input("Responda com 'True' se já tiver jogado pelo menos 3 jogos de tabuleiro ou responda com 'False' caso contrário: ")
venceu = int(input("Quantas vezes venceu um jogo? "))

if(idade >= 16 and idade <= 18 and jogos == 'True' and venceu >= 1):
    print("Apto para ingressar no Clube Juvenil de Jogos de Tabuleiro: True")
else:
    print("Apto para ingressar no Clube Juvenil de Jogos de Tabuleiro: False")