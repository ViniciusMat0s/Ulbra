#1- Faça um programa que leia uma lista de 5 elementos inteiros e mostre-os na tela.

numeros = []

for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

print(f"\nOs números inteiros digitados foram: {numeros}\n")