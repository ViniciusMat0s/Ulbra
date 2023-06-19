#1. Dados dois números A e B, some 100 ao maior número e imprima.
numero_a = float(input("Digite um número: "))
numero_b = float(input("Digite outro número: "))
if numero_a > numero_b:
    soma = numero_a + 100
    print(f"O número {numero_a} é maior.")
else:
    print(f"O número {numero_b} é maior.")