#8. Faça um programa para cálculos de multas de um determinado número de veículos. O programa deve ler a velocidade de um veículo e perguntar ao usuário se ele deseja inserir a velocidade de mais algum veículo, use “sim” para continuar e “não” para sair do loop. 
#Considere que a velocidade máxima da rodovia é de 60km/h e a margem de erro do é 7km/h até 100 km/h, e 7% quando o veículo estiver acima de 100 km/h.
#São 3 valores para a multa por excesso de velocidade: 
#Até 20% acima do limite permitido: R$130,16. Multa média.
#De 20% até 50% acima do limite permitido: R$195,23. Multa grave.
#Acima de 50% do limite permitido: R$880,41. Multa gravíssima.
#Ao término da leitura, informar:
#Quantos veículos não tiveram multas.
#Quantos veículos tiveram multa média.
#Quantos veículos tiveram multa grave.
#Quantos veículos tiveram multa gravíssima.
#Imprimir o somatório total das multas.
#Imprimir a média de velocidade da rodovia.
loop = 1
soma = 0
multa_total = 0
sem_multa = 0
multa_media = 0
multa_grave = 0
multa_gravissima = 0
soma_multas = 0
media_rodo = 0
carros = 0

while loop > 0:
    velocidade = int(input("Digite a velocidade do veículo em km/h: "))
    if velocidade > 0 and velocidade <= 100:
        carros += 1
        vel_registrada = velocidade - 7
    elif velocidade > 100:
        carros += 1
        vel_registrada = velocidade - (velocidade * 0.07)

    if vel_registrada <= 60:
        sem_multa += 1
        media_rodo = media_rodo + vel_registrada
        print("Velocidade permitida.")
        continuar = str(input('Deseja continuar? '))
        if continuar == "sim" or continuar == "Sim":
            continue
        else:
            loop = 0

    elif vel_registrada > 60:
        porcentagem = (vel_registrada / 60 - 1) * 100
        if porcentagem <= 20:
            multa_media += 1
            soma_multas = soma_multas + 130.16
            media_rodo = media_rodo + vel_registrada
            print(f"Multa média, R$130,16")
            continuar = str(input('Deseja continuar? '))
            if continuar == "sim" or continuar == "Sim":
                continue
            else:
                loop = 0
        elif porcentagem > 20 and porcentagem <= 50:
            multa_grave += 1
            soma_multas = soma_multas + 195.23
            media_rodo = media_rodo + vel_registrada
            print(f"Multa grave, R$195,23")
            continuar = str(input('Deseja continuar? '))
            if continuar == "sim" or continuar == "Sim":
                continue
            else:
                loop = 0
        else:
            multa_gravissima += 1
            soma_multas = soma_multas + 880.41
            media_rodo = media_rodo + vel_registrada
            print(f"Multa gravíssima, R$880,41")
            continuar = str(input('Deseja continuar? '))
            if continuar == "sim" or continuar == "Sim":
                continue
            else:
                loop = 0

media_tudo = media_rodo / carros
print(f"Veículos analisados: {carros}")
print(f"Veículos que não tiveram multas: {sem_multa}")
print(f"Veículos que sofreram multa média: {multa_media}")
print(f"Veículos que sofreram multa grave: {multa_grave}")
print(f"Veículos que sofreram multa gravíssima: {multa_gravissima}")
print(f"Total do valor das multas: {soma_multas}") 
print(f"Média da velocidade da rodovia: {media_tudo}")