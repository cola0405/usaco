# 看到走迷宫就怕
# 不存在while+递归

RIGHT = 0
DOWN = 1

def walk(path, row, column, n, direction, turn, max_turn):
    if turn > max_turn:
        return 0
    if path[row][column] == 'H':
        return 0
    if row == n or column == n:
        return 0
    if row == column and row == n-1:
        return 1
    tmp_column = column
    tmp_turn = turn
    ans = 0

    # right direction
    while column < n and path[row][column] != 'H':
        # 模拟移动不能算ans
        if row != n-1:
            if path[row+1][column] != 'H':
                if direction == DOWN:
                    ans += walk(path, row + 1, column, n, DOWN, turn, k)
                else:
                    ans += walk(path, row + 1, column, n, DOWN, turn + 1, k)
        if direction == DOWN:
            column += 1
            turn += 1
        else:
            column += 1


    column = tmp_column
    turn = tmp_turn
    # down direction
    while row < n and path[row][column] != 'H':
        if column != n - 1:
            if path[row][column+1] != 'H':
                if direction == RIGHT:
                    ans += walk(path, row, column+1, n, RIGHT, turn, k)
                else:
                    ans += walk(path, row, column+1, n, RIGHT, turn + 1, k)
        if direction == RIGHT:
            turn += 1
            row += 1
        else:
            row += 1
    return ans



round = int(input())
ans = []
for r in range(round):
    n, k = map(int, input().split(" "))
    path = []

    for row in range(n):
        path.append(list(input()))
    ans.append(walk(path, 0, 1, n, RIGHT, 0, k)+walk(path, 1, 0, n, DOWN, 0, k))


for i in ans:
    print(i)