def n_pairs(socks):
    pairs = {}
    result = 0
    for sock in socks:
        if str(sock) in pairs:
            pairs[str(sock)] += 0.5
        else:
            pairs[str(sock)] = 0.5
    
    for value in pairs.values():
        result += int(value)

    return result


n_socks = int(input())
socks = list(map(int, input().split()))
result = n_pairs(socks)
print(result)