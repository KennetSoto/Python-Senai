alunos = []

for _ in range(2):
    nome = input("Digite o nome do aluno: ")
    notas = [float(input(f"Digite a nota {i + 1} (0 a 10): ")) for i in range(5)]
    media = sum(notas) / len(notas)

    if media >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    alunos.append((nome, media, situacao))

#filtrando os alunos
aprovados = [aluno[0] for aluno in alunos if aluno[1] >= 7]

reprovados = [aluno[0] for aluno in alunos if aluno[1] < 7]

print("\nAlunos Aprovados:")
for aluno in aprovados:
    print(aluno)

print("\nAlunos Reprovados:")
for aluno in reprovados:
    print(aluno)