#5. Faça um programa que leia o código de um aluno e suas três notas. Calcule a média ponderada do aluno, considerando que o peso para a maior nota seja 4 e para as duas restantes, 3. Mostre o código do aluno, suas três notas, a média calculada e a mensagem “ APROVADO” se a média for maior ou igual a 7 e “REPROVADO” se a média for menor que 7.
aluno = str(input("Digite o código do aluno: "))
nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))
nota3 = float(input("Digite a nota da terceira prova: "))
media = ((nota1*4) + (nota2*3) + (nota3*3)) / 10
media = round(media, 2)
if media > 10 or media < 0:
    print("Nota inválida!")
elif media >= 7:
    print(f"O aluno de código {aluno}, está APROVADO com média de {media} em suas provas ({nota1}, {nota2} e {nota3}).")
elif media < 7:
    print(f"O aluno de código {aluno}, está REPROVADO com média de {media} em suas provas ({nota1}, {nota2} e {nota3}).")