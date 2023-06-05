import sys
sys.stdin = open("revegetate.in", "r")
sys.stdout = open("revegetate.out", "w")

n,m = map(int, input().split())
ans = 0
already = set()
for _ in range(m):
    t,a,b = input().split()
    if a not in already and b not in already:
        ans += 1
    already.add(a)
    already.add(b)


print('1'+'0'*ans)

