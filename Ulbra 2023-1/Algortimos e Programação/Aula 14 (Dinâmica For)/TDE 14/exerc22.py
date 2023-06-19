x = 1
soma = 0
conta = 0 

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
        
print(f"o menor numero é {menor}, o maior numero é {maior} e a média é {media}. ")