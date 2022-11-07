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
