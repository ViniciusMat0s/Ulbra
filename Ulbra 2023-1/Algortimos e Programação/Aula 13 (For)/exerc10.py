soma = 0

for i in range(1,101):
    if i > 3:
        if i % 2 == 0 or i % 3 == 0:
            soma += i

print(f"\nA soma dos números de 1 a 100 (exceto os números primos) é: {soma}\n")