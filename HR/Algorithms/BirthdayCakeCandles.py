def birthdayCakeCandles(ar):
    maxi = max(ar)
    result = ar.count(maxi)
    return result


ar_count = int(input())

ar = list(map(int, input().rstrip().split()))

result = birthdayCakeCandles(ar)
print(result)