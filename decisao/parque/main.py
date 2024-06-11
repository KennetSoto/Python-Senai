# acesso ao parque
nome =  input('Digite se nome: ')
idade = int(input('Digite a sua idade: '))
altura = float(input('Digite sua altura: ').replace(',', '.'))


if idade >= 16  and altura >= 1.60:
    print(f'{nome} com {altura} e {idade} anos, pode acessar o briquedo')
else:
    print(f'{nome} com {altura} e {idade} anos, não pode acessar o brinquedo')