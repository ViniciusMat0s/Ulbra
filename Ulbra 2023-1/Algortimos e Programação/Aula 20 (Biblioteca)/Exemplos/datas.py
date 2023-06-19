import datetime as dt #Importando módulo de datas

data_atual = dt.datetime.now()

dia = data_atual.day
minuto = data_atual.minute
hora = data_atual.hour

print(f"Data atual do sistema: {data_atual}")
print(f"Minuto atual: {minuto}")
print(f"Hora atual: {hora}")

print(f"Agora são {hora}:{minuto}")