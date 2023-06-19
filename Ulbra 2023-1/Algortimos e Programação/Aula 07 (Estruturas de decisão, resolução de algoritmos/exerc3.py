#3. Escreva um programa que verifique se um número está entre dois outros números.
numero = float(input("Digite um número: "))
num_superior = float(input("Digite o número superior: "))
num_inferior = float(input("Digite o número inferior: "))
if numero > num_inferior and numero < num_superior:
    print("O número está entre os dois números.")
else:
    print("O número não está entre os dois números. ")