def miniMaxSum(arr):
    sorted_arr = sorted(arr)

    mini = sum(sorted_arr[:4])
    maxi = sum(sorted_arr[1:])

    print(mini, maxi)


arr = list(map(int, input().rstrip().split()))

miniMaxSum(arr)
