nome = "estomago.txt"

with open(nome, 'r') as arquivo:
    print("Primeiras 25 linhas do arquivo:\n")
    for i in range(25):
        linha = arquivo.readline().strip()
        print(linha)

    arquivo.seek(0)
    numero_linhas = sum(1 for i in arquivo)
    print(f"\nNúmero total de linhas do arquivo: {numero_linhas}\n")

    arquivo.seek(0)
    maior_caracteres = max(arquivo, key = len).strip()
    print(f"Linha com maior número de caracteres:\n'{maior_caracteres}'\n")

    arquivo.seek(0)
    conteudo = arquivo.read().lower()
    nonato = conteudo.count('nonato')
    iria = conteudo.count('íria')
    print(f"Menções aos nomes dos personagens")
    print(f"Nonato: {nonato} vezes")
    print(f"Íria: {iria} vezes")