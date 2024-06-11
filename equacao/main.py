import math

def calcular_primeiro(a, b):
    resultado = -b / a
    return resultado

def calcular_segundo(a, b, c):
    resultado = b**2 - 4*a*c
    if resultado < 0:
        return "A equação não possui raízes reais"
    else:
        x1 = (-b + math.sqrt(resultado)) / (2*a)
        x2 = (-b - math.sqrt(resultado)) / (2*a)
        return x1, x2

print('-'*7 + 'Equações' + '-'*7)
print('1 - Equação do primeiro grau: Ax + b = 0')
print('2 - Equação do segundo grau: Ax² + bx + c = 0')
equacao = int(input('\nDigite qual deseja executar: '))

while True:
    if equacao == 1:
        a = int(input('Digite o valor de a: '))
        if a == 0:
            print('a não pode ser zero ')
            break
        b = int(input('Digite o valor de b: '))
        print(f"O resultado da equação {a}x + {b} = 0 é x = {calcular_primeiro(a,b)}")
        break
    elif equacao == 2:
        a = int(input('Digite o valor de a: '))
        b = int(input('Digite o valor de b: '))
        c = int(input('Digite o valor de c: '))
        print(f"Os resultados da equação {a}x² + {b}x + {c} = 0 são: {calcular_segundo(a,b,c)}")
        break
    else:
        print('Opção inválida')
        break
