# Crie um dicionário em Python com os seguintes dados de uma pessoa:
# - Nome
# - CPF
# - RG
# - Data de Nascimento
# - Gênero
# - E-mail
# - Telefone
# - Tipo sanguíneo
# - Profissão
# - Empresa

# O programa deverá exibir os dados da pessoa no console.

print('Insira os dados do usuário')
pessoa = {
    "Nome": input("Digite o nome: "),
    "CPF": input("Digite o CPF: "),
    "RG": input("Digite o RG: "),
    "Data de Nascimento": input("Digite a data de nascimento (dd/mm/aaaa): "),
    "Gênero": input("Digite o gênero (M/F): "),
    "E-mail": input("Digite o e-mail: "),
    "Telefone": input("Digite o telefone: "),
    "Tipo sanguíneo": input("Digite o tipo sanguíneo: "),
    "Profissão": input("Digite a profissão: "),
    "Empresa": input("Digite a empresa: ")
}

#acessando chave e valor dentro da chave no loop
print('\nDados do usuário')
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")


#acessando chave no loop e depois o valor dentro da chave
# print('\nDados do usuário')
# for chave in pessoa:
#     print(f"{chave}: {pessoa[chave]}")

