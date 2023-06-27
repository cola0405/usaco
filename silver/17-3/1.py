# 问题转换
# 说白了就是让A+B尽可能小，然后求A+B的最大值
# sort+贪心+双指针两边逼近(这里用了双端队列替代)
# 又因为数据范围，没办法用线性表，得用hash表

from collections import deque
import sys
sys.stdin = open("pairup.in", "r")
sys.stdout = open("pairup.out", "w")

n = int(input())
cows = []
d = {}
for _ in range(n):
    amount, produce = map(int, input().split())
    d[produce] = amount
    cows.append(produce)
cows.sort()
cows = deque(cows)
ans = 0
while cows:
    ans = max(cows[0]+cows[-1], ans)
    if d[cows[0]] > d[cows[-1]]:
        d[cows[0]] -= d[cows[-1]]
        d[cows[-1]] = 0
        cows.pop()
    else:
        d[cows[-1]] -= d[cows[0]]
        d[cows[0]] = 0
        cows.popleft()
    if len(cows)>0 and d[cows[0]] == 0:
        cows.popleft()
    if len(cows)>0 and d[cows[-1]] == 0:
        cows.pop()

print(ans)

