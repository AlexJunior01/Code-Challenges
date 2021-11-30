def repeated_string(s, n):
    qtd_a = s.count('a')
    size_s = len(s)
    complete_repeated = int(n/size_s)

    qtd_a *= complete_repeated

    for i in range(n % size_s):
        if s[i] == 'a':
            qtd_a += 1

    return qtd_a


if __name__ == "__main__":
    s = input()

    n = int(input().strip())

    result = repeated_string(s, n)
    print(result)
