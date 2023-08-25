# 动草稿纸确定边界条件
import sys
sys.stdin = open('speeding.in', 'r')
sys.stdout = open('speeding.out', 'w')

n, m = map(int, input().split())

limit = [0]*101
cur = 1
for _ in range(n):
    length, speed_limit = map(int, input().split())
    for i in range(cur, cur+length):
        limit[i] = speed_limit
    cur += length

journey = [0]*101
cur = 1
for _ in range(m):
    length, speed = map(int ,input().split())
    for i in range(cur, cur+length):
        journey[i] = speed
    cur += length

max_gap = 0
for i in range(1, 101):
    gap = journey[i] - limit[i]
    max_gap = max(gap, max_gap)
print(max_gap)
