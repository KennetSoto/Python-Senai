import os  # Importa o módulo 'os' que permite interagir com o sistema operacional
import time  # Importa o módulo 'time' que permite trabalhar com o tempo

# O usuário informa um número
contador = int(input('Informe um numero: '))  # Solicita ao usuário que insira um número e converte a entrada para um inteiro

os.system('cls')  # Limpa a tela do console

# Conta a partir do número informado até 0
while contador >= 1:  # Inicia um loop que continua enquanto 'contador' for maior ou igual a 0
    print(f'Contagem regressiva: {contador}...')  # Imprime a contagem regressiva atual
    time.sleep(1)  # Pausa a execução do programa pausando por 1 segundo entre cada número
    os.system('cls')  # Limpa a tela do console
    contador -= 1  # Decrementa o 'contador' em 1

print('BOOOM !!!') #Imprime a palavra BOOOM apos o fim da contagem
    

