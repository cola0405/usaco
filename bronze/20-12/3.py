# 考读题
# 题目有两个很重要的信息点
# 1.只有N和E走向
# 2.如果两头牛同时走到一块草地，则共享吃那块草地，不停

# 可按照从下到上、从左到右的顺序分别处理E和N方向的牛
# 按顺序check的话，可以最快发现被迫stop的牛

# 举个例子：从下往上检查E方向的牛
# 检查步骤：
# 1.先利用x、y确定有无可能会碰撞
# 2.检查该牛有没有被之前的E牛阻拦（足矣）

N = []
E = []
ans = dict()
n = int(input())
for i in range(n):
    direction, x, y = input().split()
    point = (int(x),int(y))
    if direction == 'N':
        N.append(point)
    else:
        E.append(point)
    ans[point] = 0

# N牛按照x从小到大排列
def sort_for_N(pair):
    return pair[0]

# E牛按照y从小到大排列
def sort_for_E(pair):
    return pair[1]

N.sort(key=sort_for_N)
E.sort(key=sort_for_E)

for i in range(len(E)):
    i_x, i_y = E[i]
    for j in range(len(N)):
        j_x, j_y = N[j][0], N[j][1]
        # 判断有无碰撞的可能
        if j_y > i_y or j_x < i_x:
            continue
        # 看看这个N牛此前有没有提前stop
        if len(N[j]) > 2 and j_y+N[j][2] < i_y:
            continue
        x_gap = j_x - i_x
        y_gap = i_y - j_y
        if x_gap > y_gap:
            ans[(i_x, i_y)] = x_gap
            E[i] = (i_x, i_y, x_gap)
            break
        elif x_gap == y_gap:
            continue
        else:
            # N牛被阻挡了，记录已走路程
            N[j] = (j_x, j_y, y_gap)
    else:
        ans[(i_x, i_y)] = 'Infinity'

for i in range(len(N)):
    i_x, i_y = N[i][0], N[i][1]
    for j in range(len(E)):
        if len(E[j]) > 2 and E[j][0]+E[j][2] < i_x:
            continue
        j_x, j_y = E[j][0], E[j][1]
        if j_y < i_y or j_x > i_x:
            continue
        x_gap = i_x - j_x
        y_gap = j_y - i_y
        if y_gap > x_gap:
            ans[(i_x,i_y)] = y_gap
            break
        elif x_gap == y_gap:
            continue
    else:
        ans[(i_x,i_y)] = 'Infinity'


for i in ans.values():
    print(i)







