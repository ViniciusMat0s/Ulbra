positivo = 0
nulo = 0
negativo = 0

for i in range(10):
    num = float(input("Digite um número: "))
    if num < 0:
        negativo += 1
    if num >= 1:
        positivo += 1
    if num == 0:
        nulo += 1

print(f"\nNulos {nulo} | Positivos {positivo} | Negativos {negativo}")