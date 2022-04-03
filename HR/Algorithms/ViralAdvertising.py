def viralAdvertising(n):
    receive = 5
    likes = 2
    result = 2

    for day in range(2, n+1):
        receive = likes*3
        likes = int(receive/2)
        result += likes

    return result


n = int(input())
result = viralAdvertising(n)
print(result)