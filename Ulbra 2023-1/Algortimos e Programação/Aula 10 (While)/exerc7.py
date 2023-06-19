#7. Faça um programa que receba a idade, a altura e, o peso de 25 pessoas, calcule e mostre:
#a) quantidade de pessoas com idade superior a 50 anos;
#b) a média das alturas das pessoas com idade entre 10 e 20 anos;
#c) percentagem de pessoas com peso inferior a 40 quilos entre todas as pessoas analisadas.
pessoas = 1
soma_idade = 0
soma_altura = 0
soma_pessoas = 0
peso_inferior = 0
media_altura = 0
y = 0

while pessoas <= 25:
    print(f"\nPessoa nº {pessoas}\n")
    idade = int(input("Digite a idade: "))
    peso = float(input("Digite o peso: "))
    altura = int(input("Digite a altura: "))
    pessoas += 1
    if idade >= 50:
        soma_idade += 1
    elif idade >= 10 and idade <= 20:
        soma_pessoas += 1
        soma_altura = soma_altura + altura
        media_altura = soma_altura / soma_pessoas
    if peso <= 40:
        peso_inferior += 1
        x = 100 * peso_inferior
        y = x / 25

print(f"\n Pessoas acima de 50 anos: {soma_idade}.")
print(f"\n Média de altura das pessoas entre 10 e 20 anos: {media_altura}.")
print(f"\n Porcentagem de pessoas com peso inferior a 40: {y}%")