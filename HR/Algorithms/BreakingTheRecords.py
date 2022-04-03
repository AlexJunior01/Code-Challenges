def breakingTheRecords(scores):
    min_score = max_score = scores[0]
    
    n_min = n_max = 0

    for score in scores:
        if score > max_score:
            max_score = score
            n_max += 1
        elif score < min_score:
            min_score = score
            n_min += 1
    
    print(n_max, n_min, sep=' ')
    


n_games = int(input())

scores = list(map(int, input().rstrip().split()))
breakingTheRecords(scores)