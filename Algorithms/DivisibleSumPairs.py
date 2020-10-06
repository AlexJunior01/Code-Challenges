def divisibleSumPairs(array, divisor, n_numbers):
    n_pairs = 0
    for i in range(n_numbers):
        for j in range(i+1, n_numbers):
            if (array[i] + array[j]) % divisor == 0:
                n_pairs += 1
    
    print(n_pairs)



n_numbers, divisor = map(int, input().strip().split())

array = list(map(int, input().strip().split()))
divisibleSumPairs(array, divisor, n_numbers)