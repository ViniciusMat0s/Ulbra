#6. Faça um algoritmo para ler dois valores: NUM1 e NUM2, e se NUM1 for maior que NUM2 executa a soma de NUM1 e NUM2; caso contrário, executa uma subtração.
num1 = float(input("Digite um valor: "))
num2 = float(input("Digite outro valor: "))
if num1 > num2:
    soma = num1 + num2
    print(f"O resultado da soma dos dois números é: {soma}")
else:
    subtracao = num2 - num1
    print(f"O resultado da subtração é: {subtracao}")