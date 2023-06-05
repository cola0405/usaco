import sys
sys.stdin = open("berries.in", "r")
sys.stdout = open("berries.out", "w")

n,k = map(int, input().split())
berries = list(map(int, input().split()))
berries.sort(reverse=True)

import heapq
def get_remain(unit):
    pick = []
    backup = []
    for i in range(n):
        berry = berries[i]
        while berry >= unit and len(pick)<k:
            pick.append(unit)
            berry -= unit
        heapq.heappush(backup, -berry)  # heapq 默认最小堆
    if len(pick) + len(backup) < k:  # k个篮子装不满，当前unit就不用看了，差值太大
        return 0
    for j in range(len(pick), k):
        pick.append(-1*heapq.heappop(backup))
    return sum(pick[k//2:])

ans = 0
for i in range(1, berries[0]):  # n，k的值都很小，经过heap优化后暴力贪心就行
    # i assuming amount
    remain = get_remain(i)
    ans = max(remain, ans)

print(ans)