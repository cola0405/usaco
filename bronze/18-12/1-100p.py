# 轮、周期 模板


import sys
sys.stdin = open("mixmilk.in", "r")
sys.stdout = open("mixmilk.out", "w")

c1, m1 = map(int, input().split())
c2, m2 = map(int, input().split())
c3, m3 = map(int, input().split())

c = [None, c1,c2,c3]
m = [None, m1,m2,m3]

# 轮、周期 模板
op = [(1, 2), (2, 3), (3, 1)]

for i in range(100):
    # 轮、周期 模板
    src, dest = op[i%3]
    if m[src] + m[dest] <= c[dest]:
        m[dest] += m[src]
        m[src] = 0
    else:
        m[src] = m[src] + m[dest] - c[dest]
        m[dest] = c[dest]

for i in m[1:]:
    print(i)


