#4. Faça um algoritmo que exiba na tela os números ímpares entre 100 e 300.

num = 100
while num <= 299:
    num += 1
    if (num % 2) != 0:
        print(f"Ímpar: {num}")