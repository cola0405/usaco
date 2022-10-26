# 自己是#时不可以
# 规则仔细看
# 水平：左边是边界或#，右边两个是.
# 竖直：上边是边界或#，下边两个是.

import sys
sys.stdin = open('crosswords.in', 'r')
sys.stdout = open('crosswords.out', 'w')

n, m = map(int, input().split())
path = []
for i in range(n):
    path.append(input())


def isClue(row, column):
    if path[row][column] == '#':
        return False

    # horizontal
    if column < m-2 \
            and (column == 0 or path[row][column - 1] == '#') \
            and (path[row][column + 1] == '.' and path[row][column + 2] == '.'):
        return True

    # vertical
    if row < n-2\
            and (row == 0 or path[row - 1][column] == '#') \
            and (path[row + 1][column] == '.' and path[row + 2][column] == '.'):
        return True

    return False


ans = 0
pos = []
for i in range(n):
    for j in range(m):
        if isClue(i,j):
            ans += 1
            pos.append((i+1,j+1))

print(ans)
for i,j in pos:
    print(i,j)

