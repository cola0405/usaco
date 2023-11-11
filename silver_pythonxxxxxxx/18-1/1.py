# 把每对点拆出来，按先后顺序排列
# 根据当前点是start还是end进行贪心统计sum和min_own

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
    gap = p-last
    if len(s) == 1:
        # do have start
        for k in s:
            own[k] += gap
    if len(s) > 0:  # 贪心积累total 只有左边有待匹配的start则都可累加
        total += gap
    if pair_id in s:  # current is the end
        s.pop(pair_id)  # 弹出待匹配队列(不是queue)
    else:   # current is the start
        s[pair_id] = None  # 加入匹配队列
    last = p

print(total - min(own))


