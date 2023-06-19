#Faça um algoritmo para ler dois inteiros (variáveis A e B) e efetuar as operações de adição, subtração, 
#multiplicação e divisão de A por B apresentando ao final os quatro resultados obtidos.
numero1 = input("Digite um número inteiro: ")
numero1 = float(numero1)
numero2 = input("Digite outro número inteiro: ")
numero2 = float(numero2)
soma = numero1 + numero2 #declarando a variável soma que recebe a soma de dois números.
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2
exponenciacao = numero1 ** numero2
resto = numero1 % numero2
print("A soma dos números é " + str(soma)) #função print para apresentar uma string e o valor da variável soma convertido
print("A subtração dos números é " + str(subtracao))
print("A multiplicação dos números é " + str(multiplicacao))
print("A divisão dos números é " + str(divisao))
print("O número " + str(numero1) + " na potência " + str(numero2) + " é " + str(exponenciacao))
print("O resto da divisão é " + str(resto))