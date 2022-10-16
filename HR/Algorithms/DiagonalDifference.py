def diagonal_difference(arr):
    diag1 = diag2 = 0
    size = len(arr)

    for i in range(size):
        diag1 += arr[i][i]
        diag2 += arr[i][size-i-1]

    return abs(diag1 - diag2)


if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonal_difference(arr)
    print(result)


# 00 01 02
# 10 11 12
# 20 21 22
