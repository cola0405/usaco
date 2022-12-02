# 再就是为什么最多就是+2
# 首先了解一个前提，当前h，是k以下最大的h
# h+1走的路程，必然超过k（不含等于）
# 如果h+1走的路程刚好是k的话，那么取的就不是h而是h+1了

# 再看一下"h速度下time+2"和"h+1"效果的区别
# h: 2*h
# h+1 : h+1+h = 2*h+1

# 因为2*h+1>k
# 所以2*h>=k （h、k都为整数的前提下，得到此不等式）

import math
import sys
sys.stdin = open('race.in', 'r')
sys.stdout = open('race.out', 'w')

k, n = map(int, input().split())
p = 1
while p*(p+1) < k*2:
    p += 1

for i in range(n):
    x = int(input())
    if x >= p:
        print(p)
        continue
    # h是k以下最大的h
    # h+1走的路程肯定是大于k（不取等号）
    # 如果h+1走的路程刚好是k的话，那么取的就不是h而是h+1了
    h = int(math.sqrt((2*k+x**2-x)/2))
    meters = (2*h**2-x**2+x)/2
    if meters == k:
        print(2*h - x)
    # 最接近k的h，如果其差距小于h
    # 那么就在h速度下time+1
    # （不是x，因为我们要贪心，尽可能快）
    elif k - meters <= h:
        print(2*h - x + 1)
    # 最接近k的h，如果其差距大于h
    # 那么time+2
    # 注意，这里不升h，因为我们的策略是从下往上逼近
    # (你当然也可以从上往下逼近，但是不方便操作)
    else:
        print(2*h - x + 2)
