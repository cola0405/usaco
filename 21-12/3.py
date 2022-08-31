# 看到走迷宫就怕

# while 走迷宫
# 终止条件：1.没路走了；2.
# 一次转向放到一个function里面！
# 注意到有条件(1≤K≤3)，是个提示！
# 这里是可以递归的

# 两个while循环，一个左，一个下，每个循环里边用递归

def walk(path, row, column, n, turn, max_turn):
    if turn > max_turn:
        return 0
    if path[row][column] == 'H':
        return 0
    if row == column and row == n-1:
        return 1
    tmp = column
    ans = 0

    while column < n-1 and row < n-1:
        if path[row+1][column] != 'H':
            ans += walk(path, row+1, column, n, turn+1, k)
        else:
            break
        column += 1

    column = tmp
    while column < n-1 and row < n-1:
        if path[row][column+1] != 'H':
            ans += walk(path, row, column+1, n, turn+1, k)
        else:
            break
        row += 1
    return ans



round = int(input())
ans = []
for r in range(round):
    n, k = map(int, input().split(" "))
    path = []

    for row in range(n):
        path.append(list(input()))
    ans.append(walk(path, 0, 1, n, 0, k) + walk(path, 1, 0, n, 0, k))


for i in ans:
    print(i)