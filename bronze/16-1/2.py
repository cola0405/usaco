# 完全搜索
# 重在代码能力

import sys
sys.stdin = open('angry.in', 'r')
sys.stdout = open('angry.out', 'w')

def right(cur):
    radius = 1
    while cur < len(hb):
        j = cur+1
        while j < len(hb) and hb[cur] + radius >= hb[j]:
            j += 1
        if j == cur+1:
            break
        cur = j-1
        radius += 1
    return cur

def left(cur):
    radius = 1
    while cur > 0:
        j = cur-1
        while j >= 0 and hb[cur] - radius <= hb[j]:
            j -= 1
        if j == cur-1:
            break
        cur = j+1
        radius += 1
    return cur

n = int(input())
hb = sorted([int(input()) for _ in range(n)])

ans = 1  # 最少都炸一个
for i in range(n):
    ans = max(ans, right(i)-left(i)+1)

print(ans)



