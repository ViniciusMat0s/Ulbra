#meu primeiro programa

numero1 = 10 #declarando variável do tipo inteiro e atribuindo o valor 10.
numero2 = 5 #declarando variável do tipo inteiro e atribuindo valor 3.
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

nome = input("Digite seu nome.")
idade = input("Digite sua idade.")
print(str(nome) + " sua idade é " + str(idade)) #mostra na tela o nome e a idade do usuário