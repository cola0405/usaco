# string op

import sys
sys.stdin = open("cowsignal.in", 'r')
sys.stdout = open("cowsignal.out", 'w')

n,m,k = map(int, input().split())
signal = []
for i in range(n):
    signal.append(input())

for line in signal:
    temp = ''
    for c in line:
        temp += c*k
    for i in range(k):
        print(temp)
