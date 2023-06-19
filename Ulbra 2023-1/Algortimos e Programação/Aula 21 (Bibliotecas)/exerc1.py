#1- Faça um programa que preencha uma lista de 10 elementos, ao fim da leitura o programa deve
#passar os números pares para um segundo vetor(lista), e os ímpares para um terceiro vetor(lista). Imprimir os dois vetores no final.

#v1 = módulo com entrada do usuário.

def elementos(elementos):
    for i in range(10):
        elementos = int(input("Digite um elemento: "))
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

elementos(elementos)
resultado(lista, pares, impares)