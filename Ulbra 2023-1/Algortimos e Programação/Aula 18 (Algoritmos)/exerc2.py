#2- Escreva um programa que solicite ao usuário que digite uma palavra e verifique se ela é um palíndromo. Um palíndromo é uma palavra que pode
#ser lida da mesma forma tanto da esquerda para a direita quanto da direita para a esquerda. O programa deve exibir "É um palíndromo" ou "Não é um palíndromo".

def eh_palindromo(string):
    return string == string[::-1]

palavra = input("\nDigite uma palavra:\n")

if eh_palindromo(palavra):
    print("\nÉ um palíndromo.\n")
else:
    print("\nNão é um palíndromo.\n")