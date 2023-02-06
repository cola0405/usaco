from itertools import permutations
import sys
sys.stdin = open("hps.in", "r")
sys.stdout = open("hps.out", "w")

p = [[0],[0],[0]]
d = {"H":0, "P":1, "S":2}

n = int(input())
for i in range(n):
    g = input()
    for j in range(3):
        if j == d[g]:
            p[j].append(p[j][-1]+1)
        else:
            p[j].append(p[j][-1])

ans = 0
for i in range(1,n+1):
    for c in permutations(range(3),2):
        a, b = c
        left = p[a][i]
        right = p[b][-1] - p[b][i]

        ans = max(left+right, ans)

print(ans)


