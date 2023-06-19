#2- Faça um programa que leia uma lista de número não determinado de nomes, ao ser digitado "fim" deve mostrar na tela todos os nomes lidos.

nomes = []

while True:
    nome = input('Digite um nome (Para finalizar, digite "fim"): ')
    if nome == "fim" or nome == "Fim" or nome == "FIM":
        break
    nomes.append(nome)

print(f"\nOs nomes lidos foram: {nomes}\n")