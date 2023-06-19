#1- Faça um programa que preencha uma lista de 10 elementos, ao fim da leitura o programa deve
#passar os números pares para um segundo vetor(lista), e os ímpares para um terceiro vetor(lista). Imprimir os dois vetores no final.

#v2 = módulo com elementos aleatórios gerados pela biblioteca.

import random as r

def elemento(elementos):
    print("Se o valor mínimo for maior que o valor máximo, o programa fechará.")
    inicio = int(input("Digite o número mínimo para os elementos: "))
    final = int(input("Digite o número máximo para os elementos: "))
    for i in range(10):
        elementos = r.randint(inicio, final)
        lista.append(elementos)
        if elementos % 2 == 0:
            pares.append(elementos)
        else:
            impares.append(elementos)

def resultado(lista, pares, impares):
    print(f"\nOs 10 elementos escolhidos foram:\n{lista}")
    print(f"\nLista de números elementos pares:\n{pares}")
    print(f"\nLista de números elementos ímpares:\n{impares}")
    
lista = []
pares = []
impares = []

elemento(elemento)
resultado(lista, pares, impares)