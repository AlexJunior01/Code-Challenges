def get_column(matrix, column_index, size):
    column = []
    for row in range(size):
        column.append(matrix[row][column_index])

    return column


def grid_challenge(grid):
    size_matrix = len(grid)
    size_words = len(grid[0])

    for i in range(size_words):
        column = get_column(grid, i, size_matrix)
        if column != sorted(column):
            return 'NO'

    return 'YES'


if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        grid = []
        for _ in range(n):
            grid_item = input()
            grid.append(sorted(grid_item))

        result = grid_challenge(grid)

        print(result)
