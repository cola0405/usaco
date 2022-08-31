# 50层的递归并不是说不可以
# 单单是判断是否进入递归还不够，需要记录
# 其实记录你会了的话，进入递归的条件可以不用做那么多判断，真的影响不大
# 无关紧要的判断前后顺序的影响也不大
# for循环里的变量也是全局

RIGHT = 0
DOWN = 1

def walk(row, column, direction, turn):
    if turn > k:
        return 0
    # 一定要检查当前！
    if path[row][column] == "H":
        return 0

    # record
    # 如果之前有记录，则直接取，不往下递归了
    if record[row][column][turn][direction] != -1:
        return record[row][column][turn][direction]
    if row == column and row == len(path)-1:
        return 1

    ways = 0
    # 当前是right方向
    if direction == RIGHT:
        if column+1 < n:
            ways += walk(row, column+1, RIGHT, turn)
        if row+1 < n and turn < k:
            ways += walk(row+1, column, DOWN, turn+1)

    # 当前是down方向
    elif direction == DOWN:
        if column+1 < n and turn < k:
            ways += walk(row, column+1, RIGHT, turn+1)
        if row+1 < n :
            ways += walk(row+1, column, DOWN, turn)
    record[row][column][turn][direction] = ways
    return ways



round = int(input())
ans = []
for r in range(round):
    n, k = map(int, input().split(" "))
    path = []
    # record[row][column][turn][direction]
    # 到(row, column)位置，且对应turn、direction时的方案数
    record = [[[[-1 for _ in range(2)] for _ in range(k+1)] for _ in range(n)] for _ in range(n)]

    for row in range(n):
        path.append(list(input()))
    ways = walk(0, 1, RIGHT, 0) + walk(1, 0, DOWN, 0)
    ans.append(ways)

for i in ans:
    print(i)