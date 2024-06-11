quant_experimentos = int(input("Informe a quantidade de experimentos registrados: "))
contador = 0
total_sapos = 0
total_ratos = 0
total_coelhos = 0

while(contador < quant_experimentos):
    quantia = int(input("Informe a quantidade de cobaias utilizadas: "))
    tipo = input("Informe o tipo de cobaia utilizada; 'S' para sapos, 'R' para ratos ou 'C' para coelhos: ")

    if(tipo == 'S'):
        total_sapos += quantia
    elif(tipo == 'R'):
        total_ratos += quantia
    elif(tipo == 'C'):
        total_coelhos += quantia

    contador +=1

total = total_sapos + total_ratos + total_coelhos
percent_sapos = (total_sapos / total) * 100 
percent_ratos = (total_ratos / total) * 100
percent_coelhos = (total_coelhos / total) * 100

print(f"Total de cobaias utilizadas: {total}")

print(f"Total de sapos: {total_sapos}")
print(f"Percentual de sapos: {percent_sapos:.2f}%")

print(f"Total de ratos: {total_ratos}")
print(f"Percentual de ratos: {percent_ratos:.2f}%")

print(f"Total de coelhos: {total_coelhos}")
print(f"Percentual de coelhos: {percent_coelhos:.2f}%")