valor_hora = float(input('Digite o valor que você ganha por hora:'))
horas_trabalhadas = float(input('Digite o número de horas trabalhadas no mês: '))
salario_bruto = valor_hora * horas_trabalhadas
imposto_renda = 0.11 * salario_bruto
inss = 0.08 * salario_bruto
sindicato = 0.05 * salario_bruto


salario_liquido = salario_bruto - (imposto_renda + inss + sindicato)

print('Salário Bruto: {}'.format(salario_bruto))
print('Desconto do Imposto de Renda (11%):{}'.format(imposto_renda))
print('Desconto do INSS (8%):{}'.format(inss))
print('Desconto do Sindicato (5%):{}'.format(sindicato))
print('Salário Líquido: {}'.format(salario_liquido))