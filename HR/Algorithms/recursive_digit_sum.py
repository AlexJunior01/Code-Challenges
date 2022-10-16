def super_digit(n, k):
    sum_digits = 0
    for digit in n:
        sum_digits += int(digit)

    p = str(sum_digits * k)

    while True:
        sum_digits = 0
        if len(p) == 1:
            return int(p)

        for digit in p:
            sum_digits += int(digit)

        p = str(sum_digits)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = first_multiple_input[0]
    k = int(first_multiple_input[1])
    result = super_digit(n, k)
    print(result)
