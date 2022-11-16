# 自己是#时不可以
# 规则仔细看
# 水平：左边是边界或#，右边两个是.
# 竖直：上边是边界或#，下边两个是.

# +1 +2 时一定要做好边界检查

import sys

sys.stdin = open('crosswords.in', 'r')
sys.stdout = open('crosswords.out', 'w')

n, m = map(int, input().split())
path = []
for i in range(n):
    path.append(input())


def isClue(path, row, column):
    if path[row][column] == '#':
        return False

    # horizontal
    # no need to check column-1
    if (column == 0 or path[row][column - 1] == '#') \
            and column + 2 < m and path[row][column + 1] == '.' \
            and path[row][column + 2] == '.':
        return True

    # vertical
    if (row == 0 or path[row - 1][column] == '#') \
            and row + 2 < n and path[row + 1][column] == '.' \
            and path[row + 2][column] == '.':
        return True
    return False


ans = []
for row in range(n):
    for column in range(m):
        if isClue(path, row, column):
            ans.append((row + 1, column + 1))

print(len(ans))
for i in ans:
    print(i[0], i[1])