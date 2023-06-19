#6. Faça um algoritmo que calcule e escreva o preço final de um computador, sendo fornecido o preço de fábrica. O preço final do computador é calculado com base nos adicionais de: 30 % de imposto e 10 % de revenda sobre o preço de fábrica.
preço_fabrica = float(input("Insira o preço de fábrica do computador: "))
valor_imposto = (preço_fabrica * 1.3)
valor_revenda = (valor_imposto * 1.1)
valor_final = (round(valor_revenda,2))
print("O preço final do computador, incluindo impostos, é de: R$",valor_final)