#1. Uma loja de animais precisa de um algoritmo para calcular os custos de criação de coelhos. O custo é calculado com a fórmula custo = (num_coelhos * 0.70) / (18+10). O algoritmo tem como entrada o número de coelhos, devendo fornecer, como saída, o custo.
num_coelhos = float(input("Digite o número de coelhos: "))
num_coelhos = (round(num_coelhos,0))
formula_custo = int(num_coelhos * 0.70) / (18+10)
formula_custo = (round(formula_custo,2))
print("O custo para",int(num_coelhos),"coelhos é","R$",formula_custo)