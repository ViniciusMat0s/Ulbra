#5- Faça um programa que leia uma lista de 10 elementos inteiros ou até os usuários digitar 99, ao fim o programa deve mostrar a média dos elementos lidos, 
#a soma dos elementos lidos, e quantos foram os elementos lidos.

numeros = []
digitados = 0
soma = 0

for i in range(10):
    numero = int(input('Digite um elemento inteiro (Para finalizar, digite "99" ): '))
    if numero == 99:
        break
    numeros.append(numero)
    digitados += 1
    soma += numero

qntdigitados = len(numeros)
media = soma / qntdigitados

print(f"\nA média dos elementos é: {media}")
print(f"A soma dos elementos é: {soma}")
print(f"Elementos digitados: {qntdigitados}\n")