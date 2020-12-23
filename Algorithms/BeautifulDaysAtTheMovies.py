def beautifulDays(i, j, k):
    result = 0

    for day in range(i, j+1):
        reverse_day = reverseDay(day)
        if abs(day - reverse_day) % k == 0:
            result +=1

    return result


def reverseDay(day):
    string_day = str(day)
    string_day = string_day[::-1]
    return int(string_day)

ijk = input().split()
i = int(ijk[0])
j = int(ijk[1])
k = int(ijk[2])
result = beautifulDays(i, j, k)
print(result)
