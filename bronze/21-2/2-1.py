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

def check_vertical(dx):
    if 0 <= x+dx <= border and pasture[x+dx][y] >= 1:
        pasture[x+dx][y] += 1
        global ans
        if pasture[x+dx][y] == 4:
            ans += 1
        if pasture[x+dx][y] == 5:
            ans -= 1
        return 1
    return 0

def check_horizontal(dy):
    if 0 <= y+dy <= border and pasture[x][y+dy] >= 1:
        pasture[x][y+dy] += 1
        global ans
        if pasture[x][y+dy] == 4:
            ans += 1
        if pasture[x][y+dy] == 5:
            ans -= 1
        return 1
    return 0


ans = 0
for i in range(n):
    x, y = list(map(int, input().split()))
    pasture[x][y] = 1
    count = check_horizontal(1) + check_horizontal(-1)
    count += check_vertical(1) + check_vertical(-1)
    pasture[x][y] += count
    if count == 4:
        ans += 1
    print(ans)
