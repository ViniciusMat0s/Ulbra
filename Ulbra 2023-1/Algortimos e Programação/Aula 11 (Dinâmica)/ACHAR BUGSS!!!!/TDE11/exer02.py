# Efetue um programa que faça a soma de números inteiros ímpares situados na faixa de 100 a 500. 

soma = 0
numero = 101

while numero <= 499:
    soma += numero
    numero += 2

print(f"A soma dos números é igual a {soma}")
