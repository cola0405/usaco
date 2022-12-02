# exactly 3，周围邻接的有三个
# “T”型，中间交界点就是comfortable
# 想抱团但是不想被围住，谓之中间交界点就是comfortable

# 新加入的牛可能会导致之前舒服的牛变得不舒服
# 也可能会让它们变得舒服

# 便利的同时检查可能会影响到的点

# 2832ms

# http://www.usaco.org/current/data/sol_prob2_bronze_feb21.html

border = 1000
COMFORTABLE = 2

n = int(input())
pasture = []
for i in range(1001):
    pasture.append([0]*1001)

def up(x, y):
    if x-1 >= 0 and pasture[x-1][y] >= 1:
        pasture[x-1][y] += 1
        global ans
        if pasture[x-1][y] == 4:
            ans += 1
        if pasture[x-1][y] == 5:
            ans -= 1
        return 1
    return 0

def down(x, y):
    if x+1 <= border and pasture[x+1][y] >= 1:
        pasture[x+1][y] += 1
        global ans
        if pasture[x+1][y] == 4:
            ans += 1
        if pasture[x+1][y] == 5:
            ans -= 1
        return 1
    return 0

def left(x, y):
    if y-1 >= 0 and pasture[x][y-1] >= 1:
        pasture[x][y-1] += 1
        global ans
        if pasture[x][y-1] == 4:
            ans += 1
        if pasture[x][y-1] == 5:
            ans -= 1
        return 1
    return 0

def right(x, y):
    if y+1 <= border and pasture[x][y+1] >= 1:
        pasture[x][y+1] += 1
        global ans
        if pasture[x][y+1] == 4:
            ans += 1
        if pasture[x][y+1] == 5:
            ans -= 1
        return 1
    return 0


ans = 0
for i in range(n):
    x, y = list(map(int, input().split()))
    pasture[x][y] = 1
    count = up(x, y) + down(x, y) + left(x, y) + right(x, y)
    pasture[x][y] += count
    if count == 4:
        ans += 1
    print(ans)

