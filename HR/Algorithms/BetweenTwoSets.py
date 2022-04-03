def getTotalX(a, b):
    total = 0
    for i in range(a[-1], b[0]+1):
        is_between = True

        # First set
        for n in a:
            if i % n != 0:
                is_between = False
                break
        
        # Second set
        for n in b:
            if n % i != 0:
                is_between = 0
                break
        
        if is_between == 1:
            total += 1
    
    return total


first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
arr = list(map(int, input().rstrip().split()))
brr = list(map(int, input().rstrip().split()))
total = getTotalX(arr, brr)
print(total)