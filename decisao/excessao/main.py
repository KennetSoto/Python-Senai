#tratando excessoes

try:
    n1 = int(input('Informe o primeiro numero: '))
    n2 = int(input('Informe o segundo numero: '))

    result = n1 + n2
    print(f'O resultado é {result}')
except:
    print('Numero informado é invalido')

