# 注意，当两个矩形不相交时，xgap*ygap可能负负得正

import sys
sys.stdin = open("billboard.in", 'r')
sys.stdout = open("billboard.out", 'w')

def getArea(x1, y1, x2, y2):
    # init area
    area = (x2 - x1) * (y2 - y1)

    mintop = min(y2, ty2)
    maxbtm = max(y1, ty1)
    minright = min(x2, tx2)
    maxleft = max(x1, tx1)

    xgap = minright - maxleft
    ygap = mintop - maxbtm

    if xgap > 0 and ygap > 0:
        area -= xgap * ygap

    return area


px1,py1,px2,py2 = map(int, input().split())
px3,py3,px4,py4 = map(int, input().split())
tx1,ty1,tx2,ty2 = map(int, input().split())

area1 = getArea(px1,py1,px2,py2)
area2 = getArea(px3,py3,px4,py4)

print(area1+area2)

