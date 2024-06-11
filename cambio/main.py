from forex_python.converter import CurrencyRates

valor = str(input('Informe o valor da moeda a ser convertida: '))
valor = float(valor.replace(',', '.'))

moeda = input('Informe a moeda de origem: ')
moeda_de_conversao = input('Informe a moeda de destino: ').upper()

#faz a conversao
result = CurrencyRates().convert(moeda, moeda_de_conversao, valor)

#exibe os resutados
print(f'$ {valor:,.2f}{moeda} =$ {result:,.2f} {moeda_de_conversao}.')