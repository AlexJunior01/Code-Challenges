def extraLongFactorials(n):
    result = 1
    for i in range(n, 0, -1):
        result *= i
    return result

n = int(input())
result = extraLongFactorials(n)
print(result)
