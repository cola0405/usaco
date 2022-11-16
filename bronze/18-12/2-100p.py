# 数组模拟法

import sys
sys.stdin = open("blist.in", "r")
sys.stdout = open("blist.out", "w")

n = int(input())
op = []
time = [0]*1100
for i in range(n):
    start, end, amount = map(int, input().split())
    for j in range(start, end+1):
        time[j] += amount

print(max(time))

