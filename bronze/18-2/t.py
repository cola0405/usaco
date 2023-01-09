import sys

sys.stdin = open("hoofball.in", "r")
sys.stdout = open("hoofball.out", "w")

n = int(input())
lst = list(map(int, input().split()))
lst.sort()

c = [0]*len(lst)
c[1] += 1
c[n-2] += 1

def target(i):
    left = lst[i-1]
    right = lst[i+1]
    if lst[i]-left <= right-lst[i]:
        return i-1
    else:
        return i+1


for i in range(1, n-1):
    c[target(i)] += 1

ans = 0
for i in range(n-1):
    if c[i]==2 and c[i+1]==2:
        ans += 1
    elif c[i] == 0:
        ans += 1
if c[n-1]==0:
    ans += 1

print(lst)
print(c)
print(ans)