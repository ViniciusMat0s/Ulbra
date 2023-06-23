import random as r
import datetime as dt

data_inicio = dt.datetime.now()
tentativas = 0
num_sorteado = r.randint(0, 20)
a = "-="

while tentativas < 3:
    num_escolhido = int(input("\nEscolha um número de 0 a 20:\t"))
    if num_escolhido >= 0 and num_escolhido <= 20:
        if num_escolhido == num_sorteado:
            print(f"\n{a * 19}\n\tParabéns, você ganhou!\n{a * 19}\n")
            break
        elif num_escolhido < num_sorteado:
            print(f"Tente um número maior.")
            tentativas += 1
        else:
            print(f"Tente um número menor.")
            tentativas += 1
    else:
        print("\nNúmero inválido, digite um número de 0 a 20.")
else:
    print(f"\n{a * 24}\n\tVocê perdeu, finalizando o jogo.\n\t\tResposta: [{num_sorteado}]\n{a * 24}\n")

data_fim = dt.datetime.now()
tempo_gasto = data_fim - data_inicio
print(f"O tempo gasto foi de: {tempo_gasto} ms\n")