# 8. Faça um algoritmo para ler três valores quaisquer e escrever o maior dos 3.
valor1 = float(input("Digite um número: "))
valor2 = float(input("Digite outro número: "))
valor3 = float(input("Digite mais um número: "))
if valor1 > valor2 and valor1 > valor3:
    print(f"O número {valor1} é o maior.")
elif valor2 > valor1 and valor2 > valor3:
    print(f"O número {valor2} é o maior.")
else:
    print(f"O número {valor3} é o maior.")