'''
递减子序列划分问题

题目大意：
给定 N头奶牛，每头奶牛有不同的初始位置和速度
奶牛们在无限长跑道上跑 T分钟
求出奶牛们不相撞所需的最少跑道数。

解题思路：先求出每头牛最后停下的位置 end
如果不想让奶牛们相撞，则要使得 end的子序列是递减的
直接暴力遍历会O(n^2)超时
这里可以用 upper_bound快速找到应插入的位置，最终时间复杂度 O(nlogn)
'''

from bisect import *
import sys
sys.stdin = open('cowjog.in', 'r')
sys.stdout = open('cowjog.out', 'w')

n,t = map(int, input().split())
end = []
for _ in range(n):
    start, speed = map(int, input().split())
    end.append(start + t*speed)             # 奶牛们停下的位置end

q = []                                      # 维护 q在插入的过程中保持递增
for e in end[::-1]:                         # 从出发位置靠后的奶牛开始，此前提下， end的判断才能确保不相撞
    inx = bisect_right(q, e)                # 在 upper_bound位置插入，q总会保持递增
    if inx == len(q):
        q.append(e)
        continue
    q[inx] = e
print(len(q))


