#1- Preencher uma lista de 10 elementos, ao fim da leitura o programa deve passar os números pares para um segundo vetor, e os ímpares para um terceiro
#vetor. Imprimir os dois novos vetores no final.

lista = []
pares = []
impares = []

for i in range(10):
    elemento = int(input("Digite um número inteiro: "))
    lista.append(elemento)

for elemento in lista:
    if elemento % 2 == 0:
        pares.append(elemento)
    else:
        impares.append(elemento)

print(f"Os números pares são: {pares}")
print(f"Os números ímpares são: {impares}")
