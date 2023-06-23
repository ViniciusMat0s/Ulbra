import requests

def convert_dolar(valor):
    response = requests.get('https://api.exchangerate-api.com/v4/latest/BRL')
    if response.status_code == 200: # Verifica sucesso da requisição
        data = response.json()
        taxadolar = data['rates']['USD'] # Obtém a taxa de câmbio 
        dolar = valor * taxadolar  # Converte o valor
    return dolar

def convert_euro(valor):
    response = requests.get('https://api.exchangerate-api.com/v4/latest/BRL')
    if response.status_code == 200:
        data = response.json()
        taxaeuro = data['rates']['EUR']
        euro = valor * taxaeuro
    return euro

def convert_peso(valor):
    response = requests.get('https://api.exchangerate-api.com/v4/latest/BRL')
    if response.status_code == 200:
        data = response.json()
        taxapeso = data['rates']['ARS']
        peso = valor * taxapeso
    return peso

print('\nOlá. Seja bem-vindo ao conversor de moedas.\n')
print('=-'*20)
print('1. Converter para Dólar (USD)')
print('2. Converter para EURO (EUR)')
print('3. Converter para Peso Argentino (ARS)')
print('0. Sair')
print('=-'*20)
print('')

while True:
    opcao = int(input('Digite a opção Desejada: '))
    valor = float(input('Digite o valor em R$: \t'))
    if opcao == 1:
        valor_convertido = convert_dolar(valor)
        print(f'\nValor convertido: US$ {valor_convertido}')
        print('=-'*20)
    elif opcao == 2:
        valor_convertido = convert_euro(valor)
        print(f'\nValor convertido: € {valor_convertido}')
        print('=-'*20)
    elif opcao == 3:
        valor_convertido = convert_peso(valor)
        print(f'\nValor convertido: AR$ {valor_convertido}')
        print('=-'*20)
    elif opcao == 0:
        print("Finalizando o programa.")
        break
    else:
        print('\nOpção inválida.\n')

   

