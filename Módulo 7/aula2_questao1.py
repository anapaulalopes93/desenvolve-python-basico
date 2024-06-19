meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

nascimento = input("Digite uma data de nascimento (dd/mm/aaaa): ")
dia, mes, ano = nascimento.split('/')
dia = int(dia)
mes = int(mes)
ano = int(ano)

mes_extenso = f"Você nasceu em {dia} de {meses[mes - 1]} de {ano}."
print(mes_extenso)