# calculo de IMC

nome = input('Informe o seu nome: ')
peso = float(input('Informe o seu peso: ').replace(",","."))
altura = float(input('Infrome sua altura: ').replace(",","."))

imc = peso /(altura*altura)

if imc < 16:
    print(f'Seu IMC é {imc:.2f} e você esta Magro pra cacete')
elif imc < 17:
    print(f'Seu IMC é {imc:.2f} e você esta Magro moderado')
elif imc < 18.5:
    print(f'Seu IMC é {imc:.2f} e você esta Magro leve')
elif imc < 25:
    print(f'Seu IMC é {imc:.2f} e você esta Saudável')
elif imc < 30:
    print(f'Seu IMC é {imc:.2f} e você esta Sobrepeso')
elif imc < 35:
    print(f'Seu IMC é {imc:.2f} e você esta Gordo')
elif imc < 40:
    print(f'Seu IMC é {imc:.2f} e você esta Gordão')
else:
    print(f'Seu IMC é {imc:.2f} e você esta Gordaça')