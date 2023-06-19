maiores = 0
menores = 0
somamaiores = 0
somamenores = 0

for i in range(10):
    num = float(input("Digite um número: "))
    if num < 0:
        menores += 1
        somamenores += num
    if num >= 0:
        maiores += 1
        somamaiores += num

print(f"\n=================================\nNúmeros maiores ou iguais a 0: {maiores}\n---------------------------------\nNúmeros menores que 0: {menores}\n---------------------------------\nSoma de maiores ou iguais a 0: {somamaiores}\n---------------------------------\nSoma de menores que 0: {somamenores}\n=================================\n")