N = int(input())

for i in range(0, N):
    lista = input().split(' ')
    f1 = int(lista[0])
    f2 = int(lista[1])

    if f1 < f2:
        menor = f1
        maior = f2
    else:
        menor = f2
        maior = f1

    resto = -1
    mdc = -1
    while resto != 0:
        resto = maior % menor
        maior = menor
        menor = resto

    print('{}'.format(maior))
