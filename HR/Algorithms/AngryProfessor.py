def angryProfessor(k, a):
    counter = 0
    for student in  a:
        if student <= 0:
            counter += 1
    
    if counter >= k:
        return 'NO'
    
    return 'YES'


t = int(input())

for t_itr in range(t):
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    a = list(map(int, input().rstrip().split()))
    result = angryProfessor(k, a)
    print(result)