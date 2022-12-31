import sys
sys.stdin = open("crossroad.in", "r")
sys.stdout = open("crossroad.out", "w")

record = dict()
n = int(input())
ans = 0
for i in range(n):
    id, side = map(int, input().split())
    if id not in record:
        record[id] = side
    else:
        if record[id] != side:
            ans += 1
        record[id] = side

print(ans)