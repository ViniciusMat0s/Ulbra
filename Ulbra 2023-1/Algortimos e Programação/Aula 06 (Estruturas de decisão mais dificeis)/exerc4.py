#4. Faça um programa para efetuar a leitura de quatro números e apresentar os números divisíveis por 2 e por 3.
num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))
num3 = float(input("Digite o terceiro valor: "))
num4 = float(input("Digite o quarto valor: "))
if num1 % 2 == 0 and num1 % 3 == 0:
    print(f"O número {num1} é divisível por 2 e por 3.")
elif num1 % 2 == 0:
    print(f"O número {num1} é divisível por 2.")
elif num1 % 3 == 0:
    print(f"O número {num1} é divisível por 3.")
else:
    print(f"O número {num1} não é divisível.")

if num2 % 2 == 0 and num2 % 3 == 0:
    print(f"O número {num2} é divisível por 2 e por 3.")
elif num2 % 2 == 0:
    print(f"O número {num2} é divisível por 2.")
elif num2 % 3 == 0:
    print(f"O número {num2} é divisível por 3.")
else:
    print(f"O número {num2} não é divisível.")

if num3 % 2 == 0 and num3 % 3 == 0:
    print(f"O número {num3} é divisível por 2 e por 3.")
elif num3 % 2 == 0:
    print(f"O número {num3} é divisível por 2.")
elif num3 % 3 == 0:
    print(f"O número {num3} é divisível por 3.")
else:
    print(f"O número {num3} não é divisível.")

if num4 % 2 == 0 and num4 % 3 == 0:
    print(f"O número {num4} é divisível por 2 e por 3.")
elif num4 % 2 == 0:
    print(f"O número {num4} é divisível por 2.")
elif num4 % 3 == 0:
    print(f"O número {num4} é divisível por 3.")
else:
    print(f"O número {num4} não é divisível.")