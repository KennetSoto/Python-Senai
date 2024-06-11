# estrutura de decisão

nome =  input('Digite se nome:')
idade = int(input('Digite a sua idade:'))

if idade >= 18:
    print(f'{nome} com {idade} anos é maior de idade')
elif idade == 16:
    print(f'{nome} com {idade} anos é menor de idade mas pode votar')
else:
    print(f'{nome} com {idade} anos não é maior de idade')


