import psutil
import platform
import cpuinfo

def info_so():
    sistema = platform.system()
    versao = platform.release()
    print(f'\nSistema Operacional {sistema} {versao}')
    print('=-'*20)

def info_processador():
    processador = cpuinfo.get_cpu_info()
    print(f"\nProcessador {processador['brand_raw']} {processador['hz_actual_friendly']}")
    print('=-'*20)

def info_memoria():
    mem = psutil.virtual_memory()
    mem_GB = mem.total / 1024 ** 3
    mem_GB = round(mem_GB,2)
    print(f'\nMémoria total: {mem_GB} GB')
    print('=-'*20)

def info_armazenamento():
    discos = psutil.disk_partitions()
    print("\nInformações de armazenamento:")
    for disco in discos:
        if disco.fstype:
            espaco = psutil.disk_usage(disco.mountpoint)
            print("Disco:", disco.device)
            print("Espaço Total:", f"{espaco.total / (1024 ** 3):.2f} GB")
            print("Espaço Utilizado:", f"{espaco.used / (1024 ** 3):.2f} GB")
            print("Espaço Livre:", f"{espaco.free / (1024 ** 3):.2f} GB\n")
    print('=-'*20)
    
print('\nOlá. Seja bem-vindo ao programa de informações do PC.\n')
print('=-'*20)
print('1. Informações do Sistema Operacional')
print('2. Informações do Processador')
print('3. Informações da Memória RAM')
print('4. Informações do Armazenamento')
print('0. Sair')
print('=-'*20)
print('')

while True:
    opcao = int(input('Digite o número da opção desejada (0 para sair do programa): '))
    if opcao == 1:
        info_so()
    elif opcao == 2:
        info_processador()
    elif opcao == 3:
        info_memoria()
    elif opcao == 4:
        info_armazenamento()
    elif opcao == 0:
        print('Finalizando o programa.')
        break
    else:
        print('Opção Inválida')

    input('\nPressione enter para continuar...')