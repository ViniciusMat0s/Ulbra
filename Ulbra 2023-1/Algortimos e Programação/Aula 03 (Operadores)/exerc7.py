#7. Faça um algoritmo que leia três números inteiros e calcule a sua média. Ao final, o algoritmo deve escrever os números lidos e o resultado da média.
numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite outro número: "))
numero3 = float(input("Digite mais um número: "))
media = (numero1 + numero2 + numero3) / 3
media = (round(media,2))
print("A média total dos números é:",media)