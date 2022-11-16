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

pastures = [0]*(n+1)
for i in range(1,5):
    j = 0
    while j <= n:
        if pastures[j] == 0:
            for k in range(1, j):
                if k in no_repeat[j]:
                    break
            else:
                pastures[j] = str(i)
        j += 1
print(pastures)
print(''.join(pastures[1:]))