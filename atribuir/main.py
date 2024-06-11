#lista
nomes = ['Stefany', 'Debora', 'Julia', 'Maria', 'Eline', 'Agda', 'Pamella', 'Rafaela', 'Eliane', 'Ana']

#exibir a lista
for nome in nomes:
    print(nome, end=' ')

#usuario informa o indice que deseja alterar
indice = int(input('\nInforme o indice que deseja alterar: '))
indice -= 1

#usuario informa o novo nome:
nomes[indice] = input('informe o novo nome: ')

#exibir a lista
for nome in nomes:
    print(nome, end=' ')