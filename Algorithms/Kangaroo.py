def kangaroo(x1, v1, x2, v2):
    result = 0
    if v2 >= v1:
       return result 
    
    while x1 < x2:
        x1 += v1
        x2 += v2

        if x1 == x2:
            result = 1
    
    return result
        


x1, v1, x2, v2 = map(int, input().rstrip().split())
result = kangaroo(x1, v1, x2, v2)

if result == 1:
    print('YES')
else:
    print('NO')
