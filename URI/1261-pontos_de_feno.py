def substitui_valor(hay_point, frase) -> int:
    """Recebe um dicionário hay_point e uma frase e retorna o valor dela."""
    aux = 0
    for palavra in frase.split():
        valor = hay_point.get(palavra)
        if valor:
            aux += valor
    return aux


def main():
    # m = Palavras no dicionário
    # n = Quantidade de descrições de cargo
    m, n = list(map(int, input().rstrip().split()))
    valor_cargo = 0
    # Criando dicionário hay_point
    hay_point = dict()
    for i in range(m):
        descricao, valor = input().rstrip().split()
        hay_point[descricao] = int(valor)

    while n > 0:
        aux = input()
        if aux == '.':
            print(valor_cargo)
            valor_cargo = 0
            n -= 1
            continue

        valor_cargo += substitui_valor(hay_point, aux)


if __name__ == '__main__':
    main()
