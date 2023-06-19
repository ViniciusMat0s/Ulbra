pessoas = int(input("Quantas pessoas foram ouvidas na região? "))
media = salario_m = salario_f = qtd_m = qtd_f = 0
idade_maior = sexo_maior = salario_maior = 0

for i in range (1, pessoas + 1):
    idade = int(input(f"Digite a idade da pessoa {i}? "))
    sexo = input(f"Qual o Sexo da Pessoa {i}? (M/F) ")
    salario = float(input(f"Qual o salário da pessoa {i}? "))
    media = media + salario

    if salario > salario_maior:
        salario_maior = salario
        idade_maior = idade
        sexo_maior = sexo

    if idade < 0:
        break

    if sexo == "M" or sexo == "m":
        salario_m = salario_m + salario
        qtd_m = qtd_m + 1
    elif sexo == "F" or sexo == "f":
        salario_f = salario_f + salario
        qtd_f = qtd_f + 1
    else:
        break 

    if sexo == "F" or sexo == "f" and salario <= 1200:
        qtd_f_salario = qtd_f_salario + 1


media = media / i
media_m = salario_m / qtd_m
media_f = salario_f / qtd_f
print("\n")
print(f"A média do salário do grupo é R${media}")
print(f"A média salarial dos homens é R${media_m}")
print(f"A média salarial das mulheres é R${media_f}")
print(f"O maior salário é de uma pessoa do sexo {sexo_maior}, que tem {idade_maior} anos e recebe R${salario_maior}")