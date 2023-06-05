import sys
sys.stdin = open("loan.in", "r")
sys.stdout = open("loan.out", "w")

n,k,m = map(int, input().split())

def fine(x, day):
    already = 0
    while already < n and day>0:
        y = (n-already)//x
        if y < m:
            leftover = (n-already + m-1)/m
            return leftover <= day
        maxmatch = n-x*y
        numdays = (maxmatch-already)//y
        if numdays > day:
            numdays = day
        already += y * numdays
        day -= numdays
    return already >= n

low = 1
high = n
ans = 0
while low<high:
    mid = (low+high+1)//2
    if fine(mid, k):
        low = mid
    else:
        high = mid-1

print(low)

