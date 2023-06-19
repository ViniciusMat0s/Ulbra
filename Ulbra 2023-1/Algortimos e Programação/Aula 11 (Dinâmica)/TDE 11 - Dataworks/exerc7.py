#7. Gabriel e Guilherme

aprovados = 0
reprovados = 0
x = 1
while x <= 10:
    x+=1
    nome = input("Digite o nome e sobrenome do aluno: ")
    n1 = float(input("Digite a primeira nota do aluno: "))
    n2 = float(input("Digite a segunda nota do aluno: "))
    n3 = float(input("Digite a terceira nota do aluno: "))
    if  0 > n1 or n1 > 10:
        print("\nPrimeira nota invalida\n") 
        x = 1
        reprovados = 0
        aprovados = 0
        continue
    if  0 > n2 or n2 > 10:
        print("\nSegunda nota invalida\n") 
        x = 1
        reprovados = 0
        aprovados = 0
        continue
    if  0 > n3 or n3 > 10:
        print("\nTerceira nota invalida\n") 
        x = 1
        reprovados = 0
        aprovados = 0
        continue
    nota =(n1 + n2 + n3) / 3
    if nota >= 7:
        aprovados += 1
    if nota <= 6:
        reprovados += 1



porcentagem = (100 / 3) * aprovados
print(f"\nO número de alunos aprovados é de {aprovados}")
print(f"O número de alunos reprovados é de {reprovados}")
print(f"A porcentagem de alunos aprovados é de {porcentagem}%\n")
