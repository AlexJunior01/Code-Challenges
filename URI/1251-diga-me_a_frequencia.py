from collections import Counter
from operator import itemgetter

quebra_linha = False
while True:
    try:
        frase = input()
        contador_de_chars = Counter(frase)
        contador_de_chars = contador_de_chars.most_common(
            len(contador_de_chars))

        ordem_ascendente_real = sorted(contador_de_chars, key=itemgetter(0))
        ordem_ascendente_real = sorted(
            ordem_ascendente_real, key=itemgetter(1), reverse=True)
        ordem_ascendente_real.reverse()
        if quebra_linha:
            print()
        else:
            quebra_linha = True
        for char, qtd in ordem_ascendente_real:
            print('{} {}'.format(ord(char), qtd))

    except EOFError:
        break
