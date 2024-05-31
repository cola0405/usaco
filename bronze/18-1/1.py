# 熟练运用交集的几何知识

# consider of this situation
#    ******
#    *    *
# *************
# *  *    *   *
# *************
#    *    *
#    ******

import sys
sys.stdin = open('billboard.in', 'r')
sys.stdout = open('billboard.out', 'w')
ax,ay,bx,by = map(int, input().split())
cx,cy,dx,dy = map(int, input().split())

min_top = min(by,dy)
max_bottom = max(ay,cy)
min_right = min(bx, dx)
max_left = max(ax,cx)
ans = (by-ay) * (bx-ax)

# the overlap rectangle is cover the upper part or lower part
if (min_right, min_top) == (bx, by) or (max_left, max_bottom) == (ax, ay):
    t_height = min_top - max_bottom
    t_width = min_right - max_left
    if t_height == (by-ay) or t_width == (bx-ax):   # check valid rectangle
        ans -= t_height * t_width
print(ans)
