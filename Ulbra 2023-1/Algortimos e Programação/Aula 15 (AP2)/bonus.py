def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_primes():
    primes = []
    while True:
        num = int(input("Digite um número primo (ou qualquer número não primo para sair): "))
        if is_prime(num):
            primes.append(num)
        else:
            break
    return primes

primes = sum_primes()

if len(primes) > 0:
    sum_of_primes = sum(primes)
    smallest_prime = min(primes)
    largest_prime = max(primes)
    print("A soma dos números primos digitados é:", sum_of_primes)
    print("O menor número primo inserido é:", smallest_prime)
    print("O maior número primo inserido é:", largest_prime)
else:
    print("Nenhum número primo foi digitado.")
