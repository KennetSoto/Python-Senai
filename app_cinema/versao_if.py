import os
import time

print('-------------------------Bem vindo ao cinema Monty-----------------------------')

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

while True:
    print('\nLista de filmes disponiveis nesta semana: ')
    print('SALA 1 - Coração Valente - Idade minima 18 anos')
    print('SALA 2 - Batman - Idade minima 16 anos')
    print('SALA 3 - Interestelar - Idade minima 14 anos')
    print('SALA 4 - Gente Grande - Idade minima 10 anos')
    print('SALA 5 - O Paizão - Sem idade minima')
    filme = int(input('\nQual a sala do filme que deseja ver: '))

    if idade >= 18:
        print(f'\nBoa escolha {nome}, siga para sala {filme} e tenha um ótimo filme')
        break
    elif idade >= 16 and filme == 1:
        print('\nSUA IDADE NÃO É ADEQUADA PRA ESTE FILME')
        print('Por favor, escolha outro filme:')
        time.sleep(3)
        os.system('cls')
        continue
    elif idade >= 14 and filme == 1  or idade >= 14 and filme == 2:
        print('\nSUA IDADE NÃO É ADEQUADA PRA ESTE FILME')
        print('Por favor, escolha outro filme:')
        time.sleep(3)
        os.system('cls')
        continue
    elif idade >= 10 and filme == 1  or idade >= 10 and filme == 2 or idade >= 10 and filme == 3:
        print('\nSUA IDADE NÃO É ADEQUADA PRA ESTE FILME')
        print('Por favor, escolha outro filme:')
        time.sleep(3)
        os.system('cls')
        continue
    else:
        print(f'\nBoa escolha {nome}, siga para sala {filme} e tenha um ótimo filme')
        break


