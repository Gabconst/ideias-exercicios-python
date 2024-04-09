notaum = float(input('Digite a primeira nota:'))
notadois = float(input('Digite a segunda nota:'))
media = (notaum + notadois) / 2
if media == 10:
    print('Aprovado com Distinção')
elif media >= 7:
    print('Aprovado')
else:
    print('Reprovado')