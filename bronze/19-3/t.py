import sys
sys.stdin = open('buckets1.in', 'r')
sys.stdout = open('buckets1.out', 'w')

path = []
for i in range(3):
    path.append(input())
# for i in range(3):
#     path.append(input())

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
    # if i >= 3 or i < 0 \
    if row >= 3 or row < 0 \
            or column < 0 or column >= 3\
            or path[row][column] == 'R'\
            or path[row][column] == 'L':
        return 999
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
for i in range(3):
    for j in range(3):
        if path[i][j] == 'L':
            flag[i][j][0] = EXPLORED
            ans1 = dfs(i+1, j ,0)
            ans2 = dfs(i-1, j, 0)
            ans3 = dfs(i, j+1, 0)
            ans4 = dfs(i, j-1, 0)
            ans = min(ans1,ans2,ans3,ans4)
            break

print(ans)



