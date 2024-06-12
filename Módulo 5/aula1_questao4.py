from datetime import datetime

data = datetime.now()
today = data.strftime('%d/%m/%Y')
hora = data.strftime('%H:%M')
print(f"Data: {today}")
print(f"Hora: {hora}")