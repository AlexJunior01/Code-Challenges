def findDigits(n):
    number = str(n)
    result = 0
    for digit in number:
        digit = int(digit)
        if digit != 0:
            if n % digit == 0:
                result += 1

    return result


t = int(input())
for t_itr in range(t):
    n = int(input())
    result = findDigits(n)
    print(result)