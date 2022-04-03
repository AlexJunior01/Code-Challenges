def staircase(n):
    sharp = '#'
    space = ' '
    for i in range(1, n+1):
        line = space*(n-i)+sharp*i
        print('{}'.format(line))


n = int(input())
staircase(n)