#2. Faça um programa que lê um conjunto de 4 valores i, a, b, c, onde i é um valor inteiro e positivo e a, b, c, são quaisquer valores reais e os escreva. A seguir:
#Se i=1 escrever os 3 valores a, b, c em ordem crescente;
#Se i=2 escrever os 3 valores a, b, c em ordem decrescente;
#Se i=3 escrever os 3 valores de forma que o maior valor entre a, b, c fica entre os outros dois.
i = int(input("Digite um número de 1 a 3: "))
a = float(input("Digite o valor de (A): "))
b = float(input("Digite o valor de (B): "))
c = float(input("Digite o valor de (C): "))
maior = 0
meio = 0
menor = 0

if a > b and a > c:
    maior = a
    if b > c:
        meio = b
        menor = c
    else:
        meio = c
        menor = b
elif b > c and b > a:
    maior = b
    if a > c:
        meio = a
        menor = c
    else:
        meio = c
        menor = a
else:
    maior = c
    if a > b:
        meio = a
        menor = b
    else:
        meio = b
        menor = a
if i == 1:
    print(f"Ordem crescente: {menor, meio, maior}.")
elif i == 2:
    print(f"Ordem decrescente: {maior, meio, menor}")
elif i == 3:
    print(f"Maior no meio: {menor, maior, meio}")
else:
    print("Número inválido.")