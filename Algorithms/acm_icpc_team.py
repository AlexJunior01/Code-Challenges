def count_unique_topics(person1, person2, qtd_topicos):
    team_topics = 0
    for i in range(qtd_topicos):
        if (person1[i] == '1') or (person2[i] == '1'):
            team_topics += 1

    return team_topics


def acm_team(topic):
    qtd_topics = len(topic[0])
    qtd_pessoas = len(topic)
    max_topics = 0
    qtd_teams = 0

    for i in range(qtd_pessoas):
        for j in range(i+1, qtd_pessoas):
            duple = count_unique_topics(topic[i], topic[j], qtd_topics)
            if duple > max_topics:
                max_topics = duple
                qtd_teams = 1
            elif duple == max_topics:
                qtd_teams += 1

    return [max_topics, qtd_teams]


if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acm_team(topic)
    print(result[0])
    print(result[1])
