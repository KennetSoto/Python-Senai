nome = input('Informe o seu nome: ')

print('BEM VINDO AO MONTY CINEMA\n')
print('LISTA DE FILMES\n')
print('SALA 1 - A volta dos que não foram.')
print('SALA 2 - A roda quadrada')
print('SALA 3 - Poeira em alto mar')
print('SALA 4 - AS tranças do rei careca')
print('SALA 5 - A vingança dos Sith\n')

sala = int(input('Infrome a sala desejada: '))

match sala:
    case 1:
        print(f'Filme escolhido por {nome}: A volta dos que não foram. ')
    case 2:
        print(f'Filme escolhido por {nome}: A roda quadrada. ')
    case 3:
        print(f'Filme escolhido por {nome}: Poeira em alto mar ')
    case 4:
        print(f'Filme escolhido por {nome}: AS tranças do rei careca')
    case 5:
        print(f'Filme escolhido por {nome}: A vingança dos Sith ')
    case _:
        print('Sala inexistente, aprenda a ler ')

