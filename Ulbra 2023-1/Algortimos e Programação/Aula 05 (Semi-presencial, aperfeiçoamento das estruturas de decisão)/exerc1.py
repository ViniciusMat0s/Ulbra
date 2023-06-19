#1. Faça um algoritmo para calcular o índice de massa corporal de uma pessoa (IMC). Dada a fórmula IMC = peso(kg) / (altura  X altura(m)), informe na tela a classificação de imc de acordo com a tabela abaixo.
peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))
imc = peso / altura ** 2
imc = (round(imc, 2))
print(f"Seu IMC é de: {imc}.")

if imc<=18.5:
    print("Magreza.")
elif imc>=18.6 and imc<24.9:
    print("Peso normal.")
elif imc>=25 and imc<29.9:
    print("Sobrepeso.")
elif imc>=30 and imc<34.9:
    print("Obesidade de Grau I.")
elif imc>=35 and imc<39.9:
    print("Obesidade de Grau II.")