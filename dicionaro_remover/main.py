pessoa = {
    'Nome': 'Mazza',
    'Idade': 35,
    'Profissão': 'Gerente',
    'Empresa': 'Maraba',
    'Genero': 'Fluido',
    'Cidade': 'São Paulo'
}
for chave in pessoa:
    print(f'{chave}: {pessoa.get(chave)}')

#opção de remoção com del
# del pessoa[input('Informe o nome da chave a ser deletada: ')]

#opção de remoção com pop que possibilida o retorno do valor removido
valor_removido = pessoa.pop(input('Informe o nome da chave a ser deletada: '))
print(f'O valor removido foi: {chave}: {valor_removido}')

for chave in pessoa:
    print(f'{chave}: {pessoa.get(chave)}')