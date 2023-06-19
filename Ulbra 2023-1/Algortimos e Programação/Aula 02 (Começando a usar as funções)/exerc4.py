#Faça um algoritmo que leia dois números reais e imprima a soma e a média aritmética desses números.
numero1 = input("Insira um número inteiro: ")
numero1 = int(numero1)
numero2 = input("Insira outro número: ")
numero2 = int(numero2)
media = numero1 + numero2 / 2
soma = numero1 + numero2
print("A soma dos números é: " + str(soma))
print("A média dos números é " + str(media))