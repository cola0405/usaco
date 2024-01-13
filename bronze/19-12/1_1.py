import sys
sys.stdin = open('gymnastics.in', 'r')
sys.stdout = open('gymnastics.out', 'w')

k, n = map(int, input().split())
ranks = [list(map(int,input().split())) for i in range(k)]

ans = 0
for a in range(1, n+1):
    for b in range(a+1, n+1):
        a_win, b_win = 0, 0
        for r in ranks:
            if r.index(a) < r.index(b):
                a_win = 1
            else:
                b_win = 1
        if a_win+b_win == 1:
            ans += 1
print(ans)