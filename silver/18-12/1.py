# 二分暴力贪心
import sys
sys.stdin = open("convention.in", "r")
sys.stdout = open("convention.out", "w")

n,m,c = map(int, input().split())
time = sorted(map(int, input().split()))

def fine(min_time):
    bus = 1
    start_time = time[0]
    cows = 1

    for i in range(1, n):
        # time to drive out
        if time[i] > start_time+min_time or cows>=c:
            bus += 1
            start_time = time[i]
            cows = 1
        else:
            cows += 1
    return bus <= m


def binSearch(low, high):
    if low == high:
        return low
    mid = (low+high)//2
    if fine(mid):  # current min_time works
        return binSearch(low, mid)
    else:  # current min_time not working so +1
        return binSearch(mid+1,high)


print(binSearch(0,int(1e9)))

