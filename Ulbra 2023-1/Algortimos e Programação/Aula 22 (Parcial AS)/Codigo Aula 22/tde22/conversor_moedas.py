import requests

def convert_dolar(valor):
    response = requests.get('https://api.exchangerate-api.com/v4/latest/BRL')
    if response.status_code == 200: # Verifica sucesso da requisição
        data = response.json()
        taxa = data['rates']['USD'] # Obtém a taxa de câmbio 
        dolar = valor * taxa  # Converte o valor
    return dolar
def convert_euro(valor):
    euro = 0
    return euro
def convert_peso(valor):
    peso = 0
    return peso

print('Bem vindo ao conversor de moedas.')
print('======Menu======')
print('1. Converter para Dólar (USD)')
print('2. Converter para EURO (EUR)')
print('3. Converter para Peso Argentino (ARS)')
print('0. Sair')

while True:
    opcao = int(input('Digite a opção Desejada: '))
    valor = float(input('Digite o valor em Reais.'))
    if opcao == 1:
        valor_convertido = convert_dolar(valor)
        print(f'Valor convertido: US$ {valor_convertido}')
    elif opcao == 2:
        valor_convertido = convert_euro(valor)
        print(f'Valor convertido: € {valor_convertido}')
    elif opcao == 3:
        valor_convertido = convert_peso(valor)
        print(f'Valor convertido: AR$ {valor_convertido}')
    elif opcao == 0:
        break
    else:
        print('Opção inválida')

   

