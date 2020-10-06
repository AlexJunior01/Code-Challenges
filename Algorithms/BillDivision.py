def billDivision(bill, item_anna, pay_anna):
    amount = sum(bill)
    amount -= bill[item_anna]
    amount /= 2

    if amount == pay_anna:
        print('Bon Appetit')
    else:
        print(int(pay_anna - amount))



nk = input().split()
n = int(nk[0])
k = int(nk[1])
bill = list(map(int, input().split()))
b = int(input())

billDivision(bill, k, b)

