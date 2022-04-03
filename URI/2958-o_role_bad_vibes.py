from operator import itemgetter

entrada = input().split(' ')
linhas = int(entrada[0])
colunas = int(entrada[1])
celulas_vida = list()
celulas_disciplinas = list()

for i in range(0, linhas):
    entrada = input().split(' ')
    for j in range(0, colunas):
        par = (int(entrada[j][0]), entrada[j][1])
        if par[1] == 'V':
            celulas_vida.append(par)
        else:
            celulas_disciplinas.append(par)

celulas_disciplinas = sorted(
    celulas_disciplinas, reverse=True, key=itemgetter(0))
celulas_vida = sorted(celulas_vida, reverse=True, key=itemgetter(0))

for celula in celulas_vida:
    print('{}{}'.format(celula[0], celula[1]))

for celula in celulas_disciplinas:
    print('{}{}'.format(celula[0], celula[1]))
