# 在下面是通过time+1来补，那为什么不可以在顶峰呢？？？
import math
import sys
sys.stdin = open('race.in', 'r')
sys.stdout = open('race.out', 'w')


k, n = map(int, input().split())
temp = k
for i in range(n):
    x = int(input())
    left = 0
    right = k
    up = 0
    down = 0
    while left <= right:
        mid = (left+right)//2
        meters = (2*mid**2-x**2+x)/2
        if meters > k:
            right = mid-1
        else:
            left = mid+1
    print(mid)
