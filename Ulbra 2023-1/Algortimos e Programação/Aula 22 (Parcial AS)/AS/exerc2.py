import random as r
import io

nome1 = input("\nDigite o nome do [Jogador 1]:\n")
nome2 = input("\nDigite o nome do [Jogador 2]:\n")
pts_jogador1 = []
pts_jogador2 = []
vit_j1 = 0
vit_j2 = 0
empates = 0
a = "-="

for i in range(10):
    jogador1 = r.randint(1,6)
    pts_jogador1.append(jogador1)
    print(a*15)
    print(f"\n[Rodada {i+1}]")
    print(f"{nome1} tirou {jogador1}.")
    with io.open('arquivo.txt', 'a') as file:
        file.write(f'\n[Rodada {i+1}] {nome1} tirou {jogador1}.')

    jogador2 = r.randint(1,6)
    pts_jogador2.append(jogador2)
    print(f"{nome2} tirou {jogador1}.\n")
    with io.open('arquivo.txt', 'a') as file:
        file.write(f'\n[Rodada {i+1}] {nome2} tirou {jogador2}.')

    if (jogador1 == jogador2):
        print("Houve um empate na rodada.\n")
        with io.open('arquivo.txt', 'a') as file:
            file.write(f'\n[Rodada {i+1}] Houve um empate na rodada.')
    elif (jogador1 > jogador2):
        print(f"{nome1} venceu a rodada.\n")
        with io.open('arquivo.txt', 'a') as file:
            file.write(f'\n[Rodada {i+1}] {nome1} venceu a rodada.')
    else:
        print(f"{nome2} venceu a rodada.\n")
        with io.open('arquivo.txt', 'a') as file:
            file.write(f'\n[Rodada {i+1}] {nome2} venceu a rodada.')

    totalj1 = sum(pts_jogador1)
    totalj2 = sum(pts_jogador2)

if totalj1 > totalj2:
    vit_j1=+1
    print(a*15)
    print(f"{nome1} venceu o jogo, parabéns!")
    with io.open('arquivo.txt', 'a') as file:
        file.write(f'\n[Rodada {i+1}] {nome1} venceu o jogo. parabéns!.')
    print(f"\n\t[Placar final]:\n\n{nome1}: {totalj1}\n{nome2}: {totalj2}\n")
    with io.open('arquivo.txt', 'a') as file:
        file.write(f'\n[Placar final]:\n\n{nome1}: {totalj1}\n{nome2}: {totalj2}\n')
elif totalj2 > totalj1:
    vit_j2=+1
    print(a*15)
    print(f"{nome2} venceu o jogo, parabéns!")
    with io.open('arquivo.txt', 'a') as file:
        file.write(f'\n[Rodada {i+1}] {nome2} venceu o jogo. parabéns!.')
    print(f"\n\t[Placar final]:\n\n{nome1}: {totalj1}\n{nome2}: {totalj2}\n")
    with io.open('arquivo.txt', 'a') as file:
        file.write(f'\n[Placar final]:\n\n{nome1}: {totalj1}\n{nome2}: {totalj2}\n')
elif totalj1 == totalj2:
    empates=+1
    print(a*15)
    print(f"O jogo empatou!")
    with io.open('arquivo.txt', 'a') as file:
        file.write(f'\nO jogo empatou!')
    print(f"\n\t[Placar final]:\n\n{nome1}: {totalj1}\n{nome2}: {totalj2}\n")
    with io.open('arquivo.txt', 'a') as file:
        file.write(f'\n[Placar final]:\n\n{nome1}: {totalj1}\n{nome2}: {totalj2}\n')

print(f"\n[Placar do jogo]:\n\n{nome1}: {vit_j1}\n{nome2}: {vit_j2}\nEmpates: {empates}\n")
with io.open('arquivo.txt', 'a') as file:
    file.write(f'\n[Placar do jogo]:\n\n{nome1}: {vit_j1}\n{nome2}: {vit_j2}\nEmpates: {empates}\n')
print(a*15)

#somar no final e mostrar quem é o campeão e depois mostrar quantas vitórias tem cada jogador