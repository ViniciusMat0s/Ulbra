#8. Fazer um algoritmo que calcule o número de litros de combustível gastos em uma viagem, sabendo-se que o carro faz 12 km com um litro. Deverão ser lidos o tempo gasto na viagem e a velocidade média.
tempo_gasto = float(input("Informe o tempo gasto (em horas): "))
velocidade_media = float(input("Informe a velocidade média da viagem: "))
distancia = tempo_gasto * velocidade_media
litros_gastos = distancia / 12
litros_gastos = (round(litros_gastos,2))
print("O consumo total de combustível para a viagem foi de",litros_gastos,"litros.")