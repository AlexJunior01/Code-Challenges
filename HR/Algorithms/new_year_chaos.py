def minimum_bribes(q):
    initial_queue = sorted(q)
    final_queue = q
    begin = 0
    bribes = 0

    for i in range(len(q)):
        aux = 0
        while final_queue[begin] != initial_queue[aux]:
            aux += 1

        if aux > 2:
            print('Too chaotic')
            return

        bribes += aux
        begin += 1
        initial_queue.pop(aux)

    print(bribes)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimum_bribes(q)
