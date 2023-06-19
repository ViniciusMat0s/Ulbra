#1. O hotel Pica-Pau cobra 50,00 Reais a diária e mais uma taxa de serviços. A taxa de serviços é de:
#1,50 por dia, se número de diárias <15
#1,00 por dia, se número de diárias =15
#0,50 por dia, se número de diárias >15
#Faça um programa que lê o número de diárias e calcula o total a ser pago pelo cliente.
num_diarias = int(input("Digite o número de diárias: "))
if num_diarias <15:
    print(f"O total a ser pago é: R${(50.00 * num_diarias) + (num_diarias * 1.50)}")
if num_diarias ==15:
    print(f"O total a ser pago é: R${(50.00 * num_diarias) + (num_diarias * 1.00)}")
if num_diarias >15:
    print(f"O total a ser pago é: R${(50.00 * num_diarias) + (num_diarias * 0.50)}")