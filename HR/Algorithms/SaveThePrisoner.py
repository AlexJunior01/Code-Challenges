def saveThePrisoner(n, m, s):
    m = m % n

    # Stop behind
    if m == 0:
        if s-1 == 0:
            return n
        return s-1

    # Stop forward
    if m-1+s <= n:
        return s+m-1

    # Stop backward
    if m-1+s > n:
        m = m - (n - s + 1)
        return m

    
t = int(input())
for t_itr in range(t):
    nms = input().split()
    n = int(nms[0])
    m = int(nms[1])
    s = int(nms[2])
    result = saveThePrisoner(n, m, s)
    print(result)