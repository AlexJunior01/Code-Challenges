def libraryFine(d1, m1, y1, d2, m2, y2):
    hackos = 0
    y = y1-y2
    m = m1-m2
    d = d1-d2

    if y > 0:
        hackos = 10000
    elif y == 0 and m > 0:
        hackos = m*500 
    elif y==0 and m==0 and d > 0:
        hackos = d*15
    
    return hackos


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    d1 = int(first_multiple_input[0])
    m1 = int(first_multiple_input[1])
    y1 = int(first_multiple_input[2])

    second_multiple_input = input().rstrip().split()
    d2 = int(second_multiple_input[0])
    m2 = int(second_multiple_input[1])
    y2 = int(second_multiple_input[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)
    print(result)