
def find_median(arr):
    sorted_arr = sorted(arr)
    size = len(arr)
    result = 0
    if size % 2 == 0:
        x1 = sorted_arr[size//2]
        x2 = sorted_arr[(size // 2) + 1]
        result = (x1+x2) // 2
    else:
        result = sorted_arr[size//2]

    return result


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = find_median(arr)
    print(result)

# 0 1 2 3 4 5 6
# 0 1 2 3 4 5
