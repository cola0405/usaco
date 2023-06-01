# 题目误导
# 最值问题，出现在端点

import sys
sys.stdin = open("teleport.in", "r")
sys.stdout = open("teleport.out", "w")

n = int(input())
pair = [tuple(map(int, input().split())) for _ in range(n)]
possible_y = set()
origin = 0
for p in pair:
    a,b = p
    origin += abs(b-a)
    possible_y.add(a)
    possible_y.add(b)

max_saver = 0
for y in possible_y:
    saver = 0
    for p in pair:
        l,r = min(p),max(p)
        tl,tr = min(0,y), max(0,y)

        if tl >= l and tr <= r:
            saver += tr-tl
        else:
            saver += max(0, (r-l) - (abs(l-tl)+abs(r-tr)))
    max_saver = max(saver, max_saver)


print(origin-max_saver)

