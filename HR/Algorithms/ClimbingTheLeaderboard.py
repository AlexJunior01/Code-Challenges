def climbingLeaderboard(ranked, player):
    ranked = list(set(ranked))
    ranked.sort(reverse=True)
    result = list()
    rank= len(ranked) - 1

    for score in player:
        while score > ranked[rank] and rank > 0:
            rank -= 1

        if score < ranked[rank]:
            result.insert(0, rank+2)
        else:
            result.insert(0, rank+1)

    for rank in result[::-1]:
        print(rank)


ranked_count = int(input().strip())
ranked = list(map(int, input().rstrip().split()))
player_count = int(input().strip())
player = list(map(int, input().rstrip().split()))
climbingLeaderboard(ranked, player)