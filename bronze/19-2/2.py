# 牛喜欢两个牧场，为了让他们吃的种类丰富，要求这两个牧场的牧草不同
# 给出n对不同，要你给一个方案
# 答案要求最小，则从1开始考虑给

# 总的思路是根据n对不同，筛除不可用的，在可用的种里选最小的
# 注意str的转换


import sys

sys.stdin = open("revegetate.in", "r")
sys.stdout = open("revegetate.out", "w")

n, m = map(int, input().split())
no_repeat = {}
for i in range(1, n+1):
    no_repeat[i] = []

for i in range(m):
    a, b = map(int, input().split())
    no_repeat[a].append(b)
    no_repeat[b].append(a)

ans = [0]
for pasture in range(1, n+1):
    seeds = ['1', '2', '3', '4']
    for j in no_repeat[pasture]:
        if j > pasture:
            continue
        if str(ans[j]) in seeds:
            seeds.remove(ans[j])
    ans.append(seeds[0])

print(''.join(ans[1:]))
