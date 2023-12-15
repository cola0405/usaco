# 问题转化为：如何使得每次提问排除的选项最少？
# 想到贪心
# 然后这里，也可以再转化一下解题角度
# 说白了就是找相同特点最多的一对
# 他们相同特点的数量+1就是答案 -- 能够坚持到最后

import sys
sys.stdin = open("guess.in", "r")
sys.stdout = open("guess.out", "w")

n = int(input())
record = [set(input().split()[2:]) for _ in range(n)]

ans = 0
for i in range(n):      # 双重循环找最相似的一对
    for j in range(i+1, n):
        ans = max(ans, len(record[i] & record[j]))  # intersection

print(ans+1)