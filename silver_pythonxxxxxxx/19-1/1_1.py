# 最大入度+1

# 观察测试用例：
# (1,3) (2,3) (4,3) 需要4种

import sys
sys.stdin = open("planting.in", "r")
sys.stdout = open("planting.out", "w")

n = int(input())
in_degree = [0]*(n+1)

for i in range(n-1):
    a, b = map(int, input().split())
    in_degree[a] += 1
    in_degree[b] += 1

print(max(in_degree)+1)
