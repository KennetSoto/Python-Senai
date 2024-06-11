import os
import time

print('-------------------------Bem vindo ao cinema Monty-----------------------------')

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

while True:
    print('\nLista de filmes disponiveis nesta semana: ')
    print('SALA 1 - Coração Valente - Idade minima 18 anos')
    print('SALA 2 - Joker - Idade minima 16 anos')
    print('SALA 3 - Interestelar - Idade minima 14 anos')
    print('SALA 4 - Gente Grande - Idade minima 10 anos')
    print('SALA 5 - O Paizão - Sem idade mínima')
    filme = int(input('\nQual a sala do filme que deseja ver: '))

    match filme:
           case 1:
                if idade >= 18:
                     print(f'\nBoa escolha {nome}, siga para sala {filme} e tenha um ótimo filme')
                     break
                else:
                     print('\nSUA IDADE NÃO É ADEQUADA PRA ESTE FILME')
                     print('Por favor, escolha outro filme:')
                     time.sleep(3)
                     os.system('cls')
           case 2:
                if idade >= 16:
                     print(f'\nBoa escolha {nome}, siga para sala {filme} e tenha um ótimo filme')
                     break
                else:
                     print('\nSUA IDADE NÃO É ADEQUADA PRA ESTE FILME')
                     print('Por favor, escolha outro filme:')
                     time.sleep(3)
                     os.system('cls')
           case 3:
                if idade >= 14:
                     print(f'\nBoa escolha {nome}, siga para sala {filme} e tenha um ótimo filme')
                     break
                else:
                     print('\nSUA IDADE NÃO É ADEQUADA PRA ESTE FILME')
                     print('Por favor, escolha outro filme:')
                     time.sleep(3)
                     os.system('cls')
           case 4:
                if idade >= 10:
                     print(f'\nBoa escolha {nome}, siga para sala {filme} e tenha um ótimo filme')
                     break
                else:
                     print('\nSUA IDADE NÃO É ADEQUADA PRA ESTE FILME')
                     print('Por favor, escolha outro filme:')
                     time.sleep(3)
                     os.system('cls')
           case 5:
                print(f'\nBoa escolha {nome}, siga para sala {filme} e tenha um ótimo filme')
                break
                
                 
                    
                   
                   
                 
    
 
