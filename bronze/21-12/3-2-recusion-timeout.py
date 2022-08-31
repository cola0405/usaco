# 5
# 50层的递归并不是说不可以
# 硬递归不是说不行，但只能过一半的用例

RIGHT = 0
DOWN = 1


def walk(path, row, column, direction, turn, max_turn):
    if turn > max_turn:
        return 0
    if row >= n or column >= n:
        return 0
    if path[row][column] == 'H':
        return 0
    if row == column and row == len(path)-1:
        return 1
    ways = 0
    if direction == RIGHT:
        ways += walk(path, row, column+1, RIGHT, turn, max_turn)
        ways += walk(path, row+1, column, DOWN, turn+1, max_turn)
    elif direction == DOWN:
        ways += walk(path, row, column + 1, RIGHT, turn+1, max_turn)
        ways += walk(path, row + 1, column, DOWN, turn, max_turn)
    return ways



round = int(input())
ans = []
for r in range(round):
    n, k = map(int, input().split(" "))
    path = []

    for row in range(n):
        path.append(list(input()))
    ways = walk(path, 0, 1, RIGHT, 0, k) + walk(path, 1, 0, DOWN, 0, k)
    ans.append(ways)

for i in ans:
    print(i)