import sys
sys.stdin = open("crossroad.in", "r")
sys.stdout = open("crossroad.out", "w")

record = [-1]*11
n = int(input())
ans = 0
for i in range(n):
    id, side = map(int, input().split())
    if record[id] == -1:
        record[id] = side
    else:
        if record[id] != side:
            ans += 1
        record[id] = side

print(ans)