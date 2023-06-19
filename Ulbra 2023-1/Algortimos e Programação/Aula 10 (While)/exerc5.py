#5. Faça um algoritmo que exiba todos os múltiplos de 5 no intervalo de 1 a 200.

num = 1
while num <= 200:
    num += 1
    if (num % 5) == 0:
        print(f"Múltiplo de 5: {num}")