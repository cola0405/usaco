import sys
sys.stdin = open('gymnastics.in', 'r')
sys.stdout = open('gymnastics.out', 'w')

k, n = map(int, input().split())
ranks = [list(map(int,input().split())) for i in range(k)]

def isConsistent(a,b):
    for rank in ranks:
        if rank.index(a) > rank.index(b):
            return False
    return True

ans = 0
for i in range(1, n+1):
    for j in range(i+1, n+1):
        if isConsistent(i,j) or isConsistent(j,i):
            ans += 1
print(ans)