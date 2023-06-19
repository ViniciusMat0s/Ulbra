#iterando uma lista
planetas = ['Terra', 'Jupter', 'Marte', 'Vênus', 'Saturno','Netuno']

for p in planetas:
    print(p)
    if p == 'Vênus':
        planetas.append('Urano')
        #print('Você descubriu um planeta')

#preenchendo uma lista

nomes = []


for i in range(3):
    nome = input('Digite o nome \n')
    nomes.append(nome)

for n in nomes:
    if (n == 'Ana'):
        print('Você encontou uma Ana.')
    