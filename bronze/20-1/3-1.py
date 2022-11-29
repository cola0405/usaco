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
        up = mid*(mid-1)//2 + mid
        if mid < x:
            left = mid + 1
            continue
        possible = up + mid*mid
        if possible > k:
            right = mid-1
        else:
            left = mid+1
    if up == k:
        print(mid)
    else:
        down_gap = max(mid*(mid-1)//2 - x*(x-1)//2, 0)
        extend = max(k - up - down_gap, 0)
        if extend == 0:
            print(mid + mid-x)
        else:
            if mid != x:
                print(mid + mid-x+1)
            else:
                print(mid+2)
