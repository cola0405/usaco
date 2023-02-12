# 按start排序
# start point往前到last就是独占的
# 再结合括号匹配

import sys
sys.stdin = open("lifeguards.in", "r")
sys.stdout = open("lifeguards.out", "w")

n = int(input())

points = []
for i in range(n):
    b,e = map(int, input().split())
    pair_id = i
    points.append((b,pair_id))
    points.append((e,pair_id))

def by_point(item):
    return item[0]
points.sort(key=by_point)


total = 0
last = 0

# 当有序字典用
s = dict()

own = [0]*n
for r in points:
    p, pair_id = r
    if len(s) == 1:
        # dict first item
        for k in s:
            own[k] += p - last
            break
    if len(s) > 0:
        total += p - last
    if id in s:
        s.pop(pair_id)
    else:
        s[pair_id] = None
    last = p

print(total - min(own))


