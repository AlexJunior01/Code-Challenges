
def service_lane(widths, cases):
    for entry, exit_ in cases:
        print(min(widths[entry:exit_ + 1]))


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    service_lane(width, cases)
