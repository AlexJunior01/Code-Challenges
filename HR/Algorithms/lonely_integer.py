def lonely_integer(arr):
    sorted_arr = sorted(arr)
    size = len(arr)

    for idx in range(0, size, 2):
        if idx == size-1:
            return sorted_arr[idx]

        if sorted_arr[idx] != sorted_arr[idx+1]:
            return sorted_arr[idx]


if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = lonely_integer(a)
    print(result)
