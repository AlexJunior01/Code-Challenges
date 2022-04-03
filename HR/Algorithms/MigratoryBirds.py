def migratoryBirds(birds):
    unique_values = unique(birds)
    max_times = result = 0

    for value in unique_values:
        if birds.count(value) > max_times:
            max_times = birds.count(value)
            result = value
    
    print(result)



def unique(array):
    values = []
    for index in array:
        if index not in values:
            values.append(index)
    return sorted(values)


n_birds = int(input())

birds = list(map(int, input().strip().split()))
migratoryBirds(birds)
