#4- Faça um programa que leia uma lista de 5 elementos inteiros e mostre a soma dos elementos lidos.

numeros = []

for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)
    soma = sum(numeros)

print(f"\nA soma dos números inteiros digitados é: {soma}\n")