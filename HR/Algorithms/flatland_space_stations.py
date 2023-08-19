# 7 3
# c [0, 2, 5]

# i     0 1 2 3 4 5 6
# dist  0 1 0 1 1 0 1


# idx_next  0 1 2 -1
# idx_prev -1 0 1 2


def update_state(current_idx, last_idx, idx_next_station, idx_previous_station, stations):
    if current_idx == stations[idx_next_station]:
        idx_previous_station += 1

        if idx_next_station < last_idx:
            idx_next_station += 1
        else:
            idx_next_station = -1

    return idx_previous_station, idx_next_station


def flatland_space_stations(number_of_cities, cities_with_space_stations):
    cities_with_space_stations.sort()
    last_idx = len(cities_with_space_stations) - 1

    max_distance = -1
    idx_next_station = 0
    idx_previous_station = -1

    for city in range(number_of_cities):
        if idx_previous_station == -1:
            dist = abs(city - cities_with_space_stations[idx_next_station])

        elif idx_next_station == -1:
            dist = abs(city - cities_with_space_stations[idx_previous_station])

        else:
            dist_previous = abs(city - cities_with_space_stations[idx_previous_station])
            dist_next = abs(city - cities_with_space_stations[idx_next_station])
            dist = min([dist_next, dist_previous])

        max_distance = max([max_distance, dist])
        idx_previous_station, idx_next_station = update_state(
            city,
            last_idx,
            idx_next_station,
            idx_previous_station,
            cities_with_space_stations
        )

    return max_distance


if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    c = list(map(int, input().rstrip().split()))

    result = flatland_space_stations(n, c)
    print(result)
