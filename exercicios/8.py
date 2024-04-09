notas = []

while True:
    valor = float(input('Digite uma nota (-1 para encerrar):'))
    if valor == -1:
        break
    notas.append(valor)

quantidade = len(notas)
print('Quantidade de valores lidos: {}'.format(quantidade))

print('Valores na ordem em que foram informados:', end=' ')
for nota in notas:
    print(nota, end=' ')

print('\nValores na ordem inversa à que foram informados:')
for nota in reversed(notas):
    print(nota)

soma = sum(notas)
print('Soma dos valores: {}'.format(soma))
media = soma / quantidade
print('Média dos valores: {:.2f}'.format(media))
acimadamedia = len([nota for nota in notas if nota > media])
print('Quantidade de valores acima da média: {}'.format(acimadamedia))
abaixodesete = len([nota for nota in notas if nota < 7])
print('Quantidade de valores abaixo de sete: {}'.format(abaixodesete))

print('Programa encerrado...')

