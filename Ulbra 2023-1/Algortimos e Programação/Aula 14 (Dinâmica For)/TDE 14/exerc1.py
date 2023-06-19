idade_50_peso_60 = 0
media_idade_altura = 0
pessoas_olhos_azuis = 0
pessoasruivas_olhosazuis = 0

for i in range(4):
    idade = int(input("Informe a idade da pessoa: "))
    peso = float(input("Informe o peso da pessoa: "))
    altura = float(input("Informe a altura da pessoa: "))
    olhos = input("Informe a cor dos olhos da pessoa (A-azul, P-preto, V-verde e C-castanho): ")
    cabelos = input("Informe a cor dos cabelos da pessoa (P-preto, C-castanho, L-louro e R-ruivo): ")
    
    if idade > 50 and peso < 60:
        idade_50_peso_60 += 1
    
    if altura < 1.50:
        media_idade_altura += idade 
    
    if olhos == "A":
        pessoas_olhos_azuis += 1 
    
    if cabelos == "R" and olhos != "A":
        pessoasruivas_olhosazuis += 1 
        
if idade_50_peso_60 > 0:
    print(f"Quantidade de pessoas com idade superior a 50 anos e peso inferior a 60 quilos: {idade_50_peso_60}")
else:
    print("Não há pessoas com idade superior a 50 anos e peso inferior a 60 quilos.")
    
if media_idade_altura > 0: 
    media_idade_altura /= 20 
    print(f"Média das idades das pessoas com altura inferior a 1,50 metro: {media_idade_altura}") 
else:
    print("Não há pessoas com altura inferior a 1,50 metro.")
    
if pessoas_olhos_azuis > 0:
    percentagem_pessoas_olhos_azuis = (pessoas_olhos_azuis / 20) * 100
    print(f"Percentagem de pessoas com olhos azuis entre todas as pessoas analisadas: {percentagem_pessoas_olhos_azuis}%")
else:
    print("Não há pessoas com olhos azuis.")
    
if pessoasruivas_olhosazuis > 0: 
    print(f"Quantidade de pessoas ruivas e que não possuem olhos azuis: {pessoasruivas_olhosazuis}") 
else:
    print("Não há pessoas ruivas e que não possuem olhos azuis.")