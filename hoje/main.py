def calc(x,y):
    soma = x + y
    yield soma
    subtracao = x - y
    yield subtracao
    multiplicacao = x * y
    yield multiplicacao
    divisao = x // y
    yield divisao

x = int(input('Informe o numero:'))
y = int(input('Informe o numero:'))
resultados = calc(x,y)

print(f'A soma é {next(resultados)}.')
print(f'A subtração é {next(resultados)}.')
print(f'A multiplicação é {next(resultados)}.')
print(f'A divisão é {next(resultados)}.')
