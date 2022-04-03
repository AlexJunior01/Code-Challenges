def cutTheSticks(arr):
    stick_sizes = [0 for i in range(1000)]
    result = []
    bigger_stick = 0
    for i in arr:
        if i > bigger_stick:
            bigger_stick = i
        stick_sizes[i] += 1


    index = 0
    remains_sticks = len(arr)

    while True:
        if index > bigger_stick:
            break
        if stick_sizes[index] != 0:
            result.append(remains_sticks)
            remains_sticks -= stick_sizes[index]
            index += 1
        else:
            index += 1
        
    return result



entry1 = [1, 2, 3, 4, 3, 3, 2, 1]
entry2 = [5, 4, 4, 2, 2, 8]
result = cutTheSticks(entry2)
[print(i) for i in result]