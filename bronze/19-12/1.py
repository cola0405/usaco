import sys
sys.stdin = open('gymnastics.in', 'r')
sys.stdout = open('gymnastics.out', 'w')

k, n = map(int, input().split())
ranks = [list(map(int,input().split())) for i in range(k)]

ans = 0
for a in range(1, n+1):
    for b in range(a+1, n+1):
        count1, count2 = 0, 0
        for r in ranks:
            if r.index(a) < r.index(b):
                count1 += 1
            else:
                count2 += 1
        if count1 == k or count2 == k:
            ans += 1
print(ans)