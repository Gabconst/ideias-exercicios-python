vende = int(input('Quantos vendedores quer registrar?'))
scontadores = [0] * 10

for i in range(vende):
    brutas = float(input(f'Insira as vendas brutas do vendedor {i + 1}: '))
    salarioo = 200 + 0.09 * brutas
    indi = int((salarioo - 200) // 100)
    indi = max(0, min(indi, 9))
    scontadores[indi] += 1

for i in range(10):
    if i == 9:
        print(f'vendedores com salário acima de 1000: {scontadores[i]}')
    else:
        print(f'vendedores com salário de {200 + i * 100} - {299 + i * 100}: {scontadores[i]}')
