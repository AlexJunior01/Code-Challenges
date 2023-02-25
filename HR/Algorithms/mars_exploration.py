
def mars_exploration(s: str) -> int:
    letters = {
        0: 'S',
        1: 'O',
        2: 'S'
    }
    changed_letters = 0

    for idx, char in enumerate(s):
        if char != letters[idx%3]:
            changed_letters += 1

    return changed_letters


if __name__ == '__main__':
    s = input()
    result = mars_exploration(s)
    print(result)
