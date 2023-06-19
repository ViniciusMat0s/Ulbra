#3 - Faça um programa para verificar se uma data é válida. O Programa deve conter uma função que verifica a data com três parâmetros (dia, mês e ano)
#e o retorno da função de ser um booleano, true quando data válida, false para inválida. Solicite a data do usuário e o informe o resultado.

#EXERCÍCIO MODIFICADO DA AP1

def testador(dia, mes, ano):
    if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
        if dia > 31 or dia < 1:
            False
            print(False)
        else:
            True
            print(True)
    elif (mes == 4 or mes == 6 or mes == 9 or mes == 11):
        if dia > 30 or dia < 1:
            False
            print(False)
        else:
            True
            print(True)
    else:
        if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
            if dia > 29 or dia < 1:
                False
                print(False)
            else:
                True
                print(True)
        else:
            if dia > 28 or dia < 1:
                False
                print(False)
            else:
                True
                print(True)

dia = int(input("\nInsira um dia:\t"))
mes = int(input("Insira um mês:\t"))
ano = int(input("Insira um ano:\t"))

testador(dia, mes, ano)