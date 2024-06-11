#entrada de dados
nome = input('Digite eu nome:')

#melhor pratica (para garantir que altura seja float e nao de erro no futuro)
# altura = str(input('Digite seu altura:')).replace(',' ,'.')
# altura = float(altura)

#converte mas altura é não é um float só string
altura = input('Digite seu altura:').replace(',', '.')
print(f'Seu nome é {nome} e sua altura é {altura}')
