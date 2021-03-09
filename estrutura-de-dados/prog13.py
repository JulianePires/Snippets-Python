altura = float(input('Informe a sua altura: '))
sexo = str(input('Informe o sexo M ou F: '))

if sexo == 'M' or sexo == 'm':
    print(f'Seu peso ideal é: {(72.7*altura) - 58}')
else:
    print(f'Seu peso ideal é: {(62.1*altura) - 44.7}')
