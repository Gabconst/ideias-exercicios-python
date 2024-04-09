salario_atual = float(input('Insira o salário atual do colaborador:'))
faixaum = 280.00
faixadois = 700.00
faixatres = 1500.00

if salario_atual <= faixaum:
    percentualaumento = 20
elif salario_atual <= faixadois:
    percentualaumento = 15
elif salario_atual <= faixatres:
    percentualaumento = 10
else:
    percentualaumento = 5

aumento = (percentualaumento / 100) * salario_atual
novosalario = salario_atual + aumento

print('Salário antes do reajuste: {}'.format(salario_atual))
print('Percentual de aumento aplicado: {}'.format(percentualaumento))
print('Valor do aumento: {}'.format(aumento))
print('Novo salário após o aumento: {}'.format(novosalario))