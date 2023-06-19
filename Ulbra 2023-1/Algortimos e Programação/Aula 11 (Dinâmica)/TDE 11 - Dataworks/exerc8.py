#8. Gabriel e Guilherme

mais_0 = 0
menos_0 = 0
soma_maior = 0
soma_menor = 0

x = 1
while x <= 10:
    x+=1
    n = int(input("Digite um numero: "))
    if n >= 0:
        mais_0 += 1
        soma_maior += n 
    elif n < 0:
        menos_0 += 1
        soma_menor += n

print(f"\nQuantidade de números maiores ou igual a 0: {mais_0}")
print(f"Quantidade de números menores que 0: {menos_0}")
print(f"Soma dos números digitados maiores que 0: {soma_maior}")
print(f"Soma dos números digitados menores que 0: {soma_menor}\n")

