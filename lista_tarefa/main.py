# Crie um programa que o usuário cadastre uma lista de tarefas do dia. Ao finalizar a lista, o programa exibe a lista na tela.
lista = []

print('-----------Lista de tarefas-------------')
print('Para adicionar nova tarefa: digite a tarefa')
print('Para encerrar a adição de tarefas: digite enter')

while True:
    tarefa = input('Adicione uma nova tarefa:')

    if tarefa != '':
        lista.append(tarefa)
        continue
    else:
        break

print('------Sua lista de tarefas------')
for tarefa in lista:
    print(tarefa)


