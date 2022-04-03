def imprimir_resposta(horas, minutos):
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas, minutos))


lista = input().split(' ')
hora_inicial = int(lista[0])
minuto_inicial = int(lista[1])
hora_final = int(lista[2])
minuto_final = int(lista[3])

if minuto_final < minuto_inicial:
    minuto_final += 60
    hora_final -= 1

if hora_final < hora_inicial:
    duracao_horas = 24 - hora_inicial + hora_final
else:
    duracao_horas = hora_final - hora_inicial
duracao_minutos = minuto_final - minuto_inicial

if duracao_horas == 0 and duracao_minutos == 0:
    duracao_horas = 24

imprimir_resposta(duracao_horas, duracao_minutos)
