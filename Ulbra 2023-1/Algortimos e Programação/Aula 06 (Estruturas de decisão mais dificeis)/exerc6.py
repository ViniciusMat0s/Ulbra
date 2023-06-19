#6. Escrever um programa que lê as 3 notas obtidas por ele em provas. Para cada aluno, calcular a média de aproveitamento, usando a fórmula:
n1 = float(input("Digite a primeira nota: "))
if n1 > 10 or n1 < 0:
    print("Nota inválida!")
n2 = float(input("Digite a segunda nota: "))
if n2 > 10 or n2 < 0:
    print("Nota inválida!")
n3 = float(input("Digite a terceira nota: "))
if n3 > 10 or n3 < 0:
    print("Nota inválida!")
    
ma = (n1 + n2 + n3) / 3
ma = round(ma, 2)

if ma > 10 or ma < 0:
    print("Erro na nota!")
elif ma >= 9.0:
    print(f"Com média de {ma}, você está aprovado. Nota A.")
elif ma >= 7.5 and ma < 9.0:
    print(f"Com média de {ma}, você está aprovado.Nota B.")
elif ma >= 6.0 and 7.5:
    print(f"Com média de {ma}, você está aprovado. Nota C")
elif ma >= 4.0 and ma < 6.0:
    print(f"Com média de {ma}, você está reprovado. Nota D.")
elif ma < 4.0 and ma >= 0:
    print(f"Com média de {ma}, você está reprovado. Nota E.")