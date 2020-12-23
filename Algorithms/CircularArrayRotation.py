def circularArrayRotation(a, k, queries):
    result = []
    size_a = len(a)
    dist = k % size_a

    new_a = a[-dist:] + a[:-dist]

    for query in queries:
        result.append(new_a[query])

    return '\n'.join(map(str, result))


nkq = input().split()
n = int(nkq[0])
k = int(nkq[1])
q = int(nkq[2])
a = list(map(int, input().rstrip().split()))

queries = []

for _ in range(q):
    queries_item = int(input())
    queries.append(queries_item)

result = circularArrayRotation(a, k, queries)
print(result)