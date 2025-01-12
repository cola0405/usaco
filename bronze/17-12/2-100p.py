# 模拟
import sys
sys.stdin = open("shuffle.in", 'r')
sys.stdout = open("shuffle.out", 'w')

n = int(input())
shuffle = list(map(int, input().split()))
a = input().split()
ins = [shuffle.index(i) for i in range(1,n+1)]

for _ in range(3):
    last = [''] * n
    for i in range(n): last[ins[i]] = a[i]
    a = last

for i in a: print(i)

