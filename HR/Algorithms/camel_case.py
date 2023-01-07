def is_capital_letter(letter):
    return 65 <= ord(letter) <= 90


def camel_case(s):
    qtd_words = 1

    for letter in s:
        if is_capital_letter(letter):
            qtd_words += 1

    return qtd_words


if __name__ == '__main__':
    s = input()
    result = camel_case(s)
    print(result)
