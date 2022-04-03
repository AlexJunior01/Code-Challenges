from decimal import Decimal


def imprimir_resposta_notas(notas):
    print('NOTAS:')
    print('{} nota(s) de R$ 100.00'.format(notas[0]))
    print('{} nota(s) de R$ 50.00'.format(notas[1]))
    print('{} nota(s) de R$ 20.00'.format(notas[2]))
    print('{} nota(s) de R$ 10.00'.format(notas[3]))
    print('{} nota(s) de R$ 5.00'.format(notas[4]))
    print('{} nota(s) de R$ 2.00'.format(notas[5]))


def imprimir_resposta_moedas(moedas):
    print('MOEDAS:')
    print('{} moeda(s) de R$ 1.00'.format(moedas[0]))
    print('{} moeda(s) de R$ 0.50'.format(moedas[1]))
    print('{} moeda(s) de R$ 0.25'.format(moedas[2]))
    print('{} moeda(s) de R$ 0.10'.format(moedas[3]))
    print('{} moeda(s) de R$ 0.05'.format(moedas[4]))
    print('{} moeda(s) de R$ 0.01'.format(moedas[5]))


valor = Decimal(input())
notas = [100, 50, 20, 10, 5, 2]
moedas = [Decimal('1'), Decimal('0.5'), Decimal('0.25'),
          Decimal('0.10'), Decimal('0.05'), Decimal('0.01')]
qtd_notas = [0, 0, 0, 0, 0, 0]
qtd_moedas = [0, 0, 0, 0, 0, 0]

nota = 0
while valor >= 2:
    if notas[nota] <= valor:
        qtd_notas[nota] += 1
        valor -= notas[nota]
    else:
        nota += 1


moeda = 0
