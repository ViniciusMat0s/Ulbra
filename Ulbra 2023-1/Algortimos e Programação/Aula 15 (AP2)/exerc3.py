sem_multa = 0
media = 0
grave = 0
gravissima = 0
soma = 0
total = 0
analisados = 0

for i in range(99999999999999999999999):
    velocidade = float(input("Digite a velocidade registrada em km/h [Digite -1 para encerrar o programa]: "))

    if velocidade < 0:
        print("Velocidade menor que 0 km/h, programa encerrado.")
        break

    if velocidade >= 0 and velocidade <= 40:
        print(f"Velocidade de {velocidade}km/h, inferior à metade da velocidade máxima da via, multa média no valor de R$ 130,16.")
        media += 1
        soma += 130.16
        analisados += 1
        total += velocidade
    elif velocidade > 40 and velocidade <= 80:
        print(f"Velocidade permitida, não houve multas.")
        sem_multa +=1
        analisados +=1
        total += velocidade
    elif velocidade > 80:
        margem = velocidade - 5
        if margem <= 80:
            print(f"Velocidade permitida, não houve multas.")
            sem_multa +=1
            analisados +=1
            total += velocidade
        if margem > 80 and margem < 96: #maxima 80 + 20% de 80 = 16
            print(f"Velocidade de {velocidade}km/h, 20% acima do valor permitido, multa média no valor de R$ 130,16.")
            media += 1
            soma += 130.16
            analisados += 1
            total += margem
        elif margem >= 96 and margem < 120:
            print(f"Velocidade de {velocidade}km/h, de 20% até 50% acima do limite permitido, multa grave no valor de R$ 195.23.")
            grave += 1
            soma += 195.23
            analisados += 1
            total += margem
        elif margem >= 120:
            print(f"Velocidade de {velocidade}km/h, 50% acima do limite permitido, multa gravíssima no valor de R$ 880,41.")
            gravissima += 1
            soma += 880.41
            analisados += 1
            total += margem

media = total / analisados
print(f"\n ===================================== \n Média de velocidade da rodovia: {media} \n Veículos sem multa: {sem_multa} \n Multas médias: {media} \n Multas graves: {grave} \n Multas gravíssimas {gravissima} \n Valor total em multas: {soma} \n -------------------------------------")