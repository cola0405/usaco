# 排序 + bound问题
# 每个植物的可行的天数会在一个范围里面
# 求所有范围的交集，即答案

# 如何确定可行天数的范围
# 从高到低看相邻两项，根据 speed 和 height 的关系来确定天数的可行范围
# 只需要看相邻两项递推过去即可，不需要双重for循环进行全检查

T = int(input())
for r in range(T):
    n = int(input())
    plants = list(map(int, input().split()))
    speeds = list(map(int, input().split()))
    taller = list(map(int, input().split()))  # 比i更高的植物的数量
    taller_idx = {taller[i]: i for i in range(n)}

    low = 0
    high = float('inf')
    for i in range(n-1):  # 从最高的开始 -- 没有植物比i高 -- 相当于已经排序了
        idx1 = taller_idx[i]
        height1, speed1 = plants[idx1], speeds[idx1]

        idx2 = taller_idx[i+1]
        height2, speed2 = plants[idx2], speeds[idx2]

        # 确定天数的可行范围
        if speed1>speed2:
            low = max(low, (height2-height1)//(speed1-speed2)+1)  # 要严格大于
        elif speed1==speed2:
            if height1<=height2:
                low = -1
                break
        else:
            if height1<=height2:
                low = -1
                break  # 要严格小于，好好理解这里的-1处理
            high = min(high, (height1-height2-1)//(speed2-speed1))  # 刚好整除是不行的

    if low>high:  # 若可行范围为空，则-1
        print(-1)
    else:
        print(low)

'''
1
3
4 8 5
3 1 3
2 1 0
'''
