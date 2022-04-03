
def get_initial_moves(n, r_q, c_q):
    r_moves = n - c_q
    l_moves = (n-1) - r_moves

    t_moves = n - r_q
    b_moves = (n-1) - t_moves

    tr_moves = min([n-r_q, n-c_q])
    br_moves = min([r_q-1, n-c_q])
    bl_moves = min([r_q-1, c_q-1])
    tl_moves = min([c_q-1, n-r_q])

    movs_without_enemys = {"t": t_moves, "tr": tr_moves, "r": r_moves, "br": br_moves,
                           "b": b_moves, "bl": bl_moves, "l": l_moves, "tl": tl_moves}

    return movs_without_enemys


def get_moves_with_enemys(initial_moves, enemys, rq, cq):
    for enemy in enemys:
        abs_dist_col = abs(enemy[1] - cq)
        abs_dist_row = abs(enemy[0] - rq)
        col_dist = enemy[1] - cq
        row_dist = enemy[0] - rq
        # Esta em uma diagonal
        if abs_dist_row == abs_dist_col:
            if row_dist > 0 and col_dist > 0:
                initial_moves["tr"] = min([initial_moves["tr"], abs_dist_row-1])
            elif row_dist < 0 and col_dist > 0:
                initial_moves["br"] = min([initial_moves["br"], abs_dist_row-1])
            elif row_dist < 0 and col_dist < 0:
                initial_moves["bl"] = min([initial_moves["bl"], abs_dist_row-1])
            else:
                initial_moves["tl"] = min([initial_moves["tl"], abs_dist_row - 1])
        # Esta na mesma linha
        elif r_q == enemy[0]:
            if col_dist > 0:
                initial_moves["r"] = min([initial_moves["r"], abs_dist_col-1])
            else:
                initial_moves["l"] = min([initial_moves["l"], abs_dist_col - 1])
        # Esta na mesma coluna
        elif c_q == enemy[1]:
            if row_dist > 0:
                initial_moves["t"] = min([initial_moves["r"], abs_dist_row - 1])
            else:
                initial_moves["b"] = min([initial_moves["b"], abs_dist_row - 1])

    return initial_moves


def queens_attack(n, k, r_q, c_q, obstacles):
    movs_without_enemys = get_initial_moves(n, r_q, c_q)
    final_moves = get_moves_with_enemys(movs_without_enemys, obstacles, r_q, c_q)

    qtd_moves = 0
    for value in final_moves.values():
        qtd_moves += value

    return qtd_moves


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()
    r_q = int(second_multiple_input[0])
    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queens_attack(n, k, r_q, c_q, obstacles)
    print(result)
