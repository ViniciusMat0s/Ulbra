num = 5
tentativas = 3
while tentativas > 0:
    resposta = int(input("Digite num número. "))
    if resposta == num:
        print("Acertou!")
        tentativas = 0
    else:
        print("Errou!")
        tentativas -= 1