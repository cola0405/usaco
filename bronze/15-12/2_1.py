# 动草稿纸确定边界条件
# 2_1更优

import sys
sys.stdin = open('speeding.in', 'r')
sys.stdout = open('speeding.out', 'w')

n, m = map(int, input().split())

road = [0]*100
cur = 0
for _ in range(n):
    length, limit = map(int, input().split())
    for i in range(cur, cur+length):
        road[i] = limit
    cur += length

car = [0]*100
cur = 0
for _ in range(m):
    length, speed = map(int ,input().split())
    for i in range(cur, cur+length):
        car[i] = speed
    cur += length

max_gap = 0
for i in range(100):
    gap = car[i] - road[i]
    max_gap = max(gap, max_gap)
print(max_gap)
