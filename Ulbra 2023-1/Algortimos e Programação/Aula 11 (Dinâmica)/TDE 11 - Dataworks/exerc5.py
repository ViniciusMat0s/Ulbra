#5. Thais, Luan e Yuri

nulo = 0
negativo = 0
positivo = 0
x = 1


while  x <=10:
    numero = float (input("Digite um número: "))
    
    if numero == 0:
        nulo += 1
    if numero < 0:
        negativo += 1
    if numero > 0:
        positivo += 1
    x += 1
    

      

print (f"Dentre os números digitados {nulo} são nulos, {negativo} são negativos, {positivo} são positivos. ")