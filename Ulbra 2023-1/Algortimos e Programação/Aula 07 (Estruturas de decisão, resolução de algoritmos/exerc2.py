#2. Escreva um programa que calcule o perímetro de um quadrado, dado o valor do lado.
lado = float(input("Digite o tamanho do lado (em metros): "))
perimetro = lado * 4
perimetro = round(perimetro, 2)
print(f"O perímetro do quadrado de lado {lado} é {perimetro} m.")