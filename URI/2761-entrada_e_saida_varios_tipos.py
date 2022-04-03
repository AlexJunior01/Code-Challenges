from struct import *

lista = input().split(' ')
inteiro = int(lista[0])
ponto_flutuante = float(lista[1])
ponto_flutuante = pack('f', ponto_flutuante)
ponto_flutuante = unpack('f', ponto_flutuante)
ponto_flutuante = ponto_flutuante[0]
char = lista[2]
esp = ' '*4
frase = ' '
frase = frase.join(lista[3:])

print('{}{:.6f}{}{}'.format(inteiro, ponto_flutuante, char, frase))
print('{}\t{:.6f}\t{}\t{}'.format(inteiro, ponto_flutuante, char, frase))
print('{:>10}{:>10.6f}{:>10}{:>10}'.format(
    inteiro, ponto_flutuante, char, frase))
