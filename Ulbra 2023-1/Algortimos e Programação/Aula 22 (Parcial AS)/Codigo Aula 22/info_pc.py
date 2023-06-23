import psutil

mem = psutil.virtual_memory()

mem_KB = mem.total / 1024
mem_MB = mem.total / 1024 ** 2
mem_GB = mem.total / 1024 ** 3
print(f'Mémoria total em KB: {mem_KB}')
print(f'Mémoria total em MB: {mem_MB}')
print(f'Mémoria total em GB: {mem_GB}')

print(f'Memória disponível: {mem.available}')

print(f'Percentual usado {mem.percent}%')