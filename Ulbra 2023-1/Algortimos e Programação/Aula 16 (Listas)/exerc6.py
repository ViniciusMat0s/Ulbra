#6- Preencher uma lista de 8 elementos inteiros. Mostrar a lista e informar quantos números são maiores que 30, e apresentar a somar apenas destes números;

numeros = []
digitados = 0
digitadosm = 0
maiores = []
soma = 0

for i in range(8):
    numero = int(input('Digite um elemento inteiro: '))
    if numero > 30:
        numeros.append(numero)
        maiores.append(numero)
        digitadosm += 1
        digitados += 1
        soma += numero
    else:
        numeros.append(numero)
        digitados += 1

qntdigitados = len(numeros)

if digitadosm > 0:
    print(f"\nOs números da lista são: {numeros}")
    print(f"A soma dos elementos maiores que 30 é: {soma}")
    print(f"Foram digitados [{digitadosm}] números maiores que 30, são eles: {maiores}\n")
else:
    print(f"\nOs números da lista são: {numeros}")
    print(f"Nenhum elemento inteiro maior que 30 foi digitado.\n")