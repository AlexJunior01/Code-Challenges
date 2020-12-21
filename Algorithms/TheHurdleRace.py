def hurdleRace(k, height):
    max_height = max(height)
    if k > max_height:
        return 0
    else:
        return max_height - k


nk = input().split()
n = int(nk[0])
k = int(nk[1])
height = list(map(int, input().rstrip().split()))
result = hurdleRace(k, height)
print(result)