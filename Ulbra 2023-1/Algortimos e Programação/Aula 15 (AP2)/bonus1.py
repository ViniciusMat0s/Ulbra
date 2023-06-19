def primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
            if num >= 100 and num <= 150 or num >= 200 and num <= 230:
                if num % i == 0:
                    return False
            return True

def sum_primo():
    primos = []
    count = 0
    while count < 10:
        num = int(input("Digite um número: "))
        if primo(num):
            primos.append(num)
            count += 1
    return primos

primos = sum_primo()

if len(primos) > 0:
    soma = sum(primos)
    menor = min(primos)
    maior = max(primos)
    print(f"A soma dos números primos é: {soma}")
    print(f"O menor número primo inserido é: {menor}")
    print(f"O maior número primo inserido é: {maior}")
else:
    print("Nenhum número primo foi digitado.")
