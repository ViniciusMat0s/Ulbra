#4- Faça um programa que leia o nome completo de um autor famoso e uma frase conhecida. Imprimir no final a mensagem no seguinte 
#formato: ‘Descarte, René. Penso logo existo’. Caso tenha mais que dois nomes considere apenas o primeiro e o último.

def formatacao(nome, frase):
    nomes = nome.split()
    primeiro = nomes[0]
    ultimo = nomes[-1]
    formatada = f"{ultimo}, {primeiro}. {frase}"
    print(formatada)

nome = input("\nDigite o nome completo do autor:\n")
frase = input("\nDigite a frase do autor:\n")

formatacao(nome, frase)