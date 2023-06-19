#9.Faça um algoritmo que leia dois números inteiros (x e y), e calcule o quociente e o resto da divisão de x por y e escreva os resultados.
x = int(input("Digite um número: "))
y = int(input("Digite outro número: "))
quociente = x / y
resto = quociente % quociente
resto = (round(resto,2))
print("O quociente é:",quociente,"e o resto da divisão é:",resto)