from math import sqrt

def diagonalDifference(arr):
    principal = antidiagonal = 0
    size = len(arr)
    for i in range(0, size):
        index_s = size-1

        principal += arr[i][i]
        antidiagonal += arr[i][index_s-i]

    result = abs(principal - antidiagonal)
    return result

n = int(input().strip())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr)
print(result)