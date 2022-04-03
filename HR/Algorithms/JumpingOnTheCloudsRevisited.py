def jumpingOnClouds(c, k):
    result = 100
    size = len(c)
    positition = 0

    while True:
        result -= 1
        positition = (positition + k) % size

        if c[positition] == 1:
            result -= 2

        if result == 0 or positition == 0:
            break
    
    return result


nk = input().split()
n = int(nk[0])
k = int(nk[1])
c = list(map(int, input().rstrip().split()))
result = jumpingOnClouds(c, k)
print(result)