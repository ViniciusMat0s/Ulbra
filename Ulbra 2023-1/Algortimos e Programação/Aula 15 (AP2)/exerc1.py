valor_parcela = 0
avista = 0.20
acrescimo = 0

valor = float(input("Digite o valor do carro: "))
parcelas = int(input(f"Qual a forma de pagamento?\n =========================== \n 0 = à vista (20% desconto) \n 6 = em 6x com 3% de juros \n 12 = em 12x com 6% de juros \n 18 = em 18x com 9% de juros \n 24 = em 24x com 12% de juros \n 30 = em 30x com 15% de juros \n 36 = em 36x com 18% de juros \n 42 = em 42x com 21% de juros \n 48 = em 48x com 24% de juros \n 54 = em 54x com 27% de juros \n 60 = em 60x com 30% de juros. \n ----------------------------\n Insira: "))

if parcelas == 0:
    acrescimo = valor * -0.20
    total = valor + acrescimo
    print(f"Você escolheu pagamento à vista e recebeu 20% de desconto, portanto, o valor final do carro é R$ {total}.")
elif parcelas == 6:
    acrescimo = valor * 0.03
    total = valor + acrescimo
    final = total / 6
    final = round(final,2)
    print(f"Você escolheu parcelamento em 6x, portanto, o valor final do carro é R$ {total}, com parcelas de R$ {final}.")
elif parcelas == 12:
    acrescimo = valor * 0.06
    total = valor + acrescimo
    final = total / 12
    final = round(final,2)
    print(f"Você escolheu parcelamento em 12x, portanto, o valor final do carro é R$ {total}, com parcelas de R$ {final}.")
elif parcelas == 18:
    acrescimo = valor * 0.09
    total = valor + acrescimo
    final = total / 18
    final = round(final,2)
    print(f"Você escolheu parcelamento em 18x, portanto, o valor final do carro é R$ {total}, com parcelas de R$ {final}.")
elif parcelas == 24:
    acrescimo = valor * 0.12
    total = valor + acrescimo
    final = total / 24
    final = round(final,2)
    print(f"Você escolheu parcelamento em 24x, portanto, o valor final do carro é R$ {total}, com parcelas de R$ {final}.")
elif parcelas == 30:
    acrescimo = valor * 0.15
    total = valor + acrescimo
    final = total / 30
    final = round(final,2)
    print(f"Você escolheu parcelamento em 30x, portanto, o valor final do carro é R$ {total}, com parcelas de R$ {final}.")
elif parcelas == 36:
    acrescimo = valor * 0.18
    total = valor + acrescimo
    final = total / 36
    final = round(final,2)
    print(f"Você escolheu parcelamento em 36x, portanto, o valor final do carro é R$ {total}, com parcelas de R$ {final}.")
elif parcelas == 42:
    acrescimo = valor * 0.21
    total = valor + acrescimo
    final = total / 42
    final = round(final,2)
    print(f"Você escolheu parcelamento em 42x, portanto, o valor final do carro é R$ {total}, com parcelas de R$ {final}.")
elif parcelas == 48:
    acrescimo = valor * 0.24
    total = valor + acrescimo
    final = total / 48
    final = round(final,2)
    print(f"Você escolheu parcelamento em 48x, portanto, o valor final do carro é R$ {total}, com parcelas de R$ {final}.")
elif parcelas == 54:
    acrescimo = valor * 0.27
    total = valor + acrescimo
    final = total / 54
    final = round(final,2)
    print(f"Você escolheu parcelamento em 54x, portanto, o valor final do carro é R$ {total}, com parcelas de R$ {final}.")
elif parcelas == 60:
    acrescimo = valor * 0.30
    total = valor + acrescimo
    final = total / 60
    final = round(final,2)
    print(f"Você escolheu parcelamento em 60x, portanto, o valor final do carro é R$ {total}, com parcelas de R$ {final}.")
else:
    print("Você inseriu uma opção inválida. O programa será encerrado.")