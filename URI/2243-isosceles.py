if __name__ == '__main__':
    n = int(input())
    colunas = list(map(int, input().rstrip().split()))
    direita = list()
    esquerda = list()

    alt_atual = 0
    for coluna in colunas:
        if coluna > alt_atual:
            alt_atual += 1
            direita.append(alt_atual)
        else:
            alt_atual = coluna
            direita.append(alt_atual)

    alt_atual = 0
    for coluna in reversed(colunas):
        if coluna > alt_atual:
            alt_atual += 1
            esquerda.append(alt_atual)
        else:
            alt_atual = coluna
            esquerda.append(alt_atual)

    # desinvertendo esquerda
    esquerda.reverse()

    maior_triangulo = 0
    for i in range(n):
        aux = min([esquerda[i], direita[i]])
        if aux > maior_triangulo:
            maior_triangulo = aux

    print(maior_triangulo)
