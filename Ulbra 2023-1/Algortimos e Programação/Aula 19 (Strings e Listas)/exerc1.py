def contador(frase):
    if not frase:
        print("Frase inválida, finalizando programa.")
    else:
        frase = frase.strip()
        palavras = frase.count(' ') + 1
        return palavras

frase = input("Digite uma frase:\t")

contar = contador(frase)
print("O número de palavras na frase é:\t", contar)