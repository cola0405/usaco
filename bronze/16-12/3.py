# string op

import sys
sys.stdin = open("cowsignal.in", 'r')
sys.stdout = open("cowsignal.out", 'w')

n,m,k = map(int, input().split())
signal = []
for i in range(n):
    signal.append(input())

ans = []
for line in signal:
    i = 0
    temp = ''
    while i < m:
        j = i
        while j+1 < m and line[j] == line[j+1]:
            j += 1
        temp += line[i:j+1]*k
        i = j+1
    for i in range(k):
        ans.append(temp)

for i in ans:
    print(i)
