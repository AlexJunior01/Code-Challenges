from typing import List, Tuple


def get_combinations(s: set) -> List[Tuple]:
    list_s = list(s)
    combinations = list()
    size = len(list_s)

    for i in range(size):
        for j in range(i+1, size):
            combinations.append((list_s[i], list_s[j]))

    return combinations


def check_string(new_s: list, combination: Tuple) -> bool:
    index = 0 if new_s[0] == combination[0] else 1
    first = new_s[0]

    for char in new_s:
        if char != combination[index]:
            return False
        index = (index + 1) % 2

    return True


def alternate(s: str) -> int:
    set_s = set(s)
    combinations = get_combinations(set_s)
    current_max = 0

    for combination in combinations:
        new_s = [char for char in s if char in combination]
        if check_string(new_s, combination) and len(new_s) > current_max:
            current_max = len(new_s)

    return current_max


if __name__ == '__main__':
    l = int(input().strip())
    s = input()
    result = alternate(s)
    print(result)