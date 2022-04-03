def permutationEquation(p):
    p.insert(0,0)
    index = p.copy()
    result = []

    for i in range(1, len(p)):
        index[i] = p.index(i)

    for i in range(1, len(p)):
        aux = index[i]
        result.append(index[aux])

    return '\n'.join(map(str, result))



n = int(input())
p = list(map(int, input().rstrip().split()))
result = permutationEquation(p)
print(result)