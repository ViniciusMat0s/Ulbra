import random

def lancar_dado():
    return random.randint(1, 6)

def obter_vencedor(pontuacoes):
    if pontuacoes[0] > pontuacoes[1]:
        return "Jogador 1"
    elif pontuacoes[1] > pontuacoes[0]:
        return "Jogador 2"
    else:
        return "Empate"

def imprimir_resultados(resultados):
    print("=== Resultados das Rodadas ===")
    for rodada, resultado in enumerate(resultados, 1):
        print(f"Rodada {rodada}: Jogador 1: {resultado[0]}, Jogador 2: {resultado[1]}")
    print("=============================")

# Inicialização das variáveis
resultados = []
pontuacoes = [0, 0]

# Loop para simular as 10 rodadas
for rodada in range(1, 11):
    print(f"=== Rodada {rodada} ===")
    jogador1 = lancar_dado()
    jogador2 = lancar_dado()
    print(f"Jogador 1: {jogador1}")
    print(f"Jogador 2: {jogador2}")
    
    resultados.append((jogador1, jogador2))
    
    if jogador1 > jogador2:
        pontuacoes[0] += 1
        print("Jogador 1 venceu a rodada!")
    elif jogador2 > jogador1:
        pontuacoes[1] += 1
        print("Jogador 2 venceu a rodada!")
    else:
        print("Empate!")
    
    print("===================")

# Imprimir resultados das rodadas
imprimir_resultados(resultados)

# Verificar o vencedor
vencedor = obter_vencedor(pontuacoes)

print(f"Total de pontos - Jogador 1: {pontuacoes[0]}, Jogador 2: {pontuacoes[1]}")
print(f"Vencedor: {vencedor}")
