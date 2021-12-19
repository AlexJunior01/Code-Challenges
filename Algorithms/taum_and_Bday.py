def taum_bday(b, w, bc, wc, z):
    if abs(bc - wc) < z:
        total = b*bc + w*wc
    else:
        if bc < wc:
            total = b*bc + w * (bc + z)
        else:
            total = w*wc + b * (wc + z)

    return total


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        b = int(first_multiple_input[0])
        w = int(first_multiple_input[1])

        second_multiple_input = input().rstrip().split()
        bc = int(second_multiple_input[0])
        wc = int(second_multiple_input[1])
        z = int(second_multiple_input[2])

        result = taum_bday(b, w, bc, wc, z)
        print(result)
