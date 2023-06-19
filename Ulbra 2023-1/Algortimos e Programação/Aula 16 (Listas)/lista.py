numeros = [0,7,4,12,434,20]
#alterando elementos
print(numeros)
numeros[0] = 21
print(numeros)
numeros[4] = 3
print(numeros)
numeros[-1] = 1 #alterando último elemento
print(numeros)
#Inserindo elemento na última posição da lista
numeros.append(100)
print(numeros)
#inserindo pelo índice
numeros.insert(3, 450)
print(numeros)
#Excluindo elementos
numeros.pop() #Exlui o último
print(numeros)
excluido = numeros.pop(1) #Exclui pelo valor do índice
print(numeros)
print(excluido)
numeros.remove(1000)
print(numeros)