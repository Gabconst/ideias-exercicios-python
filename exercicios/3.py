sexo = input('Digite "M" para masculino e "F" para feminino: ')
altura = float(input('Digite a altura em metros: '))
pesoideal = 0

if sexo.upper() == 'M':
    pesoideal = (72.7 * altura) - 58
elif sexo.upper() == 'F':
    pesoideal = (62.1 * altura) - 44.7
else:
    print('Sexo não reconhecido. Use "M" para masculino e "F" para feminino.')

if pesoideal != 0:
    print('O peso ideal é:', pesoideal)