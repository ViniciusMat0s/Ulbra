#1. Escreva um programa que verifique se um número é múltiplo de 3 e 5 ao mesmo tempo.
numero = float(input("Digite um número: "))
if numero == 0:
    print("Número neutro.")
elif numero % 5 == 0 and numero % 3 == 0:
    print("Número múltiplo de 3 e de 5.")
else:
    print("Número não é múltiplo de 3 e de 5.")