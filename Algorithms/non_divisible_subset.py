from math import ceil


def nonDivisibleSubset(divisor, numbers):
    remainders = [x%divisor for x in numbers]
    counter = [0 for i in range(divisor)]
    max_subset = 0

    for x in remainders:
        counter[x] += 1

    if counter[0] > 0:
        max_subset += 1

    if divisor % 2 == 0:
        if counter[int(divisor/2)] > 0:
            max_subset += 1

    for i in range(1, ceil(divisor/2)):
        j = divisor - i

        if counter[i] >= counter[j]:
            max_subset += counter[i]
        else:
            max_subset += counter[j]
    
    return max_subset




if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    s = list(map(int, input().rstrip().split()))
    
    result = nonDivisibleSubset(k, s)
    print(result)
