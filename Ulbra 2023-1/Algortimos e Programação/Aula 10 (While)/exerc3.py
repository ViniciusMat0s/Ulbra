#3. Faça um algoritmo que leia 10 valores inteiros e:
#• Encontre e mostre o maior valor 
#• Encontre e mostre o menor valor 
#• Calcule e mostre a média dos números lidos
soma = 0
x = 1
maior = 0
menor = 9999999999999999999999999999999999999999999999999999999999999

while x <= 10:
    x += 1
    num = int(input("Digite um número: "))
    soma = soma + num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
media = soma / 10

print(f"====================\nO número maior é: {maior}\n--------------------")
print(f"O número menor é: {menor}\n--------------------")
print(f"A média dos números é: {media}\n=====================")