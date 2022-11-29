# 无法通过二分+驼峰规律
# 因为有可能会中途横着走一段再降速，不一定是驼峰形状

import math
import sys
sys.stdin = open('race.in', 'r')
sys.stdout = open('race.out', 'w')


k, n = map(int, input().split())
temp = k
for i in range(n):
    x = int(input())
    k = temp
    if x*(x+1)//2 >=k:
        for num in range(x+1):
            if num * (num + 1) // 2 >= k:
                print(num)
                break
        continue
    # to x
    meters = x*(x+1)//2 - x
    k -= meters
    time = x-1

    left = 1
    right = k
    h = 0
    while left < right:
        h = (left+right)//2
        if (2*h+1)*x+h**2 == k:
            break
        elif (2*h+1)*x+h**2 >= k:
            right = h - 1
        else:
            left = h + 1
    while h > 0 and (2 * h + 1) * x + h ** 2 > k:
        h -= 1
    time += 2*h + 1
    s = (2 * h + 1)*x + h**2
    k -= (2 * h + 1)*x + h**2
    if k > 0 and k < h+x:
        time += 1
    elif k > 0:
        time += math.ceil(k/x)
    print(time)




