#4. Escreva um programa que verifique se uma letra é vogal ou consoante.
letra = input("Insira uma letra: ")
if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u" or letra == "A" or letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
    print(f"A letra {letra} inserida é uma vogal.")
else:
    print(f"A letra {letra} inserida é uma consoante.")