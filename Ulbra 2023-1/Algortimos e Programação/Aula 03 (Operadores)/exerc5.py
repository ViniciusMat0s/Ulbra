#5. Faça um algoritmo que leia dois números e calcule qual é o valor inteiro da divisão do 2o pelo 1o número. Exiba na tela este valor final.
numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))
resto = (numero2 // numero1)
resto = int(resto)
print("O valor inteiro da divisão é:",resto)