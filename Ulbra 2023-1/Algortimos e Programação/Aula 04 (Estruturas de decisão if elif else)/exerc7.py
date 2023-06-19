#7. Faça um algoritmo que lê dois valores e escreve cada um juntamente com a mensagem: “É múltiplo de 2” ou “Não é múltiplo de dois”.
valor1 = float(input("Digite um valor: "))
valor2 = float(input("Digite outro valor: "))
if valor1 % 2 == 0:
    print(f"O valor {valor1} é múltiplo de dois.")
else:
    print (f"O valor {valor1} não é múltiplo de dois.")
if valor2 % 2 == 1:
    print(f"O valor {valor2} não é múltiplo de dois.")
else:
    print(f"O valor {valor2} é múltiplo de dois.")