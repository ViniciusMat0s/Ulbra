#6. Faça um programa que calcule a média ponderada de um aluno a partir de suas três notas e seus respectivos pesos. Considere que as notas valem 20%, 30% e 50%, respectivamente. O usuário deve informar as três notas de 0 a 10 e caso sua média seja maior ou igual a 6 informar aprovado, caso contrário reprovado.
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 * 0.2) + (nota2 * 0.3) + (nota3 * 0.5) / 1.0
if nota1 > 10 or nota1 < 0 or nota2 > 10 or nota2 < 0 or nota3 > 10 or nota3 < 0:
    print("Nota inválida!")
else:
    print(f"Média ponderada de {media}")