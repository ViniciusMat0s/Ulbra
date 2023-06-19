#8. Faça um algoritmo para calcular  o valor da multa de um veículo. Considere que o veículo está trafegando pela estrada do mar onde a velocidade máxima é de 80km/h e o radar tem uma margem de erro de 7%. Informe a velocidade do veículo caso esteja abaixo da velocidade exibir uma mensagem com a velocidade, informando que não houve multa, caso contrário, informar o valor da multa de acordo com o texto abaixo:
velocidade = float(input("Qual a velocidade do veículo (em km/h): "))
if velocidade <= 0:
    print("O carro está parado!")
if velocidade <= 85.6:
    print("Velocidade permitida, não houve multa.")
if velocidade > 85.7 and velocidade < 102.72:
    print(f"Velocidade de {velocidade}km/h, 20% acima do valor permitido, multa média no valor de R$ 130,16.")
if velocidade > 102.73 and velocidade < 128.40:
    print(f"Velocidade de {velocidade}km/h, de 20% até 50% acima do limite permitido, multa grave no valor de R$ 195.23.")
if velocidade > 128.41:
    print(f"Velocidade de {velocidade}km/h, 50% acima do limite permitido, multa gravíssima no valor de R$ 880,41. ")