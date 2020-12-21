def pickingNumbers(a):
    counter = [0 for i in range(100)]
    result = 0
    
    for number in a:
        counter[number] += 1

    for i in range(1, 100):
        if counter[i-1] + counter[i] > result:
            result = counter[i-1] + counter[i]

    return result


n = int(input().strip())
a = list(map(int, input().rstrip().split()))
result = pickingNumbers(a)
print(result)