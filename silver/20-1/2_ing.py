import math
import sys
sys.stdin = open("loan.in", "r")
sys.stdout = open("loan.out", "w")
n,k,m = map(int, input().split())

def fine(x, day):
    already = 0
    while already < n and day>0:
        y = (n-already)//x  # 变化不可skip，积累变化的时候可以skip
        if y <= m:
            return already + m*day >= n

        # already只是每次循环+1的话，让y值变小1都费劲(当x的值足够大时)
        # 这里需要skip优化，gap是要让y值变化，already需要累积的量（列方程得表达式）
        gap = n-already-(y-1)*x
        # gap//y 则是already积累所需天数
        # 可以状态压缩的，快进的天数
        # 可能不是整除，需要向上取整!!!!!!
        need = max(math.ceil(gap/y), 1)  # 当前y足够支撑下次变化，则不需要skip，按正常1天算
        if need >= day:  # y不会再变化，则不需要继续模拟，可以skip，直接计算结果了
            return already + y*day >= n
        already += y*need  # 不+gap，因为会忽略掉加了skip后over the line的情况
        day -= need
    return already >= n

low = 1
high = n
while low<high:
    mid = (low+high+1)//2
    # print(mid)
    if fine(mid, k):
        low = mid
    else:
        high = mid-1

print(low)