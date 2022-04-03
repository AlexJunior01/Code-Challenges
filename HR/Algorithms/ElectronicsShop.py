def getMoneySpent(keyboards, drives, b):
    result = -1

    for kb in keyboards:
        for drive in drives:
            if kb+drive <= b and kb+drive > result:
                result = kb+drive
    
    return result



bnm = input().split()
b = int(bnm[0])
n = int(bnm[1])
m = int(bnm[2])
keyboards = list(map(int, input().rstrip().split()))
drives = list(map(int, input().rstrip().split()))

moneySpent = getMoneySpent(keyboards, drives, b)
print(moneySpent)