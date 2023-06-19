import random as r
import io

nome1 = input("\nDigite o nome do [Jogador 1]:\n")
nome2 = input("\nDigite o nome do [Jogador 2]:\n")
pts_jogador1 = []
pts_jogador2 = []
vit_j1 = 0
vit_j2 = 0

for i in range(10):
    jogador1 = r.randint(1,6)
    pts_jogador1.append(jogador1)
    print(f"{nome1} tirou {jogador1}.")
    #escrever os prints no txt com o .io (funcao a)

    jogador2 = r.randint(1,6)
    pts_jogador2.append(jogador2)
    print(f"{nome2} tirou {jogador1}.")

    if (jogador1 == jogador2):
        print("Houve um empate na rodada.") #botar quantos pontos cada um tirou e tem
    elif (jogador1 > jogador2):
        print(f"{nome1} venceu.")
        vit_j1 += 1
    else:
        print(f"{nome2} venceu.") #IMPLEMENTAR UM BOTÃO "JOGAR DADOS" PARA EXECUTAR A PROXIMA RODADA
        vit_j2 += 1

#somar no final e mostrar quem é o campeão e depois mostrar quantas vitórias tem cada jogador