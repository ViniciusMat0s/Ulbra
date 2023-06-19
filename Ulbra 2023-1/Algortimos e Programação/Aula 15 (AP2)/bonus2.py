def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def find_first_n_primes(n):
    primes = []
    number = 2
    while len(primes) < n:
        if is_prime(number):
            primes.append(number)
        number += 1
    return primes

def find_largest_prime(start, end):
    largest_prime = None
    for number in range(start, end + 1):
        if is_prime(number):
            if largest_prime is None or number > largest_prime:
                largest_prime = number
    return largest_prime

def find_smallest_prime(start, end):
    smallest_prime = None
    for number in range(start, end + 1):
        if is_prime(number):
            if smallest_prime is None or number < smallest_prime:
                smallest_prime = number
    return smallest_prime

# Encontrar os 10 primeiros números primos
primes = find_first_n_primes(10)
prime_sum = sum(primes)

# Encontrar o maior número primo no intervalo de 100 a 150
largest_prime_100_150 = find_largest_prime(100, 150)

# Encontrar o menor número primo no intervalo de 200 a 230
smallest_prime_200_230 = find_smallest_prime(200, 230)

# Calcular a multiplicação
result = largest_prime_100_150 * smallest_prime_200_230

print("Soma dos 10 primeiros números primos:", prime_sum)
print("Multiplicação do maior número primo entre 100 e 150 com o menor número primo entre 200 e 230:", result)
