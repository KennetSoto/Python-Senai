#função como lambda
calcular_retangulo = lambda base, altura: base * altura

base = int(input('Informe a base do retangulo: '))
altura = int(input('Informe a altura do retangulo: '))

print(f'A area do retangulo é {calcular_retangulo(base, altura)}')