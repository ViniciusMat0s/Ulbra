# 9. Faça um algoritmo que leia o número da conta bancária e o saldo de um cliente. Caso a conta tenha saldo negativo, o programa deve enviar a seguinte mensagem: CONTA ESTOURADA, caso contrário CONTA NORMAL.
conta = float(input("Digite o número de sua conta bancária: "))
saldo = float(input("Digite seu saldo: "))
if saldo <= 0:
    print("CONTA ESTOURADA")
else:
    print("CONTA COMUM")