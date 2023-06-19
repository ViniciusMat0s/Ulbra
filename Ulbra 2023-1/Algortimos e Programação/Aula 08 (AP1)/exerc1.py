horas_sono = float(input("Insira o seu tempo diário de sono (em horas): "))
tempo = float(input("Há quano tempo você dorme dessa maneira? (em meses): "))
if horas_sono <= 8 and horas_sono > 0:
    perdido = ((8 - horas_sono) * 1.5) * (tempo * 30)
    print(f"Tendo {horas_sono} horas de sono por {tempo} meses, você perdeu um total de {int(perdido)} horas de vida.")
elif horas_sono > 8:
    print("Você tem um sono saudável!")
if (horas_sono < 4) and (tempo > 3):
    print("Risco de problemas cardíacos e aumento do risco de acidentes.")
elif (horas_sono >= 4 and horas_sono <= 6) and (tempo > 6):
    print("Risco de diminuição da capacidade de concentração e da memória.")
elif (horas_sono >= 6 and horas_sono <= 8) and (tempo >= 12):
    print("Menor risco de problemas de saúde e maior disposição física e mental.")
elif (horas_sono > 8) and (tempo >= 12):
    print("Aumento do risco de doenças crônicas, como obesidade e diabetes.")
elif (horas_sono < 4) or (horas_sono >= 4 and horas_sono <= 6) or (horas_sono > 8) and (tempo < 3):
    print("Você precisa melhorar a qualidade de seu sono, procure dormir entre 6 e 8 horas por dia.")