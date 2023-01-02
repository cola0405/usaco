# 熟练运用交集的几何知识

import sys
sys.stdin = open('billboard.in', 'r')
sys.stdout = open('billboard.out', 'w')

ax,ay,bx,by = map(int, input().split())
cx,cy,dx,dy = map(int, input().split())

min_top = min(by,dy)
min_right = min(bx, dx)

max_bottom = max(ay,cy)
max_left = max(ax,cx)

b_area = (by-ay) * (bx-ax)
ans = b_area

#    ******
#    *    *
# *************
# *  *    *   *
# *************
#    *    *
#    ******
# 仍然需要覆盖整个板
if (min_top < by and max_bottom > ay) \
            or (min_right < bx and max_left > ax):
    pass

# 相交
elif min_top > max_bottom and min_right > max_left:
    dy = min_top - max_bottom
    dx = min_right - max_left
    # 需要减去相交部分
    if dy == (by-ay) or dx == (bx-ax):
        ans -= dx*dy

print(ans)
