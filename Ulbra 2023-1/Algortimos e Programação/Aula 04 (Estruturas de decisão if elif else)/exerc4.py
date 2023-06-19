# 4. Faça um algoritmo que leia um número e mostre uma mensagem indicando se este número é par ou ímpar e se é positivo ou negativo.
numero = float(input("Digite um número: "))
if numero % 2 == 0:
    print("Seu número é par.")
else:
    print("Seu número é impar.")
if numero >= 0:
    print("O número é positivo.")
else:
    print("O número é negativo.")