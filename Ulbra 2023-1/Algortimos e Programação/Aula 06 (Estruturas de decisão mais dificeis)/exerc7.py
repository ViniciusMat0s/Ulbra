#A empresa Enxuga Gelo SA decidiu conceder um aumento de salários a seus funcionários de acordo com a tabela a seguir:
#Escrever um programa que lê o nome e o salário atual de funcionário e escreve o nome do funcionário, seu salário atual, o percentual de seu aumento e o valor do salário corrigido.
nome = str(input("Digite o nome do funcionário: "))
salario_atual = float(input(f"Digite o salário atual do funcionário [{nome}]: "))

if salario_atual == 0 or salario_atual <= 400.00:
    aumento = (salario_atual * 0.15) + salario_atual
    print(f"O salário anterior de [{nome}] no valor de R$ {salario_atual}, teve um aumento de 15%, portanto passou a ser de R${aumento}.")
elif salario_atual >= 400.01 or salario_atual <= 700.00:
    aumento = (salario_atual * 0.12) + salario_atual
    print(f"O salário anterior de [{nome}] no valor de R$ {salario_atual}, teve um aumento de 12%, portanto passou a ser de R${aumento}.")
elif salario_atual >= 700.01 or salario_atual <= 1000.00:
    aumento = (salario_atual * 0.10) + salario_atual
    print(f"O salário anterior de [{nome}] no valor de R$ {salario_atual}, teve um aumento de 10%, portanto passou a ser de R${aumento}.")
elif salario_atual >= 1000.01 or salario_atual <= 1800.00:
    aumento = (salario_atual * 0.07) + salario_atual
    print(f"O salário anterior de [{nome}] no valor de R$ {salario_atual} teve um aumento de 7%, portanto passou a ser de R${aumento}.")
elif salario_atual >= 1800.01 or salario_atual <= 2500.00:
    aumento = (salario_atual * 0.4) + salario_atual
    print(f"O salário anterior de [{nome}] no valor de R$ {salario_atual} teve um aumento de 4%, portanto passou a ser de R${aumento}.")
elif salario_atual > 2500:
    print(f"O salário de {nome} não teve aumento.")