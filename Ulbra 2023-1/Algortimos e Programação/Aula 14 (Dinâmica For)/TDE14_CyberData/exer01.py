count = 1
idade = 0
peso = 0
altura = 0
olhos = "F"
cabelo = "F"
soma_media = 0
total_media = 0
olhos_azuis = 0
req1 = 0 #idade>50 e peso<60
req2 = 0 #ruivos sem olhos azuis

while count < 21:    
    if idade <= 0:
        print(f"Pessoa nº {count}: ")
        idade = float(input("\n Digite a sua idade: "))
        if idade <= 0:
            print(f"\n Idade inválida, digite novamente: ")
            continue
    if peso <= 0:
        peso = float(input("\n Digite o seu peso em Kg: "))
        if peso <= 0:   
            print("\n Peso inválido, digite novamente: ")
            continue
    if altura <= 0:
        altura = float(input("\n Digite sua altura em M: "))
        if altura <= 0:
            print("\n Altura inválida, digite novamente: ")
            continue
    if olhos == "F":
        olhos = str(input("\n Digite a cor dos seus olhos (A-azul, P-preto, V-verde e C-castanho): "))
        if olhos == "A" or olhos == "P" or olhos == "V" or olhos == "C" or olhos == "a" or olhos == "p" or olhos == "v" or olhos == "c":
            olhos = olhos
        else:
            olhos = "F"
            print("\n Cor dos olhos inválida, digite novamente: ")
            continue
    if cabelo == "F":
        cabelo = str(input("\n Digite a cor do seu cabelo (P-preto, C-castanho, L-louro e R-ruivo): "))
        if cabelo == "P" or cabelo == "C" or cabelo == "L" or cabelo == "R" or cabelo == "p" or cabelo == "c" or cabelo == "l" or cabelo == "r":
            cabelo = cabelo
        else:
            cabelo = "F"
            print("\n Cor do cabelo inválida, digite novamente: ")
            continue            
    if idade > 50 and peso < 60:
        req1 +=1
    if altura < 1.5:
        soma_media += 1
        total_media += idade
    if olhos == "a" or olhos == "A":
        olhos_azuis += 1
    else:
        if cabelo == "R" or cabelo == "r":
            req2 += 1
    
    idade = 0
    peso = 0
    altura = 0
    olhos = "F"
    cabelo = "F"
    count += 1
    
if soma_media == 0:
    media = soma_media   
else:
    media = total_media / soma_media

percentagem = (olhos_azuis * 100) / (20)

print(f"\n A quantidade de pessoas com idade superior a 50 anos e peso inferior a 60 quilos: {req1}.")
if soma_media == 0:
    print("\n Não há pessoas com altura inferior a 1,50 metro.")
else:
    print(f"\n A média das idades das pessoas com altura inferior a 1,50 metro: {media}.")
print(f"\n A percentagem de pessoas com olhos azuis entre todas as pessoas analisadas: {percentagem}%")
print(f"\n A quantidade de pessoas ruivas e que não possuem olhos azuis: {req2}.")