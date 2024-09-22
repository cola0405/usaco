# cw的对于的cw拐一定更多
# 因为ccw干扰的，它都得拐回去

CW = ['ES', 'SW', 'WN', 'NE']
CCW = ['WS', 'SE', 'EN', 'NW']

n = int(input())
for _ in range(n):      # n testcase
    s = input()
    cw = ccw = 0
    for i in range(len(s)-1):
        if s[i:i+2] in CW:
            cw += 1
        elif s[i:i+2] in CCW:
            ccw += 1
    if cw > ccw:
        print('CW')
    else:
        print('CCW')