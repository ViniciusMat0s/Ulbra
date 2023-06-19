#1. Faça um programa que receba um número, calcule e mostre a tabuada desse número.
i = 0
tabuada = int(input("Digite um número: "))

while i <= 10:
    print(f"{tabuada} x {i} = {tabuada*i}")
    i = i + 1