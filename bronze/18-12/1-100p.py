# 轮、周期 模板


import sys
sys.stdin = open('mixmilk.in', 'r')
sys.stdout = open('mixmilk.out', 'w')

c1, m1 = map(int, input().split())
c2, m2 = map(int, input().split())
c3, m3 = map(int, input().split())

capacity = [None, c1, c2, c3]
milk = [None, m1, m2, m3]

# 记录动作
op = [(1,2), (2,3), (3,1)]

for i in range(100):
    # 取动作
    src, dest = op[i%3]
    if milk[src] + milk[dest] <= capacity[dest]:
        milk[dest] += milk[src]
        milk[src] = 0
    else:
        milk[src] -= capacity[dest] - milk[dest]
        milk[dest] = capacity[dest]

for i in milk[1:]:
    print(i)


