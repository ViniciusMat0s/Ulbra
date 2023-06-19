consumidos = int(input("Quantos cigarros você fuma por dia? "))
meses = float(input("Há quantos meses você fuma? "))
dias = (meses * 30)
perda = 15 * (consumidos * dias)
horas = perda / 60

if dias <= 90 and dias > 0:
    print(f"Dentes amarelos | Você perdeu cerca de {horas} horas de vida.")
elif dias > 90 and dias < 365:
    print(f"Perda de paladar e respiração comprometida | Você perdeu cerca de {horas} horas de vida.")
elif dias > 365:
    print(f"Pulmão comprometido | Você perdeu cerca de {horas} horas de vida.")
else:
    print("Não fume! Continue assim.")