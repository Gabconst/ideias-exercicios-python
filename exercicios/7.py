num = int(input('Digite um número inteiro de 1 a 10:'))

if 1 <= num <= 10:
    print('Tabuada de {}'.format(num))
    for i in range(1, 11):
        print('{} X {} = {}'.format(num, i, num * i))
else:
    print('Número fora do intervalo válido. Por favor, digite um número entre 1 e 10.')

