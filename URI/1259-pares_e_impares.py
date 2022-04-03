number_of_inputs = int(input())
pairs = list()
odd = list()

for inputs in range(0, number_of_inputs):
    number = int(input())
    if number % 2 == 0:
        pairs.append(number)
    else:
        odd.append(number)

pairs = sorted(pairs)
odd = sorted(odd, reverse=True)

for number in pairs:
    print(number)

for number in odd:
    print(number)
