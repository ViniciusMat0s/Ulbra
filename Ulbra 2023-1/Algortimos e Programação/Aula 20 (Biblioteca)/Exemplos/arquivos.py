import io

with io.open("arquivo.txt", "w") as file: #Subescrever textos
    file.write("Olá, mundo!")

with io.open("arquivo.txt", "a") as file: #Acumular textos
    file.write("Olá, mundo!")

with io.open("arquivo.txt", "r") as file: #Ler o texto
    content = file.read()
    print(content[2]) #O 2 é a letra lida