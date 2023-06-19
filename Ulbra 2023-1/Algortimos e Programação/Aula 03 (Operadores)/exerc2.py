#2. Faça um algoritmo para calcular o valor de lucro que um vendedor tem em um produto, com base em seu preço de custo e o preço de venda.
custo_produto = int(input("Insira o custo do produto: "))
venda_produto = int(input("Insira o valor de venda do produto: "))
lucro = venda_produto - custo_produto
print("O lucro total do produto é de R$",lucro)