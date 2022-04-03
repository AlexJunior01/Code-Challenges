def catAndMouse(x, y, z):
    distA = abs(x-z)
    distB = abs(y-z)

    if distA < distB:
        return 'Cat A'
    elif distB < distA:
        return 'Cat B'
    else:
        return 'Mouse C'



q = int(input())
for q_itr in range(q):
    xyz = input().split()
    x = int(xyz[0])
    y = int(xyz[1])
    z = int(xyz[2])
    result = catAndMouse(x, y, z)
    print(result)