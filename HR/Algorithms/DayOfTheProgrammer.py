def dayOfProgrammer(year):
    day = ''
    if year < 1918:
        if year % 4 == 0:
            day = '12.09.{}'.format(year)
        else:
            day = '13.09.{}'.format(year)
    elif year > 1918:
        if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
            day = '12.09.{}'.format(year)
        else:
            day = '13.09.{}'.format(year)
    else:
        day = '26.09.{}'.format(year)
    
    return day


year = int(input())

result = dayOfProgrammer(year)
print(result)