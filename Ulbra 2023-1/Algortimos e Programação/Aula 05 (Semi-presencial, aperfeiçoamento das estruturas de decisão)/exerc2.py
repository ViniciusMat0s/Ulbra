#2. Faça um algoritmo para ler e escrever três números. Se o primeiro for positivo, imprimir sua raiz quadrada, caso contrário, imprimir o seu quadrado; se o segundo número for maior que 10 e menor que 100, imprimir a mensagem: "NÚMERO ESTÁ ENTRE 10 E 100 - INTERVALO PERMITIDO"; se o terceiro número for menor que o segundo, calcular e escrever a diferença entre eles, caso contrário, calcular e escrever a soma entre eles. 
num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
num3 = float(input("Digite mais um número: "))
if num1 >= 0:
    raiz = num1 ** 0.5
    raiz = (round(raiz, 2))
    print(f"A raiz quadrada de {num1} é: {raiz}")
else:
    quadrado = num1 * num1
    print(f"O número {num1} ao quadrado é: {quadrado}")
if num2 >= 10 and num2 <= 100:
    print("O número está entre 10 e 100 - Intervalo Permitido!")
else:
    print("O número não está entre 10 e 100 - Intervalo Negado!")
if num3 < num2:
    dfrnc = num2 - num3
    print(f"O seu segundo número é maior que o terceiro, portanto, a diferença entre {num2} e {num3} é de: {dfrnc}.")
else:
    soma = num3 + num2
    print(f"O seu terceiro número é maior que o segundo, portanto, a soma dos dois é de: {soma}.")