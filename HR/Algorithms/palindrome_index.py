ERR_LETF = 'L'
ERR_RIGHT = 'R'
ERR_BOTH = 'B'
CORRECT = 'C'


def search_invalid_index(s, left, right):
    while left <= right:
        if s[left] == s[right]:
            right -= 1
            left += 1
            continue

        if s[left] == s[right-1] and s[right] == s[left+1]:
            return ERR_BOTH, [left, right]

        elif s[left] == s[right-1]:
            return ERR_RIGHT, [left, right]

        else:
            return ERR_LETF, [left, right]

    return CORRECT, [left, right]


def palindrome_index(s:str):
    size = len(s)
    right = size-1
    left = 0

    status, [left, right] = search_invalid_index(s, left, right)

    if status == CORRECT:
        return -1
    elif status == ERR_LETF:
        final_status, _ = search_invalid_index(s, left+1, right)
        if final_status == CORRECT:
            return left
        return -1
    elif status == ERR_RIGHT:
        final_status, _ = search_invalid_index(s, left, right-1)
        if final_status == CORRECT:
            return right
        return -1
    else:
        esq_result, _ = search_invalid_index(s, left + 1, right)
        dir_result, _ = search_invalid_index(s, left, right - 1)

        if esq_result == CORRECT:
            return left
        elif dir_result == CORRECT:
            return right
        else:
            return -1


if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = palindrome_index(s)
        print(result)
