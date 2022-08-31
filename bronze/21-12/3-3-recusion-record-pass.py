# 50层的递归并不是说不可以
# 单单是判断是否进入递归还不够，需要记录
# 其实记录你会了的话，进入递归的条件可以不用做那么多判断，真的影响不大
# 无关紧要的判断前后顺序的影响也不大

RIGHT = 0
DOWN = 1

def walk(path, row, column, direction, turn, max_turn):
    if turn > max_turn:
        return 0
    if path[row][column] == "H":
        return 0
    if record[row][column][turn][direction] != -1:
        return record[row][column][turn][direction]
    if row == column and row == len(path)-1:
        return 1

    ways = 0
    if direction == RIGHT:
        if column+1 < n:
            ways += walk(path, row, column+1, RIGHT, turn, max_turn)
        if row+1 < n and turn < max_turn:
            ways += walk(path, row+1, column, DOWN, turn+1, max_turn)
    elif direction == DOWN:
        if column+1 < n and turn < max_turn:
            ways += walk(path, row, column+1, RIGHT, turn+1, max_turn)
        if row+1 < n :
            ways += walk(path, row+1, column, DOWN, turn, max_turn)
    record[row][column][turn][direction] = ways
    return ways



round = int(input())
ans = []
for r in range(round):
    n, k = map(int, input().split(" "))
    path = []
    record = [[[[-1 for _ in range(2)] for _ in range(k + 1)] for _ in range(50)] for _ in range(50)]

    for row in range(n):
        path.append(list(input()))
    ways = walk(path, 0, 1, RIGHT, 0, k) + walk(path, 1, 0, DOWN, 0, k)
    ans.append(ways)

for i in ans:
    print(i)