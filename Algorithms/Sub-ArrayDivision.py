def birthday(chocolate, day, month):
    result = 0
    for i in range(len(chocolate)):
        if sum(chocolate[i:i+month]) == day:
            result += 1
        
    return result

size_choc = int(input())
chocolate = list(map(int, input().rstrip().split()))
dm = input().rstrip().split()
d = int(dm[0])
m = int(dm[1])

result = birthday(chocolate, d, m)
print(result)
