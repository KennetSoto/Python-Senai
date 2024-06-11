#Crie um programa que o usuário possa escolher se deseja saber a área de um círculo, de um triângulo ou de um trapézio.

def calculo_circulo(raio):
    area = 3.14 * (raio * raio)
    return area

def calculo_triangulo(base, altura):
    area = (base * altura)/ 2
    return area

def calculo_trapezio(base, base2, altura):
    area = (base + base2)*altura // 2
    return area

print(f'{'='*20} Geometria {'='*20}\n')
print('Circulo: A = π . r²')
print('Triangulo: A = b⋅h 2')
print('Trapézio: A = (a + b)⋅h / 2')
forma = input('Digite qual area deseja descobrir: ').lower()

if forma == 'circulo':
    raio = float(input('Digite o raio do circulo: '))
    print(f'\nA area do {forma} é {calculo_circulo(raio)}')
elif forma == 'triangulo':
    base = float(input('Digite a base do triangulo: '))
    altura = float(input('Digite a altura do triangulo: '))
    print(f'\nA area do {forma} é {calculo_triangulo(base, altura)}')
elif forma == 'trapezio':
    base = float(input('Digite a base maior do trapezio: '))
    base2 = float(input('Digite a base menor do trapezio: '))
    altura = float(input('Digite a altura do trapezio: '))
    print(f'\nA area do {forma} é {calculo_trapezio(base, base2, altura)}')

