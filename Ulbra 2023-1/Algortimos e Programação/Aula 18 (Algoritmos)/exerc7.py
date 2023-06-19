#7- Faça um programa que leia dois números do usuário e exiba o seguinte menu de opções: 
#(1 - Somar, 2 - Subtrair, 3 - Multiplicar, 4 - Dividir, 5 - Sair) e apresente o resultado escolhido na tela. Crie uma função para cada operação, lembre-se que não se divide número por 0. 

def exibir_menu():
    print("\nMENU:\n")
    print("1. Adicionar item à lista")
    print("2. Alterar item da lista")
    print("3. Remover item da lista")
    print("4. Listar itens da lista")
    print("\n5. Sair\n")

def somar(n1, n2):
    soma = n1 + n2
    print("\nOPÇÃO SELECIONADA: [Somar]")
    print(f"A soma dos números é: {soma}")

def subtrair(n1, n2):
    subtracao = n1 - n2
    print("\nOPÇÃO SELECIONADA: [Subtrair]")
    print(f"A subtração dos números é: {subtracao}")

def multiplicar(n1, n2):
    multiplicacao = n1 * n2
    print("\nOPÇÃO SELECIONADA: [Multiplicar]")
    print(f"A multiplicação dos números é: {multiplicacao}")

def dividir(n1, n2):
    divisao = n1 / n2
    print("\nOPÇÃO SELECIONADA: [Dividir]")
    print(f"A divisão dos números é: {divisao}")

def sair():
    print("\nOPÇÃO SELECIONADA: [Sair]")
    print("Saindo do programa.")

while True:
    n1 = float(input("\nDigite o primeiro número:\t"))
    n2 = float(input("Digite o segundo número:\t"))
    exibir_menu()
    opcao = int(input("Digite uma opção. (1 - Somar, 2 - Subtrair, 3 - Multiplicar, 4 - Dividir, 5 - Sair):\t"))
    if opcao == 1:
        somar(n1,n2)
    elif opcao == 2:
        subtrair(n1,n2)
    elif opcao == 3:
        multiplicar(n1,n2)
    elif opcao == 4:
        dividir(n1,n2)
    elif opcao == 5:
        sair
        break
    else:
        print("\nOpção inválida. Tente novamente.\n")
