# declaraçao de variaveis
nome = "Kennet" # string
idade = 34      #int
altura = 1.82   #float
dev = True      #logico (booleano)

#saida de dados (primeira forma " + ")
print('Forma de saída +')
print('Nome: ' + nome + ',')
print('Idade: '+ str(idade) + '.')

#saida de dados (segunda forma " , ")
print('Forma de saída ,')
print('Nome: ' , nome , ',')
print('Idade: ' ,idade  , '.')

#saida de dados (terceira forma " {} . format ")
print('Forma de saída {}. format')
print('Nome: {}.'.format(nome))
print('Idade: {}.'.format(idade))
print('Meu nome é: {} e tenho {} anos.'.format(nome,idade))

#saida de dados (quarta forma " f ")
print('Forma de saída F')
print(f'Nome: ' , nome )
print(f'Idade: ' ,idade)
print(f'Meu nome é {nome} e tenho {idade} anos.')

# tipo da variavel
print('Tipo das variaveis')
print(type(nome))
print(type(idade))
print(type(altura))
print(type(dev))