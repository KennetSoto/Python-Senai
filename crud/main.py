# Crie um CRUD utilizando os conceitos de lista, tupla e dicionário. O usuário pode cadastrar quantas pessoas quiser. Os dados a serem cadastrados são:
# - Nome
# - CPF
# - Telefone
# - E-mail
# - Profissão
# - Empresa

tupla = ('Nome','CPF', 'Telefone','E-mail','Profissao', 'Empresa')
lista =[]

def adicionar():
    dicionario = {}
    for chave in tupla:
        dicionario[chave] = input(f'Digite o {chave}: ')
    lista.append(dicionario)

def listar():
    for dicionario in lista:
        for chave in dicionario:
            print(f'{chave}: {dicionario[chave]}')
        

def apagar():
    nome = input('Digite o nome da pessoa a ser deletada: ')
    for pessoa in lista:
        if pessoa['Nome'] == nome:
            chave = input('Digite a chave a ser deletada: ')
            if chave in pessoa:
                del pessoa[chave]
                print(f'Chave {chave} foi removida da lista.')
                break
    else:
        print(f'{nome} não está na lista.')

def atualizar():
    nome = input('Informe o nome a ser alterado: ')
    for pessoa in lista:
        if pessoa['Nome'] == nome:
            chave = input('Informe a chave a ser alterada: ')
            if chave in pessoa:
                novo = input('Informe o novo valor: ')
                pessoa[chave] = novo
                print('Valor atualizado.')
                break
    else:
        print('Nome não encontrado.')

while True:
    print('\nCadastros')
    print('\n1. Inserir pessoa na lista')
    print('2. Listar pessoas cadastradas')
    print('3. Atualizar nome')
    print('4. Deletar nome')
    print("5. Sair do programa")

    opcao = int(input('Digite a opção desejada: '))

    if opcao == 1:
        adicionar()
    elif opcao == 2:
        listar()
    elif opcao == 3:
        atualizar()
    elif opcao == 4:
        apagar()
    elif opcao == 5:
        print('Fim do programa')
        break
    else:  
        print('Opção invalida')



            