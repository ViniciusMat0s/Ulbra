#Descreva um algoritmo que de na como calcular o IMC de uma pessoa
peso = input("Informe seu peso: ")
peso = float(peso)
altura = input("Informe sua altura: ")
altura = float(altura)
imc = peso / altura ** 2
imc = (round(imc, 2))
print("Seu IMC é de: " + str(imc) + ".")

if (imc<18.5):
    print("Você está muito magro!")
if (imc>18.5):
    print("Você está saudável!")
if (imc>24.9):
    print("Você está em sobrepeso!")
if (imc>29.9):
    print("Você tem obesidade")
if (imc>39.9):
    print("Você tem obesidade grave")