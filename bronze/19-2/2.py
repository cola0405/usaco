# 贪心
# 牛喜欢两个牧场，为了让他们吃的种类丰富，要求这两个牧场的牧草不同
# 给出n对不同，要你给一个方案
# 答案要求最小，则从1开始考虑给

# 不与之前的牧场矛盾，然后选当前可用的最小的seed
# 题目说的 "no pasture is a favorite of more than 3 cows."
# 其实意味着cur之前最多3个种子没法用 -- 肯定会剩下一个能用的

from collections import defaultdict
import sys
sys.stdin = open("revegetate.in", "r")
sys.stdout = open("revegetate.out", "w")

n, m = map(int, input().split())
diff = defaultdict(list)    # 记录不同的pair

for i in range(m):
    a, b = map(int, input().split())
    if a < b:
        diff[b].append(a)  # 只记录其之前的
    else:
        diff[a].append(b)

grass = ['']   # '' 占位
for pasture in range(1, n+1):
    seeds = ['1', '2', '3', '4']
    for p in diff[pasture]:
        if grass[p] in seeds:
            seeds.remove(grass[p])  # 筛选掉不可用的 -- 与diff pair 矛盾的
    grass.append(seeds[0])  # 选可用种子中最小的

print(''.join(grass[1:]))
