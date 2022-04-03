
def compareTriplets(a, b):
    result = [0, 0]

    for i in range(3):
        if a[i] > b[i]:
            result[0] = result[0] + 1
        elif a[i] < b[i]:
            result[1] = result[1] + 1

    return result


a = list(map(int, input().rstrip().split()))

b = list(map(int, input().rstrip().split()))

result = compareTriplets(a, b)

print(result)