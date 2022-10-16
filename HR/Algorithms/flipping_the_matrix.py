
# Q1 = i,       j
# Q2 = i,       size*2-1-j
# Q3 = size*2-1-i,       j
# Q4 = size*2-1-i, size*2-1-j

def flipping_matrix(matrix):
    size = len(matrix)
    last_index = size - 1
    max_sum = 0

    for i in range(size//2):
        for j in range(size//2):
            Q1 = matrix[i][j]
            Q2 = matrix[i][last_index-j]
            Q3 = matrix[last_index-i][j]
            Q4 = matrix[last_index-i][last_index-j]

            max_sum += max([Q1, Q2, Q3, Q4])

    return max_sum


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flipping_matrix(matrix)
        print(result)
