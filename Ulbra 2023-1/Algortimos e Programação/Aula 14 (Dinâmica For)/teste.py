x = 1
soma = 0
conta = 0 
primo = 0
number = 0

for i in range(12):
    num = float(input("Digite um numero: "))
    soma = soma + num
    media = soma / 12
    x += 1
    if conta == 0:
        menor = num
        maior = num
    if num > maior :
        maior = num
    elif menor > num :
        menor = num
    conta = conta + 1

if number > 1:
    n = 0
    for i in number:
        if number % i == 0:
            print(number, 'não é primo')
            break
    else:
        soma += i
        print(number, 'é primo')

print(f"o menor numero é {menor}, o maior numero é {maior}, a média é {media} e a soma dos primos é {soma}")