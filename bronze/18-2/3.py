# 遇到非-1的，往前更新状态
# 最后统计必为breakout的作为min
# max = min + missing

import sys
sys.stdin = open('taming.in', 'r')
sys.stdout = open('taming.out', 'w')

NO_BREAKOUT = -2
BREAKOUT = 0
MISSING = -1

n = int(input())
log = list(map(int, input().split()))

for i in range(n):
    if log[i] != -1:
        j = 0
        days = log[i]
        while j < days:
            log[i-j] = NO_BREAKOUT
            j += 1
        log[i-j] = BREAKOUT

log[0] = BREAKOUT

# min
min_ans = 0
max_ans = 0
for i in log:
    if i == BREAKOUT:
        min_ans += 1
        max_ans += 1
    elif i == MISSING:
        max_ans += 1

print(min_ans, max_ans)
