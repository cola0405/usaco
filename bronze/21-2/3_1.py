# 数量必定是偶数
# 上下左右要刚好抵消，一定是偶数

# 为什么cw和ccw的数量不能相等
# 如果相等的话，那就没有多余的角了，也就不可能形成闭合区域

cw = ['ES', 'SW', 'WN', 'NE']
ccw = ['WS', 'SE', 'EN', 'NW']

n = int(input())
for _ in range(n):
    path = input()
    cw_count = 0
    ccw_count = 0
    for i in range(len(path)-1):
        turn = path[i:i+2]
        if turn in cw:
            cw_count += 1
        elif turn in ccw:
            ccw_count += 1

    if cw_count > ccw_count:
        print('CW')
    else:
        print('CCW')

