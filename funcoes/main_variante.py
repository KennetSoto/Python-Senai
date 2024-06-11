#Crie um programa que o usuário possa escolher se deseja saber a área de um círculo, de um triângulo ou de um trapézio.

def formas(escolha):
    if escolha == 'circulo':
        area = 'A = π . r²'
        return area
    elif escolha == 'triangulo':
        area = 'A = b⋅h 2'
        return area
    elif escolha == 'trapezio':
        area = 'A = (a + b)⋅h / 2'
        return area

escolha = input('Qual forma deseja saber a area: (circulo, triangulo ou trapezio): ').lower()

print(f'A formula para calcular a área do {escolha} é: {formas(escolha)}')