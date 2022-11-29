# c++可，python超时

# 路程>=k, 超了无所谓，贪到最少步数就行

import sys
sys.stdin = open('race.in', 'r')
sys.stdout = open('race.out', 'w')


k, n = map(int, input().split())
temp = k
for i in range(n):
    x = int(input())
    up_meter = 0
    down_meter = 0
    speed = 0
    time = 0
    while True:
        speed += 1
        up_meter += speed
        time += 1
        if up_meter + down_meter >= k:
            break
        if speed >= x:
            down_meter += speed
            time += 1
            if up_meter + down_meter >= k:
                break
    print(up_meter,down_meter,up_meter+down_meter)
    print(time)
