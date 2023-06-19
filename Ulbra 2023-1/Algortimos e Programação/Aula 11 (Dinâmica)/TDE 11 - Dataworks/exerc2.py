#2. Vinícius e Mary

num = 100
soma = 0

while num <= 499:
    num += 1
    if (num % 2) != 0:
        soma = soma + num
        print(f"Ímpar: {num}")

print(f"===================================\nA soma de todos os números é: {soma}\n-----------------------------------")