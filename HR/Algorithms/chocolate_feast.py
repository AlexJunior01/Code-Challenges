def chocolate_feast(money_spent, cost, wrappers_tax):
    total_bars = current_wrappers = money_spent/cost

    while True:
        if current_wrappers >= wrappers_tax:
            new_bars = current_wrappers // wrappers_tax
            current_wrappers = current_wrappers % wrappers_tax
            total_bars += new_bars
            current_wrappers += new_bars
        else:
            break

    return int(total_bars)


if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        c = int(first_multiple_input[1])
        m = int(first_multiple_input[2])

        result = chocolate_feast(n, c, m)
        print(result)
