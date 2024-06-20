import os
import re

caminho = os.path.join(os.getcwd(), "frase.txt")
with open(caminho, 'r') as arquivo:
    conteudo = arquivo.read().strip()

lido = re.sub(r'[^a-zA-Z\s]', '', conteudo)
palavras = lido.split()

caminho_palavras = os.path.join(os.getcwd(), "palavras.txt")
with open(caminho_palavras, 'w') as arquivo_palavras:
    for palavra in palavras:
        arquivo_palavras.write(palavra + '\n')

with open(caminho_palavras, 'r') as arquivo_palavras:
    conteudo_palavras = arquivo_palavras.read()
    print(conteudo_palavras)