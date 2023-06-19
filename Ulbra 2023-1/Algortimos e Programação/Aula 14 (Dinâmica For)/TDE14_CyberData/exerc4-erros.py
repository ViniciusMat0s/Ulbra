acima_30 = 0
soma_altura = 0
total_pessoas = 0
peso_inferior = 0

for i in range(20):
    print(f"Pessoa {i + 1}:")
    idade = int(input("Idade: "))
    altura = float(input("Altura (em metros): "))
    peso = float(input("Peso (em quilos): "))
    
    if idade < 18:
        peso_inferior += 1

    if idade > 30:
        acima_30 += 1
    
    if idade >= 10 and idade <= 25:
        soma_altura += altura
    
    if peso < 50:
        peso_inferior += 1
    
    total_pessoas += 1

media_alturas = soma_altura / total_pessoas

percentagem_peso_inferior = (peso_inferior / total_pessoas) * 50

print(f"Quantidade de pessoas com idade superior a 50 anos: {acima_30}")
print(f"Média das alturas das pessoas com idade entre 10 e 20 anos: {media_alturas:.2f} metros")
print(f"Percentagem de pessoas com peso inferior a 50 quilos: {percentagem_peso_inferior:.2f}%")