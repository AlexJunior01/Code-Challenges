def hackerrank_in_string(s: str) -> str:
    string = 'hackerrank'
    idx = 0

    for char in s:
        if char == string[idx]:
            idx += 1

        if idx == 10:
            return 'YES'

    return 'NO'


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()
        result = hackerrank_in_string(s)
        print(result)
