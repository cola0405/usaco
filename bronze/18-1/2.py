# complete search
# 各种情况模拟出来

# 手撸测试用例
# 数组模拟法
# 注意端点是否取，草稿纸中找规律

# 4
# 0 6
# 4 10
# 3 7
# 4 6

import sys
sys.stdin = open('lifeguards.in', 'r')
sys.stdout = open('lifeguards.out', 'w')

n = int(input())
time = [0]*(1000+1)
shifts = []
for i in range(n):
    start, end = map(int, input().split())
    shifts.append((start, end))
    for i in range(start, end):
        time[i] += 1

ans = 0
for shift in shifts:
    covered_time = 0
    temp = list(time)
    start, end = shift
    for i in range(start, end):
        temp[i] -= 1
    for i in temp:
        if i > 0:
            covered_time += 1
    ans = max(ans, covered_time)

print(ans)
