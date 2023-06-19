# 3. Escreva um algoritmo que leia vários números e quando o valor 0 (zero) for lido, o algoritmo deverá cessar sua execução. Informe:
# quantos números entre 50 e 150 foram digitados.
# quantos números divisíveis por 4 foram digitados.
# a média dos números menores que 40. 



       
n = 0
i = 0
total = 0
intervalo = 0
divisivel = 0
for i in range(9999999999999999):
    num = int(input("Digite um numero: "))
    if num != 0:
        continue
    if num > 50 and num < 150:
        intervalo += num
        num += 1
        print(f"Foram digitados {num} entre 50 e 150.")
    if num % 4 == 0:
        divisivel += num
        print(f"No total foram digitados {num} divisíveis por 4")
    if num < 40:
        
        print(f"A média dos números menores que 40 é {num}")   
    if num == 0:
        break