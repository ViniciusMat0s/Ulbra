#3. Faça um algoritmo para ler dois valores numéricos e apresentar a diferença do maior pelo menor.
valor1 = float(input("Digite um valor: "))
valor2 = float(input("Digite outro valor: "))
if valor1 > valor2:
    diferença = valor1 - valor2
    print(f"O valor maior é {valor1} e sua diferença para o menor é: {diferença}")
else:
    diferença = valor2 - valor1
    print(f"O valor maior é {valor2} e sua diferença para o menor é: {diferença}")