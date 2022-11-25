# 总共两种情况：
# 1.B和L在同行或同列
# 2.B和L在不同行

# 细节的坑在于：
# 同行同列时，R在B和L之间才需要绕道




import sys
sys.stdin = open('buckets.in', 'r')
sys.stdout = open('buckets.out', 'w')

path = []
for i in range(10):
    path.append(input())


ROW = 0
COLUMN = 1

B = None
R = None
L = None

for i in range(10):
    for j in range(10):
        if path[i][j] == 'B':
            B = (i, j)
        elif path[i][j] == 'R':
            R = (i, j)
        elif path[i][j] == 'L':
            L = (i, j)

min_column = min(B[COLUMN], L[COLUMN])
max_column = max(B[COLUMN], L[COLUMN])
min_row = min(B[ROW], L[ROW])
max_row = max(B[ROW], L[ROW])

ans = 0
if B[ROW] == L[ROW]:
    # R在中间才+1
    if R[ROW] == B[ROW] and min_column < R[COLUMN] < max_column:
        ans = abs(B[COLUMN]-L[COLUMN]) + 1
    else:
        ans = abs(B[COLUMN]-L[COLUMN]) - 1
elif B[COLUMN] == L[COLUMN]:
    if R[COLUMN] == B[COLUMN] and min_row < R[ROW] < max_row:
        ans = abs(B[ROW]-L[ROW]) + 1
    else:
        ans = abs(B[ROW]-L[ROW]) - 1
else:
    ans = abs(B[ROW]-L[ROW]) + abs(B[COLUMN]-L[COLUMN]) - 1

print(ans)