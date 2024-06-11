# lista

nomes = ['Stefany', 'Debora', 'Julia', 'Maria', 'Eline', 'Agda', 'Pamella', 'Rafaela', 'Eliane', 'Ana']

#usuario informa o nome que deseja pesquisar, transforma a primeira letra em maiusculo
nome = input('Digite o nome que deseja procurar: ').capitalize()



#verifica se o nome esta na lista:
try:
    #retorna o indice do nome pesuisado
    indice = nomes.index(nome)
    print(f'Nome {nome} encontrado, posicionado no numero {indice}.')
except:
    print('Nome não encontrado')