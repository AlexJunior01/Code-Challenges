def get_conjs():
    conj = list()
    for p in dicio['por']:
        for m in dicio['mat']:
            for f in dicio['fis']:
                for q in dicio['qui']:
                    for b in dicio['bio']:
                        conj.append(p+m+f+q+b)

    return sorted(conj, reverse=True)


if __name__ == '__main__':
    dicio = dict()
    dicio['por'] = sorted(
        list(map(int, input().rstrip().split()))[1:], reverse=True)
    dicio['mat'] = sorted(
        list(map(int, input().rstrip().split()))[1:], reverse=True)
    dicio['fis'] = sorted(
        list(map(int, input().rstrip().split()))[1:], reverse=True)
    dicio['qui'] = sorted(
        list(map(int, input().rstrip().split()))[1:], reverse=True)
    dicio['bio'] = sorted(
        list(map(int, input().rstrip().split()))[1:], reverse=True)
    n_conj = int(input())
    conjs = get_conjs()

    total = sum(conjs[0:n_conj])

    print(total)
