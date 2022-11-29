# exactly 3
# 新加入的牛可能会导致之前舒服的牛变得不舒服


# 一对一对地破坏

border = 1000
COMFORTABLE = 2

n = int(input())
pasture = []
for i in range(1001):
    pasture.append([0]*1001)

def up(x,y):
    if x-1 >= 0 and pasture[x-1][y] == 1:
        return 1
    elif x-1 >= 0 and pasture[x-1][y] == COMFORTABLE:
        global ans
        ans -= 1
        pasture[x - 1][y] = 1
    return 0

def down(x,y):
    if x+1 <= border and pasture[x+1][y] == 1:
        return 1
    elif x+1 <= border and pasture[x+1][y] == COMFORTABLE:
        global ans
        ans -= 1
        pasture[x + 1][y] = 1
    return 0

def left(x,y):
    if y-1 >= 0 and pasture[x][y-1] == 1:
        return 1
    elif y-1 >= 0 and pasture[x][y-1] == COMFORTABLE:
        global ans
        ans -= 1
        pasture[x][y - 1] = 1
    return 0

def right(x,y):
    if y+1 <= border and pasture[x][y+1] == 1:
        return 1
    elif y+1 <= border and pasture[x][y+1] == COMFORTABLE:
        global ans
        ans -= 1
        pasture[x][y + 1] = 1
    return 0


ans = 0
for i in range(n):
    x,y = list(map(int, input().split()))
    pasture[x][y] = 1
    count = up(x, y) + down(x, y) + left(x, y) + right(x, y)
    if count == 3:
        pasture[x][y] = COMFORTABLE
        ans += 1
    print(ans)

