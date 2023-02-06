import sys
sys.stdin = open('bcount.in', 'r')
sys.stdout = open('bcount.out', 'w')

n,q = map(int, input().split())

cows = []
for i in range(n):
    cows.append(int(input()))

a = [0]
b = [0]
c = [0]

for i in range(n):
    if cows[i] == 1:
        a.append(a[-1]+1)
    else:
        a.append(a[-1])

    if cows[i] == 2:
        b.append(b[-1]+1)
    else:
        b.append(b[-1])

    if cows[i] == 3:
        c.append(c[-1]+1)
    else:
        c.append(c[-1])

for r in range(q):
    start,end = map(int, input().split())
    h_num = a[end] - a[start-1]
    g_num = b[end] - b[start-1]
    j_num = c[end] - c[start-1]

    print(h_num, g_num, j_num)


