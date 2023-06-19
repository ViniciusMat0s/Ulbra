#3. Matheus e Tamires

x = 1
soma = 0

while x <= 10:
    nota = int(input("Digite sua nota."))
    soma = soma + nota
    x += 1 
media = soma / 10

if nota >= 0 and nota <=10:
    print(f"A média das notas dos alunos é {media}.")
    
else:
    print(f"A nota é inválida.")