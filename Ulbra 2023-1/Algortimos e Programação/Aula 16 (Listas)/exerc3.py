#3- Faça um programa que leia uma lista de 5 elementos e mostre-os na tela na ordem inversa que foi digitada.

nomes = []

for i in range(5):
    nome = input("Digite um nome: ")
    nomes.insert(0, nome)

print(f"\nOs nomes que foram digitados (em ordem inversa) foram: {nomes}\n")