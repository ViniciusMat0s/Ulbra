#6. Escreva um algoritmo que leia vários números e informe quantos números 
#entre 100 e 200 foram digitados. Quando o valor 0 (zero) for lido, o algoritmo 
#deverá cessar sua execução.
x = 1
i = 0
digitados = 0

while x > 0:
    digitados += 1
    num = float(input("Digite um número (Digite [0] para finalizar a contagem): "))
    if num >= 100 and num <= 200:
        i += 1
    elif num == 0:
        x = 0
print(f"Foram digitados [{digitados - 1}] numeros, [{i}] deles foram entre 100 e 200.")