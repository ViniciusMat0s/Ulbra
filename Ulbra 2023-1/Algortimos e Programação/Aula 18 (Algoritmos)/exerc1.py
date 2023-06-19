#1- Escreva um programa que solicite ao usuário que digite um texto e conte o número de caracteres no texto e exiba o resultado na tela. Os espaços em branco não devem ser contados.

def contagem(texto):
    texto = texto.strip()
    texto = texto.replace(" ","")
    print(f"\nO texto que você digitou possui {len(texto)} caracter(es) sem espaçamento.\n")

texto = input("\nDigite o texto:\n")

contagem(texto)