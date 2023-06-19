nulos = 0
negativos = 0
positivos = 0
cont = 0

while cont < 10:
    num = float(input("Digite um número: "))
    if num == 0:
        nulos += 1
    elif num < 0:
        negativos += 1
    else:
        positivos += 1
    cont += 1

print("Quantidade de números nulos:",nulos)
print("Quantidade de números negativos:", negativos)
print("Quantidade de números positivos:", positivos)