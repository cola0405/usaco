# 2D geometry
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
min_right = min(bx, dx)
max_bottom = max(ay,cy)
max_left = max(ax,cx)
ans = (by-ay) * (bx-ax)

# 仍然需要覆盖整个板
if (min_top < by and max_bottom > ay) \
            or (min_right < bx and max_left > ax):
    pass
