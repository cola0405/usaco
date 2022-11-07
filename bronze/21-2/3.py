
# 画一个单向箭头，绕着原点转
# 累计转动的角度
# 看最后结果是顺还是逆

# 顺逆是可以相消的
# 基于此，我们只要看顺多还是逆多就行


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