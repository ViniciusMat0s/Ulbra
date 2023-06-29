import random

def jogo_de_dados():
    jogadores = ["Jogador 1", "Jogador 2"]
    vitorias = [0, 0]

    for _ in range(10):
        resultados = []
        for i in range(2):
            resultado = random.randint(1, 6)
            resultados.append(resultado)
            print(f"{jogadores[i]}: {resultado}")

        if resultados[0] > resultados[1]:
            vitorias[0] += 1
            print(f"{jogadores[0]} venceu a rodada!\n")
        elif resultados[1] > resultados[0]:
            vitorias[1] += 1
            print(f"{jogadores[1]} venceu a rodada!\n")
        else:
            print("Empate!\n")

    print("--- Contador de Vitórias ---")
    print(f"{jogadores[0]}: {vitorias[0]} vitórias")
    print(f"{jogadores[1]}: {vitorias[1]} vitórias")

jogo_de_dados()
