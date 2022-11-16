# greedy

# 首先明确一点，必须得把最下层的给解决了
# 那么问题就转化为了单层最少次数
# 另外，为什么这样就是minim的
# 因为必须得把最下面的先给调整好！
# 然后问题又转化为(N-1)x(N-1)最少需要多少次

import sys


sys.stdin = open("cowtip.in")
sys.stdout = open("cowtip.out", 'w')


def reverse(line, x, y):
    for i in range(x):
        for j in range(y):
            line[i][j] = not line[i][j]


N = int(input())
lines = []
for i in range(N):
    lines.append(list(map(int, list(input()))))

count = 0
for i in range(N)[::-1]:
    for j in range(N)[::-1]:
        if lines[i][j]:
            count += 1
            reverse(lines, i + 1, j + 1)

print(count)