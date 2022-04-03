from math import sqrt, ceil, floor

def squares(a, b):
    qtd_squares = 0
    begin = floor(sqrt(a))
    end = ceil(sqrt(b))

    for i in range(begin, end+1):
        if  a <= i**2 <=b:
            qtd_squares += 1

    return qtd_squares

    return qtd_squares




q = int(input().strip())
for q_itr in range(q):
    first_multiple_input = input().rstrip().split()

    a = int(first_multiple_input[0])

    b = int(first_multiple_input[1])

    result = squares(a, b)
    print(result)