#2-  Faça um programa para criar uma lista de compras de mercadorias. Ela deve possuir um "menu" com as opções de adicionar, 
#alterar, remover, listar e sair. Deve criar uma função para cada uma  das quatro primeiras opções do menu.

#ALGORÍTMO DO TDE 17.

lista = []

def exibir_menu():
    print("\nMENU:\n")
    print("1. Adicionar item à lista")
    print("2. Alterar item da lista")
    print("3. Remover item da lista")
    print("4. Listar itens da lista")
    print("\n5. Sair")

def adicionar_item():
    item = input("Digite o nome do item a ser adicionado: ")
    lista.append(item)
    print("\nItem adicionado à lista de compras.\n")

def alterar_item():
    indice = int(input("Digite o índice do item a ser alterado: "))
    if indice < 0 or indice >= len(lista):
        print("\nÍndice inválido.\n")
    else:
        novo_item = input("Digite o novo nome do item: ")
        lista[indice] = novo_item
        print("\nItem alterado.\n")

def remover_item():
    indice = int(input("Digite o índice do item a ser removido: "))
    if indice < 0 or indice >= len(lista):
        print("\nÍndice inválido.\n")
    else:
        item_removido = lista.pop(indice)
        print("\nItem removido:\n", item_removido)

def listar_itens():
    print("Lista de compras:")
    if len(lista) == 0:
        print("\nA lista está vazia.\n")
    else:
        for i, item in enumerate(lista):
            print(f"{i}. {item}")

while True:
    exibir_menu()
    opcao = input("\nDigite a opção desejada:\n")

    if opcao == "1":
        adicionar_item()
    elif opcao == "2":
        alterar_item()
    elif opcao == "3":
        remover_item()
    elif opcao == "4":
        listar_itens()
    elif opcao == "5":
        print("\nSaindo do programa.\n")
        break
    else:
        print("\nOpção inválida. Tente novamente.\n")
