# step三维数组剪枝
# 10x10大不好debug的话，可以把grid缩小方便debug

import sys
sys.stdin = open('buckets.in', 'r')
sys.stdout = open('buckets.out', 'w')

path = []
for i in range(10):
    path.append(input())

# 构造三维record
flag = []
for i in range(10):
    t2 = []
    for j in range(10):
        t1 = []
        for step in range(100):
            t1.append(999)
        t2.append(t1)
    flag.append(t2)

EXPLORED = 1

def dfs(row,column,step):
    if row >= 10 or row < 0 \
            or column < 0 or column >= 10\
            or path[row][column] == 'R'\
            or path[row][column] == 'L'\
            or flag[row][column] == EXPLORED:
        return 999
    # 三维step剪枝
    # 如果之前更少的step已经走过这里了
    # 那就没必要继续dfs了
    for k in range(step):
        if step >= 100 or flag[row][column][step] != 999:
            return 999

    if path[row][column] == 'B':
        return step
    if path[row][column] == '.':
        flag[row][column][step] = EXPLORED
        ans1 = dfs(row+1, column, step+1)
        ans2 = dfs(row-1, column, step+1)
        ans3 = dfs(row, column+1, step+1)
        ans4 = dfs(row, column-1, step+1)
        ans = min(ans1,ans2,ans3,ans4)
    return ans

ans = 0
for i in range(10):
    for j in range(10):
        if path[i][j] == 'L':
            flag[i][j][0] = EXPLORED
            ans1 = dfs(i+1, j, 0)
            ans2 = dfs(i-1, j, 0)
            ans3 = dfs(i, j+1, 0)
            ans4 = dfs(i, j-1, 0)
            ans = min(ans1,ans2,ans3,ans4)
            break

print(ans)



