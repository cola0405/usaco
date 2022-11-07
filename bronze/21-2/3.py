# cw的对于的cw拐一定更多
# 因为ccw干扰的，它都得拐回去

cw = ['ES', 'SW', 'WN', 'NE']
ccw = ['WS', 'SE', 'EN', 'NW']

n = int(input())
for i in range(n):
    path = input()
    index = 0
    cw_count = 0
    ccw_count = 0
    while index < len(path)-1:
        if path[index:index+2] in cw:
            cw_count += 1
        elif path[index:index+2] in ccw:
            ccw_count += 1
        index += 1
    if cw_count > ccw_count:
        print('CW')
    else:
        print('CCW')