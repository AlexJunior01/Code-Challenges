
# a -> 97
# z -> 122
# A -> 65
# Z -> 90

def cipher_character(c, k):
    if not c.isalpha():
        return c

    is_minisculo = 97 <= ord(c) <= 122
    ciphed_char = ord(c) + k

    if is_minisculo:
        ciphed_char = chr(ciphed_char) if ciphed_char <= 122 else chr(ciphed_char-26)
    else:
        ciphed_char = chr(ciphed_char) if ciphed_char <= 90 else chr(ciphed_char - 26)

    return ciphed_char


def caesar_cipher(s, k):
    real_k = k % 26
    new_text = [cipher_character(letter, real_k) for letter in s]

    return ''.join(new_text)


if __name__ == '__main__':
    n = int(input().strip())
    s = input()
    k = int(input().strip())
    result = caesar_cipher(s, k)

    print(result)
