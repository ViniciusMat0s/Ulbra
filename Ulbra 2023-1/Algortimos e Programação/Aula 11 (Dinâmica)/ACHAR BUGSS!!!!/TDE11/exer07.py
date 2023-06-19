aprovados = 0
reprovados = 0
alunos = []

for i in range(10):
    nome = input("Digite o nome do aluno {}: ".format(i+1))
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    media = (nota1 + nota2 + nota3) / 3

    if (nota1 or nota2 or nota3 < 0) or (nota1 or nota2 or nota3 > 10):
        print("Erro")

    if media >= 7 and media <= 10:
        aprovados += 1
        situacao = "Aprovado"
    elif media >= 0 and media <= 6:
        reprovados += 1
        situacao = "Reprovado"
    else:
        reprovados += 1
        situacao = "Erro!!"
        print("ERRO!")
    alunos.append([nome, media, situacao])
print("")
print("Resultados dos alunos:")
for aluno in alunos:
    print("O aluno {} está {} com média {:.1f}.".format(aluno[0], aluno[2], aluno[1]))

percent_aprovacao = aprovados / 10 * 100
percent_reprovacao = reprovados / 10 * 100

print("Quantidade de aprovados: ", aprovados)
print("Quantidade de reprovados: ", reprovados)
print("Índice de aprovação: {:.1f}%".format(percent_aprovacao))

#nota 11 passou para media