#Faça um algoritmo que lê o número de um funcionário, seu número de horas trabalhadas e o valor que recebe por hora. O algoritmo deve calcular e mostrar o salário deste funcionário.
horas_trabalhadas = input("Informe seu tempo de trabalho em horas: ")
horas_trabalhadas = float(horas_trabalhadas)
horas_valor = input("Informe o valor ganho por hora trabalhada: R$ ")
horas_valor = float(horas_valor)
salario_dia = horas_valor * horas_trabalhadas
salario_dia = (round(salario_dia, 2))
salario_semanal = salario_dia * 7
salario_semanal = float(salario_semanal)
salario_mensal = salario_dia * 30
salario_mensal = float(salario_mensal)
print("O seu salário diário é de R$ " + str(salario_dia))
print("O seu salário semanal é de R$ " + str(salario_semanal))
print("O seu salário mensal é de R$ " + str(salario_mensal))
if (salario_mensal<1380.60):
    print("Você está sendo explorado!!!")