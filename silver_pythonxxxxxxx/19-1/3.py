# 落脚有在外面的就不会被遮挡（利用好角度固定45°）
# 落脚点可能重叠，这是和lifeguard不一样的地方
# 需要做边界处理

# 方法不见得是最简单的，但是基于lifeguard的括号匹配压缩查找效率来做的
# 括号匹配需要last来记录已pop出去的信息

import sys
sys.stdin = open("mountains.in", "r")
sys.stdout = open("mountains.out", "w")

n = int(input())

points = []
for i in range(n):
    x, y = map(int, input().split())
    pair_id = i
    left = (x-y, pair_id)
    right = (x+y, pair_id)
    points.append(left)
    points.append(right)

def by_point(item):
    return item[0]

points.sort(key=by_point)

d = dict()
ans = n
last = 0
for i in range(2*n):
    p, pair_id = points[i]

    blocked = False
    if pair_id in d:
        # check whether inside
        for k in d:             # it will be ok if the left is the first endpoint
            if k != pair_id:
                blocked = True
            break
        if blocked:
            ans -= 1
            d.pop(pair_id)
            continue

        # left check
        cnt = 0
        for k in d:
            if cnt == 1:
                if d[k] == d[pair_id]:
                    ans -= 1
                break
            cnt += 1

        # right check
        if last == p:
            ans -= 1
        d.pop(pair_id)
    else:
        d[pair_id] = p
    last = p


print(ans)
