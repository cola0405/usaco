# 抱怨是没有用的
# 只有根据测试用例去推导题目的意思

# 顺序没关系的

# ps: guess should be after the swap

import sys
sys.stdin = open("shell.in", "r")
sys.stdout = open("shell.out", "w")

n = int(input())
swap = []
guess = []

for i in range(n):
    a, b, g = map(int, input().split())
    swap.append((a-1, b-1))
    guess.append(g-1)

f = 0
for i in range(3):
    # 0:no pebble
    # 1:has pebble
    shell = [0, 0, 0]
    shell[i] = 1
    count = 0
    for j in range(n):
        a, b = swap[j][0], swap[j][1]
        g = guess[j]
        shell[a], shell[b] = shell[b], shell[a]
        if shell[g] == 1:
            count += 1
    if count > f:
        f = count

print(f)