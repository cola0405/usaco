import sys
sys.stdin = open('lifeguards.in', 'r')
sys.stdout = open('lifeguards.out', 'w')

n = int(input())
t = [0]*1001
shifts = []
for i in range(n):
    start, end = map(int, input().split())
    for j in range(start, end):
        t[j] += 1
    shifts.append((start, end))

ans = 0
total = 1001 - t.count(0)
for start,end in shifts:
    x = total
    for j in range(start, end):
        if t[j] == 1:
            x -= 1
    ans = max(ans, x)

print(ans)