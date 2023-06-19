#5- Faça um programa que leia uma lista de 5 elementos inteiros, ao fim o programa deve mostrar a média dos elementos lidos e a soma dos 
#elementos lidos. Deve criar uma função soma e uma função média que receba a lista como argumento e retorne o valor.

def soma(elementos):
    soma = sum(elementos)
    print(f"\nSoma dos elementos: {soma}")

def media(elementos):
    media = sum(elementos) / len(elementos)
    print(f"Média dos elementos: {media}\n")

elementos = []

for i in range (5):
    elemento = int(input("\nDigite um elemento inteiro:\n"))
    elementos.append(elemento)

soma(elementos), media(elementos)