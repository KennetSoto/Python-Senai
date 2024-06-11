# Notas do aluno

nome =  input('Digite se nome: ')

#primeira pratica
nota = float(input('Digite sua nota: ').replace(',', '.'))

# segunda pratica
nota = str(input('Digite sua nota: ')).replace(',', '.')
nota = float(nota)

if nota >= 7:
    print(f'Aluno {nome} com a nota {nota} passou e não fez mais que a obrigação! ')
elif nota >= 5:
    print(f'Aluno {nome} com a nota {nota} não fez o mínimo e esta de recuperação! ')
else:
    print(f'Aluno {nome} com a nota {nota} foi a escola para que? Esta reprovado! ')