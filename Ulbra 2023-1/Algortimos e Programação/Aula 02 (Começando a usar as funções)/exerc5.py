#Faça um algoritmo que leia um número inteiro e imprima seu antecessor e seu sucessor.
numero1 = input("Insira um número inteiro ")
numero1 = int(numero1)
antecessor = numero1 - 1
antecessor = int(antecessor)
sucessor = numero1 + 1
sucessor = int(sucessor)
subtracao = numero1 - antecessor
print(" O antecessor do número " + str(numero1) + " é " + str(antecessor) + ".")
print(" O sucessor do número " + str(numero1) + " é " + str(sucessor) + ".")