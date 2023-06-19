num1 = 0
num2 = 0
num3 = 0
media = 0
num4 = 0

for i in range(1,500):
    num = float(input("Digite um número:"))
    if num == 0:
        break
    if num % 4 == 0:
        num1 += 1
    if num >= 50 and num <= 150: 
        num2 += 1
    if num <= 40:
        num3 += 1
        num4 += num
        media = num4 / num3

print(f"Divisíveis por 4: {num1} | Entre 50 e 150: {num2} | Média dos números menores que 40: {media}")