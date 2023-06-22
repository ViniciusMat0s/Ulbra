import requests

response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')


if response.status_code == 200:
    data = response.json()
    taxa = data['rates']['BRL']
    valor_dolar = float(input('Digite um valor em dolar USD.'))
    valor_real = valor_dolar * taxa
    print(f'Valor em R$: {valor_real}' )
else:
    print('Erro ao consulta api.')
