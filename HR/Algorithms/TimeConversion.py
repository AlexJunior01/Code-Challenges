def timeConversion(s):
    hour = int(s[:2])
    minute = int(s[3:5])
    second = int(s[6:8])

    if hour != 12 and 'PM' in s:
        hour += 12
    elif hour == 12:
        if 'AM' in s:
            hour = 0
    
    result = '{:02}:{:02}:{:02}'.format(hour, minute, second)
    return result


s = input()

result = timeConversion(s)
print(result)