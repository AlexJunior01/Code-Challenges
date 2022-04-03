def countApplesAndOranges(s, t, a, b, apples, oranges):
    n_apples = n_oranges = 0

    for apple in apples:
        apple += a
        if s <= apple  and apple <= t:
            n_apples += 1
    
    for orange in oranges:
        orange += b
        if s <= orange and orange <= t:
            n_oranges += 1
    
    print('{}\n{}'.format(n_apples, n_oranges))


house = input().split()
s = int(house[0])
t = int(house[1])

tree = input().split()
a = int(tree[0])
b = int(tree[1])

n_fruits = input().split()
m = int(n_fruits[0])
n = int(n_fruits[1])

apples = list(map(int, input().rstrip().split()))
oranges = list(map(int, input().rstrip().split()))

countApplesAndOranges(s, t, a, b, apples, oranges)
