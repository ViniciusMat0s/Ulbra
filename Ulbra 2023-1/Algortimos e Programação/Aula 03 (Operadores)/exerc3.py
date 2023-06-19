#3. Faça um algoritmo que leia o preço de um produto e a quantidade comprada e exiba para o usuário o preço que ele tem que pagar pela compra.
preço_produto = float(input("Digite o preço do produto: "))
quantidade_produto = int(input("Qual a quantidade de produtos?"))
total = quantidade_produto * preço_produto
total = (round(total,2))
print("O valor total da compra foi R$",total)