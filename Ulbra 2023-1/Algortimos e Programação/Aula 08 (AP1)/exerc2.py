velocidade = float(input("Digite a velocidade registrada em km/h: "))
if velocidade > 0 and velocidade <= 100:
    velocidade = velocidade - 7
elif velocidade > 100:
    velocidade = velocidade - (velocidade * 0.07)
else:
    print("Velocidade inserida está inválida.")
if velocidade > 0 and velocidade <= 80:
    print("Velocidade permitida, não houve multa.")
elif velocidade > 80:
    porcentagem = (velocidade / 80 - 1) * 100
    if porcentagem <= 20:
        print(f"Velocidade de {velocidade}km/h, 20% acima do valor permitido, multa média no valor de R$ 130,16.")
    elif porcentagem > 20 and porcentagem <= 50:
        print(f"Velocidade de {velocidade}km/h, de 20% até 50% acima do limite permitido, multa grave no valor de R$ 195.23.")
    else:
        print(f"Velocidade de {velocidade}km/h, 50% acima do limite permitido, multa gravíssima no valor de R$ 880,41. ")