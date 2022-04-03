def print_statistics(dict_threes, n_threes, with_last_enter=True):
    sorted_keys = sorted(dict_threes.keys())
    size = len(dict_threes)
    for index, three in enumerate(sorted_keys):
        v = dict_threes[three] / n_threes * 100
        print(f"{three} {v:.4f}")

    if with_last_enter:
        print()


def main():
    n_cases = int(input())
    input()
    n_threes = 0
    threes = dict()

    while True:
        try:
            three = input()
        except EOFError:
            print_statistics(threes, n_threes, False)
            break

        if not three:
            n_cases -= 1
            if n_cases == 0:
                print_statistics(threes, n_threes, False)
                break
            print_statistics(threes, n_threes, True)
            threes.clear()
            n_threes = 0
            continue

        counter = threes.get(three)
        if counter:
            threes[three] += 1
        else:
            threes[three] = 1

        n_threes += 1


if __name__ == '__main__':
    main()
