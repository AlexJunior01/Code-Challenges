def plusMinus(arr):
    size_arr = len(arr)
    positive = negative = zero = 0

    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zero += 1
    
    print('{:.6f}'.format(positive/size_arr))
    print('{:.6f}'.format(negative/size_arr))
    print('{:.6f}'.format(zero/size_arr))


n = int(input())

arr = list(map(int, input().rstrip().split()))

plusMinus(arr)