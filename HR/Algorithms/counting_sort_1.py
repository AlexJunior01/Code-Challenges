def counting_sort(arr):
    frequency_arr = [0 for i in range(100)]

    for number in arr:
        frequency_arr[number] += 1

    return frequency_arr


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = counting_sort(arr)
    print(result)


