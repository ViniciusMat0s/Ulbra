loop = 1
soma = 0

while loop <= 10:
    print(f"Aluno nº {loop}, nota:")
    nota = float(input("Digite a nota do aluno: "))
    soma = soma + nota
    loop += 1

media = soma / 10
print(f"A média da nota dos 10 alunos é: {media}")