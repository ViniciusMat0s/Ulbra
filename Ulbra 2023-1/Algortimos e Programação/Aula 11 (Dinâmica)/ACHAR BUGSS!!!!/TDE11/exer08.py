maiores = menores = soma_maiores = soma_menores = 0

for i in range(10):

    numero = float(input("Digite um número: "))

    if numero >= 0:
        maiores += 1
        soma_maiores += numero
    else:
        menores += 1
        soma_menores += numero

print(f"Quantidade de números maiores ou igual a 0: {maiores}")
print(f"Quantidade de números menores que 0: {menores}")
print(f"Soma de todos os números maiores que zero: {soma_maiores}")
print(f"Soma de todos os números menores que zero: {soma_menores}")