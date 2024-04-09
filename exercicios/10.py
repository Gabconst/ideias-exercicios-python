def valorPagamento(valorprestacao, diasatraso):
    multa = valorprestacao * 0.03
    juros = valorprestacao * (0.001 * diasatraso)
    valorpagar = valorprestacao + multa + juros
    return valorpagar


quantidadep = 0
totaldeprestacoes = 0

while True:
    valorprestacao = float(input('Digite o valor da prestação (ou 0 para encerrar):'))

    if valorprestacao == 0:
        break

    diasatraso = int(input('Digite o número de dias em atraso:'))
    valorpagar = valorPagamento(valorprestacao, diasatraso)

    print('Valor a ser pago: {}'.format(valorpagar))

    quantidadep = quantidadep + 1
    totaldeprestacoes = totaldeprestacoes + valorpagar

print('Relatório:')
print('Quantidade de prestações pagas: {}'.format(quantidadep))
print('Valor total das prestações pagas: {}'.format(totaldeprestacoes))

