#5. Faça um algoritmo para ler dois números. Se os números forem iguais, imprimir a mensagem: "NÚMEROS IGUAIS" e encerrar a execução; caso contrário, imprimir o de maior valor.
numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite outro número: "))
if numero1 == numero2:
    print("NÚMEROS IGUAIS")
elif numero1 > numero2:
    print(f"O número maior é: {numero1}")
else:
    print(f"O número maior é: {numero2}")