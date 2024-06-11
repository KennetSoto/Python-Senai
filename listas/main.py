#lista
nomes = ['Ana', 'Bia', 'Cida', 'Dora', 'Ellie', 'Aline']

#ordenar a lista
nomes.sort(reverse=True)

# #ordenar a lista na ordem reversa
# nomes.sort(reverse=True)

# exibe a lista 
for i in range(len(nomes)):
    print(f'{i + 1}º nome da lista: {nomes[i]}.')
