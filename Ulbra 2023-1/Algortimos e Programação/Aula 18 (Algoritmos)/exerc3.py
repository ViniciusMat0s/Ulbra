#3- Escreva um programa que solicite ao usuário que digite uma frase e, em seguida, substitua todas as ocorrências 
#de uma determinada letra por outra letra especificada pelo usuário. Informe no final a frase modificada.

def substituir_letra(frase):
    frase = frase.replace(original,trocar)
    print(f"\nFrase modificada:\n{frase}\n")

frase = input("\nDigite a frase:\n")
original = input("\nDigite a letra que você quer modificar.\n")
trocar = input("\nDigite a nova letra.\n")

substituir_letra(frase)