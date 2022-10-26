import sys
sys.stdin = open('geteven.in', 'r')
sys.stdout = open('geteven.out', 'w')

n = int(input())
d = {'B':[], 'E':[], 'S':[], 'I':[],'O':[],'M':[], 'G':[]}


for i in range(n):
    line = input().split()
    k = line[0]
    v = int(line[1])
    d[k].append(v)

ans = 0
for b in d['B']:
    for e in d['E']:
        for s in d['S']:
            for i in d['I']:
                for o in d['O']:
                    for m in d['M']:
                        for g in d['G']:
                            res = (b+e+2*s+i+e)*(g+o+e+s)*(m+2*o)
                            if res % 2 == 0:
                                ans += 1

print(ans)