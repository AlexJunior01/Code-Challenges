def minimum_distances(arr) -> int:
    first_occur = dict()
    actual_min_dist = 10_000_000

    for idx, x in enumerate(arr):
        first_index = first_occur.get(x)
        if first_index is not None:
            pair_dist = idx-first_index
            actual_min_dist = pair_dist if pair_dist < actual_min_dist else actual_min_dist
        else:
            first_occur[x] = idx

    if actual_min_dist == 10_000_000:
        actual_min_dist = -1

    return actual_min_dist


if __name__ == '__main__':
    a = [1, 1]
    result = minimum_distances(a)
    print(result)
