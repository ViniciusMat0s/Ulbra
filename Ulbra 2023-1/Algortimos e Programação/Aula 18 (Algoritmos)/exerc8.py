#8 - Faça um programa que leia 5 números inteiros e passe lista de números como argumento e retorne uma string contendo os números ordenados em ordem crescente, separados por vírgula.

lista_num = []

for i in range(5):
    numero = int(input("Digite um número inteiro:\t"))
    lista_num.append(numero)
    lista_num.sort()

numeros = ''.join(str(lista_num))
print(numeros)
