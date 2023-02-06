
def comfortable(temp):
    for temperature in temp:
        if temperature>0:
            return False
    return True


n,m = map(int, input().split())

target = [0]*101
for r in range(n):
    s, t, c = map(int, input().split())
    for j in range(s, t+1):
        target[j] += c

acs = []
for r in range(m):
    ac = tuple(map(int, input().split()))
    acs.append(ac)


from itertools import combinations
ans = float('inf')
#for num in range(1,11):
for num in range(4):
    cbns = combinations(acs, num)

    for cbn in cbns:
        temp = target[:]
        cost = 0
        for ac in cbn:
            a, b, p, m = ac
            for i in range(a, b+1):
                temp[i] -= p
            cost += m
        if comfortable(temp):
            ans = min(cost, ans)

print(ans)


