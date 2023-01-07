
def truck_tour(petrolpumps):
    current_fuel = 0
    min_index = 0

    for index, [qtd, dist] in enumerate(petrolpumps):
        current_fuel += qtd
        if current_fuel < dist:
            current_fuel = 0
            min_index = index + 1
        else:
            current_fuel -= dist

    return min_index


if __name__ == '__main__':
    n = int(input().strip())
    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truck_tour(petrolpumps)
    print(result)
