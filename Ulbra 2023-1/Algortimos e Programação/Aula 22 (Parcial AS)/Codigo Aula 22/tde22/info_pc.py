import psutil
import platform
import cpuinfo
def info_so():
    sistema = platform.system()
    versao = platform.release()
    print(f'Sistema Operacional {sistema} {versao}')
def info_processador():  #Pegar com o módulo CPUInfo
    print('Processador')
def info_memoria(): #Pegar como o módul psutil
    print('Mémoria PC')
def info_armazenamento(): #Pegar como o módul psutil
    print('Armazenamento do PC')
print('Olá seja bem vindo ao programa de informações do PC.')
print('--x----Menu---x---')
print('1. Informações do Sistema Operacional')
print('2. Informações do Processador')
print('3. Informações da Memória RAM')
print('4. Informações do Armazenamento')
print('0. Sair')

while True:
    opcao = int(input('Digite o número da opção desejada: '))
    if opcao == 1:
        info_so()
    elif opcao == 2:
        info_processador()
    elif opcao == 3:
        info_memoria()
    elif opcao == 4:
        info_armazenamento()
    elif opcao == 0:
        break
    else:
        print('Opção Inválida')

    input('\nPressione enter para continuar...')
