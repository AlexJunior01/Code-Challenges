
def how_many_games(p, d, m, s):
    total_games = 0
    actual_price = p
    reach_minimum = False

    while True:
        if actual_price > s:
            break

        total_games += 1
        s -= actual_price

        if not reach_minimum:
            actual_price -= d
            if actual_price <= m:
                actual_price = m
                reach_minimum = True

    return total_games


if __name__ == '__main__':
    first_game_price = 20
    discount = 3
    minimum_cost = 6
    budget = 80

    res = how_many_games(first_game_price, discount, minimum_cost, budget)
    print(res)
