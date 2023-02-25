
ASCII_A = ord('a')
ASCII_Z = ord('z')


def pangrams(s: str) -> str:
    letters = set([chr(i) for i in range(ASCII_A, ASCII_Z+1)])
    unique_letters = set([letter for letter in s.lower() if letter.isalpha()])

    if letters == unique_letters:
        return 'pangram'

    return 'not pangram'


if __name__ == '__main__':
    s = input()
    result = pangrams(s)
    print(result)
