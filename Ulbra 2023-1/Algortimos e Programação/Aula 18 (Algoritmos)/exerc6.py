#6- Faça um programa que leia uma frase e apresente o número de vogais presentes na frase. O número de vogais devem vir do retorno da função.

def vogal(frase):
    frase = frase.lower()
    frase = frase.strip()
    print(frase)
    print("\nNúmero de vogais presentes na frase:")
    print("\nA >> ",frase.count("a"))
    print("E >> ",frase.count("e"))
    print("I >> ",frase.count("i"))
    print("O >> ",frase.count("o"))
    print("U >> ",frase.count("u"))

frase = input("\nDigite uma frase:\n")

vogal(frase)