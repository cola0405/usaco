# 这优先队列用的真的6。。。
import sys
sys.stdin = open("cowdance.in", "r")
sys.stdout = open("cowdance.out", "w")

n,t = map(int, input().split())
cow = [int(input()) for _ in range(n)]

import heapq
def fine():
    the_time = 0
    stage = []
    for i in range(n):
        if len(stage) == k:
            the_time = heapq.heappop(stage)
        if the_time + cow[i] > t:
            return False
        heapq.heappush(stage, the_time+cow[i])
    return True


low = 1
high = t

while low<high:
    k = (low+high)//2
    if fine():
        high = k
    else:
        low = k+1

print(low)



