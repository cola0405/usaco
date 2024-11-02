# 3_2 最优
# 1.根据生病的人筛出可能坏的牛奶
# 2.看分别多少人喝了这些牛奶
# 3.进行连续交集操作，set最后的长度就是答案 -- 准备这个数量的药才够
import sys
sys.stdin = open('badmilk.in', 'r')
sys.stdout = open('badmilk.out', 'w')
N, M, D, S = map(int, input().split())

record = [tuple(map(int, input().split())) for _ in range(D)]
bad = set(range(1,M+1))
for _ in range(S):
    s, st = map(int, input().split())
    possible = set()
    for p, m, t in record:
        if p == s and t < st:
            possible.add(m)
    bad = bad & possible  # 交集，要生病的人都喝了的

ans = 0
for b in bad:
    count = set()
    for p,m,t in record:
        if m == b:
            count.add(p)
    ans = max(ans, len(count))

print(ans)