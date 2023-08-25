# 数组模拟

import sys
sys.stdin = open('lifeguards.in', 'r')
sys.stdout = open('lifeguards.out', 'w')

n = int(input())
time = [0]*(1000+1)
shifts = []
for _ in range(n):
    start, end = map(int, input().split())
    shifts.append((start, end))
    for i in range(start, end):
        time[i] += 1

ans = 0
for start, end in shifts:
    for i in range(start, end):  # fire
        time[i] -= 1

    covered = len(time) - time.count(0)
    ans = max(ans, covered)

    for i in range(start, end):  # recover
        time[i] += 1

print(ans)