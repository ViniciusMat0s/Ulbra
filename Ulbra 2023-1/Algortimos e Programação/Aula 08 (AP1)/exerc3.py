faturamento = float(input("Informe o faturamento da empresa: "))
custos = float(input("Informe os custos da empresa: "))
pis = faturamento * 0.0065
cofins = faturamento * 0.03
impostos = pis + cofins
lucro = faturamento - (impostos + custos)
print(f"O valor do imposto PIS é: R$ {pis}")
print(f"O valor de COFINS é: R$ {cofins}")
print(f"O lucro da empresa é de: R$ {lucro}")