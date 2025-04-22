'''
c++
图 + dp

题目大意：
已知城市 i到 i+1,i+2,... 航线数量的奇偶性，航线中的城市满足关系 c1 < c2 < c3 < ... (只能往更大的城市飞)
航线中可能包含多个城市，求直达航线 (没有中转城市)的数量

解题思路：
从后往前枚举城市 i，j
然后枚举所有与城市 i相邻的中间节点 k，统计所有可通过 k到 j的航线数量为 cnt
如果 cnt的奇偶性和 i到 j航线数量的奇偶性不一致，那就说明 i到 j一定需要有一个直达的航线

额外需要补充的是，如何统计所有中间节点到 j的航线数量比较好？
其实可以不用直接统计数量，把奇偶性异或累计起来即可
'''


from collections import defaultdict
n = int(input())
p = defaultdict(lambda: defaultdict(int))       # 记录 a到 b航线数量的奇偶性
g = defaultdict(lambda: defaultdict(int))       # 记录 a到 b之间是否有直达的航线，1——有，0——没有
for i in range(1, n):
    s = list(map(int, input()))
    for j in range(len(s)):
        p[i][i+j+1] = s[j]            # 记录 i到后续节点的航线数量的奇偶性

ans = 0
for i in range(1, n+1)[::-1]:
    for j in range(i+1, n+1):
        cnt = 0
        for k in range(i+1, j):     # 枚举中间节点 k
            if g[i][k]:             # 看与 i相邻的城市有没有可达 j的
                cnt ^= p[k][j]      # 累计奇偶性
        if cnt != p[i][j]:          # 如果 cnt与 p[i][j] 不一致，那说明我们需要添加一条 i到 j的直达航线来达到题目的奇偶性要求
            g[i][j] = 1
            ans += 1
print(ans)
