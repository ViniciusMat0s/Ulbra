dia = int(input("Insira um dia: "))
mes = int(input("Insira um mês: "))
ano = int(input("Insira um ano: "))
if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
    if dia > 31 or dia < 1:
        print("A data inserida é inválida.")
    else:
        print("Data válida.")
elif (mes == 4 or mes == 6 or mes == 9 or mes == 11):
    if dia > 30 or dia < 1:
        print("A data inserida é inválida.")
    else:
        print("Data válida.")
else:
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        if dia > 29 or dia < 1:
            print("A data inserida é inválida.")
        else:
            print("Data válida.")
    else:
        if dia > 28 or dia < 1:
            print("A data inserida é inválida.")
        else:
            print("Data válida.")