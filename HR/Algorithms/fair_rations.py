
def is_possible(B):
    aux = sum([value % 2 for value in B])
    return aux % 2 == 0


def fair_rations(B):
    normalized = []
    total = 0

    if not is_possible(B):
        return 'NO'

    for idx, value in enumerate(B):
        if value % 2 == 1:
            normalized.append(idx)

    for idx in range(1, len(normalized), 2):
        total += normalized[idx] - normalized[idx-1]

    return str(total*2)


if __name__ == '__main__':
    N = int(input().strip())

    B = list(map(int, input().rstrip().split()))

    result = fair_rations(B)
    print(result)
