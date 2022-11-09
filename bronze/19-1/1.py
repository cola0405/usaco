# 连接数最多的能处理，其他任意范围的动能处理
# 直接相连的和连接到同一个花圃的要求种类不同
# 连接数+1

import sys

sys.stdin = open("planting.in", "r")
sys.stdout = open("planting.out", "w")


n = int(input())
connections = [0]*(n+1)

for i in range(n-1):
    a, b = map(int, input().split())
    connections[a] += 1
    connections[b] += 1

print(max(connections)+1)
