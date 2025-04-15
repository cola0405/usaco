'''
数学 + 优先队列 + 双向链表（多物体碰撞问题）

题目大意：有 n个粒子排成一行，粒子与反粒子交叉排列，他们的初始运动方向分别是向右、向左、向右、向左、.....
每个粒子的速度可能不同，然后在 Bessie每次观察的时候，粒子的运动方向会往相反方向改变
Bessie的观察规律是：1s后观察一次，然后 2s后观察一次，然后 3s后观察一次......
问各个粒子分别是在第几次观察中消失的

思路：这里需要分析粒子运动的规律
先向右运动 1 秒，再向左运动 2 秒，再向右运动 3 秒，再向左运动 4 秒……
其实刚才运动的本质是，Bessie 第 1 次观察时位于 p+s，第 2 次观察时位于 p−s，然后是 p+2s，然后 p−2s……
可以得到结论：第 2k−1 次观察，位于 p+ks；第 2k 次观察，位于 p−ks
反哞微子反之，第 2k−1 次观察，位于 p-ks；第 2k 次观察，位于 p+ks
我们现在研究正向粒子，如果两粒子相遇，则有 p1+ks = p2-ks, k = (p2-p1)/(s1+s2)
根据 k值，我们可以计算出其是第 2k-1 次观察到粒子消失的所以可以得到 cal(i,j) 中的计算公式

额外要注意的是，对于哞微子，是 k*2 - 1，需要 -1操作
对于反哞微子，它也可能在向右运动时与右边的粒子相遇而消失，那么对于这种情况我们应该对应前面 ——（第 2k 次观察，位于 p+ks）
所以对应 cal() 应该是 k*2 不需要 -1
然后我们可以根据index的奇偶性来判断该微子是什么类型
'''


import heapq

# 计算是第几次观察到两个粒子消失
def cal(i, j):
    return int((p[j]-p[i] + (s[i]+s[j]-1)) // (s[i]+s[j]) * 2 - (1 - i%2))

T = int(input())
for _ in range(T):
    n = int(input())
    p = list(map(int, input().split()))
    s = list(map(int, input().split()))

    # 初始化优先队列，按照相遇的最短时间排序
    pq = []
    for i in range(n-1):
        heapq.heappush(pq, (cal(i, i+1), i, i+1))

    # 初始化双向链表
    L = [-1]*n
    R = [-1]*n
    for i in range(1, n-1):
        L[i] = i-1
        R[i] = i+1
    ans = [-1]*n        # 记录各个粒子分别在第几次观察时消失
    while pq:
        t, i, j = heapq.heappop(pq)
        if ans[i] != -1 or ans[j] != -1: continue       # 有任一粒子已经消失，则跳过
        ans[i] = ans[j] = t
        if L[i] != -1 and R[j] != -1:                   # 两个粒子都还在
            heapq.heappush(pq, (cal(L[i], R[j]), L[i], R[j]))       # 将新的一对粒子加入到优先队列
            R[L[i]] = R[j]                              # 更新双向链表
            L[R[j]] = L[i]
    print(' '.join(map(str, ans)))

