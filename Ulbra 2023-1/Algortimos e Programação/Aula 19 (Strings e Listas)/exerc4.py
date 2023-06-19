#4 - Faça um programa que leia a pontuação de um números de times determinado pelo usuário (o número de times deve ser maior que 4 e menor que 25). 
#Ao final da leitura, o programa deve listar as três maiores pontuações, a pontuação do time campeão e a pontuação do último colocado. Não aceite pontuações negativas

#EU NÃO ESTAVA CONSEGUINDO ADICIONAR NA LISTA E ORDENAR O MAIOR COM AS FUNÇÕES, ENTÃO PROCUREI NO CHATGPT E ADAPTEI MEU CÓDIGO AO MODELO.

def pontos(times):
    pontuacoes = []
    for i in range(times):
        pontuacao = int(input(f"Digite a pontuação do time {i}: "))
        if pontuacao >= 0:
            pontuacoes.append(pontuacao)
        else:
            print("\nPontuação inválida, tente novamente:\n")
    return pontuacoes

def tabela():
    times = int(input("Digite o número de times participantes (Min. 5 e Max. 24): "))
    while times < 5 or times > 24:
        print("\nNúmero de times inválido, tente novamente:\n")
        times = int(input("Digite o número de times participantes (Min. 5 e Max. 24): "))

    pontuacoes = pontos(times)
    classificacao = sorted(pontuacoes, reverse=True)

    print("\nOs três primeiros colocados são:")
    for i in range(3):
        print(classificacao[i])

    print("\nPontuação do campeão:", classificacao[0])
    print("Pontuação do lanterna:", classificacao[-1])

tabela()