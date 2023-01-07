ESPECIAL_CHAR = '!@#$%^&*()-+'
MIN_SIZE = 6


def password_has_number(password:str):
    for char in password:
        if char.isnumeric():
            return True

    return False


def password_has_especial_char(password:str):
    for char in password:
        if char in ESPECIAL_CHAR:
            return True

    return False


def password_has_uppercase(password:str):
    for char in password:
        if 97 <= ord(char) <= 122:
            return True

    return False


def password_has_lowercase(password:str):
    for char in password:
        if 65 <= ord(char) <= 90:
            return True

    return False


def minimum_number(n, password):
    missing_constraints = 0
    pass_len = len(password)

    if not password_has_lowercase(password):
        missing_constraints += 1

    if not password_has_uppercase(password):
        missing_constraints += 1

    if not password_has_especial_char(password):
        missing_constraints += 1

    if not password_has_number(password):
        missing_constraints += 1

    return max([missing_constraints, MIN_SIZE-pass_len])


if __name__ == '__main__':
    n = int(input().strip())
    password = input()
    answer = minimum_number(n, password)
    print(answer)
