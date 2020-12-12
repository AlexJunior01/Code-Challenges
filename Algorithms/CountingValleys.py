def countingValleys(steps, path):
    now = 0
    result = 0
    for step in path:
        if step == 'U':
            now += 1
            if now == 0:
                result += 1
        else:
            now -= 1
    
    return result


steps = int(input().strip())
path = input()

result = countingValleys(steps, path)
print(result)