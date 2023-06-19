idade_sup_30 = 0
media_altura_idade_10_25 = 0
media_peso_menor_idade = 0
peso_inferior_50 = 0

for i in range(20):
    idade = int(input("Informe a idade da pessoa : "))
    altura = float(input("Informe a altura da pessoa : "))
    peso = float(input("Informe o peso da pessoa : "))
    
    if idade > 30:
        idade_sup_30 += 1
    
    if 10 <= idade <= 25:
        media_altura_idade_10_25 += altura
    
    if idade < 18:
        media_peso_menor_idade += peso
    
    if peso < 50:
        peso_inferior_50 += 1
        
if idade_sup_30 > 0:
    print(f"Quantidade de pessoas com idade superior a 30 anos: {idade_sup_30}")
   
if media_altura_idade_10_25 > 0:
    media_altura_idade_10_25 /= idade_sup_30
    print(f"Média das alturas das pessoas com idade entre 10 e 25 anos: {media_altura_idade_10_25}")
    
if media_peso_menor_idade > 0:
    media_peso_menor_idade /= (20 - idade_sup_30)
    print(f"Média de peso das pessoas menores de idade: {media_peso_menor_idade}")


if peso_inferior_50 > 0:
    porcentagem_peso_inferior_50 = (peso_inferior_50 / 20) * 100
    print(f"Porcentagem de pessoas com peso inferior a 50 quilos entre todas as pessoas analisadas: {porcentagem_peso_inferior_50}%")
