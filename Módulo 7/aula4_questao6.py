import csv

def linha_valida(linha):
    if len(linha) != 10:
        return False
    
    if '"' in linha[1]:
        return False
    
    return True

def processar_arquivo(arquivo):
    musicas_ano = {}
    
    with open(arquivo, "r", encoding = "latin-1") as csvfile:
        reader = csv.reader(csvfile)

        next(reader)

        for linha in reader:
            if linha_valida(linha):
                track_name = linha[0]
                artist_name = linha[1]
                released_year = int(linha[3])
                streams = int(linha[8])

                if released_year >= 2012 and released_year <= 2022:
                    if released_year not in musicas_ano:
                        musicas_ano[released_year] = [track_name, artist_name, released_year, streams]
                    else:
                        if streams > musicas_ano[released_year][3]:
                            musicas_ano[released_year] = [track_name, artist_name, released_year, streams]

    musicas = [musicas_ano[ano] for ano in sorted(musicas_ano)]
    return musicas

arquivo = "spotify-2023.csv"
mais_tocadas = processar_arquivo(arquivo)
print(mais_tocadas)