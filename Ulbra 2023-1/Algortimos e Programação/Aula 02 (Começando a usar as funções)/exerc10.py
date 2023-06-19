#Faça um algoritmo para calcular a área de um triângulo, exibindo o resultado. A base e a altura são dados que devem ser lidos como entrada.
piramide_altura = input("Qual a altura do triângulo? ")
piramide_altura = float(piramide_altura)
piramide_base = input("Qual o tamanho da base do triângulo? ")
piramide_base = float(piramide_base)
area = piramide_altura * piramide_base / 2
print("A área do seu triângulo é " +str(area))