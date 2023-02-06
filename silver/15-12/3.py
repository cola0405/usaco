import sys
sys.stdin = open('bcount.in', 'r')
sys.stdout = open('bcount.out', 'w')

n,q = map(int, input().split())

p = [[],[0],[0],[0]]
for i in range(n):
    cow = int(input())
    for j in range(1,4):
        if j == cow:
            p[j].append(p[j][-1] + 1)
        else:
            p[j].append(p[j][-1])

H = 1
G = 2
J = 3
for r in range(q):
    start,end = map(int, input().split())
    h_num = p[H][end] - p[H][start-1]
    g_num = p[G][end] - p[G][start-1]
    j_num = p[J][end] - p[J][start-1]

    print(h_num, g_num, j_num)


