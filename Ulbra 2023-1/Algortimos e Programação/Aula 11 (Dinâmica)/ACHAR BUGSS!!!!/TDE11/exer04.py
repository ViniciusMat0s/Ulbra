num = int(input("Digite o número: "))
loop = 1
loop_inv = -1
valor = 0
final = 0

if num < 0:
    while loop_inv >= num:
        loop_inv -= 1
        valor -= 1
        final = final + valor

if num > 0:
    while loop <= num:
        loop += 1
        valor += 1
        final = final + valor

print(f"A soma dos valores de 0 até {num} é: {final}")