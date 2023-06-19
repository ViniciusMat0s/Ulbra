salFem=0
salMas=0
salGrupo=0
sal1200=0
maiorSal = 0
numM = 0
numF=0
while True:
    #coletando dados
    idade = int(input("Qual a sua idade (digite um número negativo para parar): "))
    if idade < 0:
        break
    sexo = input("Digite seu sexo(M ou F): ").upper()
    
    if sexo != "M":
        if sexo != "F":
            print("Digite um sexo válido 'M' ou 'F'")
            continue
    sal = float(input("Qual é seu salario: "))

    #somando dados
    if sexo =="M":
        salMas+=sal
        numM += 1
    if sexo == "F":
        salFem += sal
        numF += 1
        if sal <=1200:
            sal1200 +=1
    salGrupo += sal
    if sal > maiorSal:
        maiorSal = sal
        idadeRica=idade
        sexoRica = sexo

#médias salariais
if numM > 0:
    mediaMas = salMas /numM
if numF >0:
    mediaFem = salFem / numF
if numF > 0 and numM > 0:
    media = (salFem + salMas)/(numF + numM)

#prints
print(f"A média salárial do grupo é R${media:.2f}")
print(f"A média salárial Masculina é R${mediaMas:.2f}")
print(f"A média salárial feminina é R${mediaFem:.2f}")
print(f"A quantidade de mulheres que recebem salario até R$1200,00 é {sal1200} ")
print(f"O sexo da pessoa que recebe o mairo salário é {sexoRica}, e a idade é {idadeRica}")

