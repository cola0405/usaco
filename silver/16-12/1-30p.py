# 超时，但是可以学习
# 加深二分的理解

import sys
sys.stdin = open("haybales.in", "r")
sys.stdout = open("haybales.out", "w")

n,q = map(int, input().split())
cows = list(map(int, input().split()))
cows.sort()


# not less than (包括相等)
def lower_bound(target):
    if target > cows[n-1]:
        return n
    left = 0
    right = n-1
    while left < right:
        mid = (left+right)//2
        # 小于targte，那就敢敢+1
        # 越了target正好是对的
        if cows[mid]<target:
            left = mid+1
        elif cows[mid]>target:
            right = mid-1
        else:
            return mid
    # 二分的条件就是left<=target=<right
    # while 循环出来，left == right
    # 那肯定就是left not less than target
    return left

# greater (一定是大于)
def upper_bound(target):
    if target >= cows[n-1]:
        return n
    left = 0
    right = n-1
    while left < right:
        #print(left,right,target)
        mid = (left+right)//2
        if cows[mid]<target:
            left = mid+1
        # 不让cows[right]有机会比target小
        # -1可能会使cows[right] 越过target，比target小
        elif cows[mid]>target:
            right = mid
        else:
            # greater 则遇到相等的需要取mid+1
            return mid+1

    # while 循环出来是 right >= target
    # 如果恰好相等的话是需要+1的
    #print(cows[right],target)
    return right


for i in range(q):
    start, end = map(int, input().split())
    inx1 = lower_bound(start)
    inx2 = upper_bound(end)
    res = inx2-inx1
    #print(inx1,inx2)
    print(res)
